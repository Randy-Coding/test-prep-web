"""Check reviewed MT2 records and independently verify process traces.

Run from the repository root: python scripts/validate_cse320_mt2.py
"""
import ast
import importlib.util
import itertools
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("mt2", ROOT / "question_banks/CSE320_MT2.py")
bank = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bank)
review_topics = {topic: entries for topic, entries in bank.questions.items()
                 if topic.endswith(" review session")}
core_topics = {topic: entries for topic, entries in bank.questions.items()
               if topic not in review_topics}
records = {a["id"]: (q, a) for entries in core_topics.values() for q, a in entries.items()}
assert len(records) == sum(map(len, core_topics.values())) == 137
assert {topic: len(entries) for topic, entries in core_topics.items()} == {
    "PROCESSES": 31,
    "SIGNALS": 18,
    "HW5 [Shell]": 22,
    "HW3 [Compiler]": 5,
    "HEAP MEMORY": 36,
    "VIRTUAL MEMORY": 25,
}
vm = bank.questions["VIRTUAL MEMORY"]
assert {r["id"] for r in vm.values()} == {f"VM{i:02}" for i in range(1, 26)}
assert {r.get("image") for r in vm.values()} == {
    "cse320/page_table.png", "cse320/page_table_hard.svg"
}
assert all(r["image"] == ("cse320/page_table_hard.svg" if q.startswith("⭐ Hard: ")
                          else "cse320/page_table.png") for q, r in vm.items())
assert all(q.startswith("⭐ ") for q in vm)
assert sum(q.startswith("⭐ Easy: ") for q in vm) == 10
assert sum(q.startswith("⭐ Hard: ") for q in vm) == 15
assert sum(r["subcategory"] == "Page-fault access counts" for r in vm.values()) == 0
assert sum(r["subcategory"] == "Access counts" for r in vm.values()) == 7
assert all("page fault" not in prompt.lower() and "stops the walk" not in prompt.lower()
           for prompt in vm)
heap = bank.questions["HEAP MEMORY"]
assert {r["id"] for r in heap.values()} == {f"HP{i:02}" for i in range(1, 37)}
assert sum(r["subcategory"] == "General" for r in heap.values()) == 24
assert sum(r["subcategory"] == "Bad memory usage code" for r in heap.values()) == 12
assert {r["id"] for p, r in heap.items() if p.startswith("⭐ ")} == {
    f"HP{i:02}" for i in (*range(7, 13), *range(14, 20), *range(25, 37))
}
for prompt, record in heap.items():
    assert any("9.1 (The) Heap.pptx, slides " in s for s in record["sources"])
    if record["subcategory"] == "Bad memory usage code":
        assert prompt.startswith("⭐ ") and "```c" in prompt
        assert any("midterm-2-code-examples.md, entry " in s for s in record["sources"])
        assert any("line 85" in s and "something wrong with every program" in s
                   for s in record["sources"])
compiler = bank.questions["HW3 [Compiler]"]
assert {r["id"] for r in compiler.values()} == {"CP01", "CP02", "CP03", "CP04", "CP09"}
assert {r["id"] for q, r in compiler.items() if q.startswith("⭐ ")} == {
    "CP01", "CP02", "CP03", "CP04", "CP09"
}
for prompt, record in compiler.items():
    assert "```" not in prompt
    if prompt.startswith("⭐ "):
        assert any("new_new_transcript" in s and "line 65" in s for s in record["sources"])
# Retain stable IDs after consolidation; gaps are intentional.
assert {r["id"] for r in bank.questions["PROCESSES"].values()} == {
    f"PC{i:02}" for i in (1,3,4,6,7,8,9,10,11,12,13,14,16,17,18,20,22,25,26,27,
                          31,32,33,34,35,36,37,38,39,40,41)
}
for ident, (prompt, record) in records.items():
    assert prompt.strip() and record["answer"].strip() and record["subcategory"]
    assert record["explanation"].strip(), ident
    assert record["sources"] and all(
        s.startswith("https://") or any(
            (base / s.split(", ", 1)[0]).is_file()
            for base in (ROOT / "midterm-2", ROOT / "cse320/midterm-2")
        )
        for s in record["sources"]
    ), ident
    assert prompt.count("```") % 2 == 0, ident
    if prompt.startswith("⭐ "):
        assert any(("Nov 5 mt2 review" in s and "line 85" in s) or
                   ("new_new_transcript" in s and "line 65" in s) or
                   (ident in {"SG16", "SG26"} and "new_transcripts/nov17 " in s
                    and ("line 87" in s or "lines 9-11" in s))
                   for s in record["sources"]), ident
    if ident.startswith("PC"):
        assert record["explanation"].strip(), ident
        assert any("8. Processes.pptx, slides " in s for s in record["sources"]), ident
        if "```" in prompt:
            assert any("midterm-2-code-examples.md" in s for s in record["sources"]), ident

