"""Small local web server for the question-bank study app."""

import importlib.util
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
BANKS = ROOT / "question_banks"


def load_banks():
    result = {}
    for path in sorted(BANKS.glob("*.py")):
        if path.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"bank_{path.stem}", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        raw = getattr(module, "questions", None)
        if not isinstance(raw, dict):
            continue
        if raw and all(isinstance(value, dict) for value in raw.values()):
            topics = raw
        else:
            topics = {"All questions": raw}
        result[path.stem] = {
            topic: [{"question": str(q), "answer": str(a)} for q, a in entries.items()]
            for topic, entries in topics.items()
        }
    return result


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/banks":
            try:
                body = json.dumps(load_banks(), ensure_ascii=False).encode("utf-8")
            except Exception as exc:
                self.send_error(500, str(exc))
                return
            content_type = "application/json; charset=utf-8"
        elif path in ("/", "/index.html"):
            body = (ROOT / "index.html").read_bytes()
            content_type = "text/html; charset=utf-8"
        elif path == "/app.js":
            body = (ROOT / "app.js").read_bytes()
            content_type = "text/javascript; charset=utf-8"
        elif path == "/style.css":
            body = (ROOT / "style.css").read_bytes()
            content_type = "text/css; charset=utf-8"
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the local test-prep web app")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    print(f"Open http://localhost:{args.port}")
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
