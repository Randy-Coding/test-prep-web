"""Create the static site that Vercel publishes."""

import json
import shutil
from pathlib import Path

from server import load_banks


root = Path(__file__).resolve().parent
output = root / "dist"
output.mkdir(exist_ok=True)

for name in ("index.html", "app.js", "style.css"):
    shutil.copy2(root / name, output / name)

(output / "banks.json").write_text(
    json.dumps(load_banks(), ensure_ascii=False, separators=(",", ":")),
    encoding="utf-8",
)
print(f"Built static site in {output}")