# Reject literal duplicate question keys before Python can silently discard them.
tree = ast.parse((ROOT / "question_banks/CSE320_MT2.py").read_text(encoding="utf-8"))
prompts = [n.args[2].value for n in ast.walk(tree)
           if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
           and n.func.id in {"_pc", "_pc_code", "_sg", "_shell", "_compiler", "_heap", "_vm"}
           and isinstance(n.args[2], ast.Constant)]
assert len(prompts) == len(set(prompts))

def answer_has(ident, *values):
    answer = records[ident][1]["answer"]
    assert all(value in answer for value in values), (ident, values, answer)

# Enumerate observable fork2 sequences without assuming a preferred schedule.
# One L0 precedes two branches, each of which prints L1 before its two Bye's.
events = ("L0", "A1", "B1", "Abye1", "Abye2", "Bbye1", "Bbye2")
edges = [("L0", "A1"), ("L0", "B1")]
edges += [(branch + "1", branch + "bye" + suffix)
          for branch in "AB" for suffix in "12"]
outputs = set()
for order in itertools.permutations(events):
    pos = {event: i for i, event in enumerate(order)}
    if all(pos[a] < pos[b] for a, b in edges):
        outputs.add(tuple("L0" if e == "L0" else "L1" if e in {"A1", "B1"} else "Bye"
                          for e in order))
assert ("L0", "L1", "Bye", "Bye", "L1", "Bye", "Bye") in outputs
assert ("L0", "L1", "Bye", "Bye", "Bye", "L1", "Bye") not in outputs
assert ("L0", "L1", "L1", "Bye", "Bye", "Bye", "Bye") in outputs
answer_has("PC32", "A and C are possible", "B is impossible")

wait_orders = [p for p in itertools.permutations(("HC", "HP", "CT", "Bye"))
               if p.index("HC") < p.index("CT")
               and p.index("HP") < p.index("CT") < p.index("Bye")]
assert set(wait_orders) == {("HC", "HP", "CT", "Bye"), ("HP", "HC", "CT", "Bye")}
answer_has("PC34", "HC, HP, CT, Bye", "HP, HC, CT, Bye")
answer_has("PC06", "run another process while one waits for I/O")
assert 2**3 == 8
answer_has("PC39", "8 total processes")
answer_has("PC41", "HP, CT, Bye, HC", "wait(&child_status)")

assert {r["id"] for r in bank.questions["SIGNALS"].values()} == {
    f"SG{i:02}" for i in range(1, 34)
    if i not in {1, 3, 4, 7, 8, 9, 10, 11, 15, 17, 22, 24, 28, 29, 30}
}
signals = bank.questions["SIGNALS"]
assert all(not any(term in (q + r["answer"] + r["explanation"]).lower()
                   for term in ("setjmp", "longjmp", "nonlocal jump"))
           for q, r in signals.items())
assert sum(r["subcategory"] == "General" for r in signals.values()) == 7
assert sum("```c" in q for q in signals) == 11
for prompt, record in signals.items():
    assert record["explanation"].strip(), record["id"]
    assert any("8.1 Signals.pptx, slides " in s for s in record["sources"])
    if "```c" in prompt:
        assert any("midterm-2-code-examples.md" in s for s in record["sources"])
for ident, quote in {
    "SG02": "generic signal theory stuff",
    "SG18": "Tell me what I'm doing wrong",
    "SG23": "Tell me what I'm doing wrong",
    "SG25": "Tell me what I'm doing wrong",
    "SG20": "does it leave zombies behind?",
    "SG21": "Tell me what you expect to happen",
    "SG27": "Tell me what you expect to happen",
}.items():
    prompt, record = records[ident]
    assert prompt.startswith("⭐ "), ident
    assert any(quote in s and "line 85" in s for s in record["sources"]), ident
