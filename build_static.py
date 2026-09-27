"""Create the static site that Vercel publishes."""

import json
import shutil
from pathlib import Path
from urllib.parse import unquote

from server import load_banks


root = Path(__file__).resolve().parent
output = root / "dist"
output.mkdir(exist_ok=True)

for name in ("index.html", "app.js", "style.css"):
    shutil.copy2(root / name, output / name)

banks = load_banks()
(output / "banks.json").write_text(
    json.dumps(banks, ensure_ascii=False, separators=(",", ":")),
    encoding="utf-8",
)
for image in {
    item["image"]
    for topics in banks.values()
    for questions in topics.values()
    for item in questions
    if "image" in item
}:
    name = unquote(Path(image).name)
    destination = output / "assets" / "cse320" / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / "cse320" / name, destination)
print(f"Built static site in {output}")