assert not records["SG19"][0].startswith("⭐ ")
assert not any("Nov 5 mt2 review" in source for source in records["SG19"][1]["sources"])
assert {r["id"] for q, r in bank.questions["HW5 [Shell]"].items()
        if q.startswith("\u2b50 ")} == {
    "SH01", "SH03", "SH06", "SH07", "SH09", "SH15", "SH17"
}
assert {r["id"] for r in bank.questions["HW5 [Shell]"].values()} == {
    f"SH{i:02}" for i in range(1, 23)
}
print("PASS: 137 custom questions across Processes, Signals, Virtual Memory, Shell, Compiler, and Heap; unique IDs, sources, explanations, image attachments, required stars, and process ordering/counts.")

# Review deck: 54 numbered questions, including multipart prompts and answers.
assert {topic: len(entries) for topic, entries in review_topics.items()} == {
    "processes review session": 6,
    "signals review session": 5,
    "virtual memory review session": 10,
    "heap memory review session": 8,
    "general concepts review session": 10,
    "HW3 [Compiler] review session": 5,
    "HW4 [Pages] review session": 5,
    "HW5 [Shell] review session": 5,
}
review = {r["review_question"]: (q, r)
          for entries in review_topics.values() for q, r in entries.items()}
assert set(review) == set(range(1, 55))
assert {r["id"] for q, r in review.values()} == {f"RS{i:02}" for i in range(1, 55)}
assert not ({r["id"] for q, r in review.values()} & records.keys())
for number, (prompt, record) in review.items():
    assert prompt.startswith(record["subcategory"] + "\n\n")
    assert all(f"\n{letter}. " in prompt for letter in "ABC")
    assert record["answer"][0] in "ABC" and record["answer"][1:3] == ". "
    assert record["question_slides"] and record["answer_slides"]
    assert prompt.count("```") % 2 == 0
    assert record.get("explanation", "").count("```") % 2 == 0
for number in range(12, 22):
    prompt = review[number][0]
    assert "Table Index" in prompt and "Table Contents" in prompt and "Present" in prompt
    assert prompt.count("```text") == (1 if number in (12, 13, 17, 20) else 5)

# When local course sources are present, independently check every numbered
# question/answer slide against the imported text and verify all table cells.
deck = ROOT / "cse320/midterm-2/CSE 320 MT2 Review Session.pptx"
if deck.is_file():
    import re
    import zipfile
    import xml.etree.ElementTree as ET
    ns = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main",
          "p": "http://schemas.openxmlformats.org/presentationml/2006/main"}
    compact = lambda s: "".join(s.split())
    source_slides = set()
    with zipfile.ZipFile(deck) as archive:
        for name in archive.namelist():
            match = re.fullmatch(r"ppt/slides/slide(\d+)\.xml", name)
            if not match:
                continue
            slide = int(match[1])
            root = ET.fromstring(archive.read(name))
            shapes = root.findall(".//p:sp", ns)
            texts = ["\n".join("".join(t.text or "" for t in p.findall(".//a:t", ns))
                               for p in shape.findall(".//a:p", ns)).strip()
                     for shape in shapes]
            heading = re.match(r"(Question|Answer) (\d+)", texts[0])
            if not heading:
                continue
            source_slides.add(slide)
            kind, number = heading[1], int(heading[2])
            prompt, record = review[number]
            target = prompt if kind == "Question" else record.get("explanation", "")
            assert slide in record["question_slides" if kind == "Question" else "answer_slides"]
            if kind == "Answer":
                assert record["answer"].startswith(re.search(r"Correct: ([ABC])", texts[0])[1] + ". ")
            if number == 10:
                # User-approved scope adaptation supplies the loop semantics and
                # replaces the detailed API explanation. Keep checking the deck
                # answer key and slide inventory; exact text fidelity is no
                # longer expected for this item's adapted answer slides.
                assert record.get("code_modification")
                if kind == "Answer":
                    continue
                target = re.sub(r"/\* Reap one available.*?\*/", "", target, flags=re.S)
            for text in texts[1:]:
                if text.startswith("Bottom tables 0"):
                    continue  # A slide-navigation cue, replaced by embedded tables.
                assert compact(text) in compact(target), (number, slide, text)
            for table in root.findall(".//a:tbl", ns):
                cells = ["".join(t.text or "" for t in c.findall(".//a:t", ns))
                         for c in table.findall(".//a:tc", ns)]
                assert compact("".join(cells)) in compact(target), (number, slide, "table")
    imported_slides = [s for q, r in review.values()
                       for s in r["question_slides"] + r["answer_slides"]]
    assert len(imported_slides) == len(set(imported_slides)) == 213
    assert set(imported_slides) == source_slides
print("PASS: all 54 review-session questions in 8 topic buckets; choices, answer keys, multipart coverage, code, and page tables.")
