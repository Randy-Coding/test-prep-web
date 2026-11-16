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
records = {a["id"]: (q, a) for entries in bank.questions.values() for q, a in entries.items()}
assert len(records) == sum(map(len, bank.questions.values())) == 57
assert {topic: len(entries) for topic, entries in bank.questions.items()} == {
    "PROCESSES CUSTOM": 31,
    "SIGNALS": 26,
}
# Retain stable IDs after consolidation; gaps are intentional.
assert {r["id"] for r in bank.questions["PROCESSES CUSTOM"].values()} == {
    f"PC{i:02}" for i in (1,3,4,6,7,8,9,10,11,12,13,14,16,17,18,20,22,25,26,27,
                          31,32,33,34,35,36,37,38,39,40,41)
}
for ident, (prompt, record) in records.items():
    assert prompt.strip() and record["answer"].strip() and record["subcategory"]
    assert record["sources"] and all(
        s.startswith("https://") or (ROOT / "cse320/midterm-2" / s.split(", ", 1)[0]).is_file()
        for s in record["sources"]
    ), ident
    assert prompt.count("```") % 2 == 0, ident
    if prompt.startswith("⭐ "):
        assert any("Nov 5 mt2 review" in s and "line 85" in s
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
           and n.func.id in {"_pc", "_pc_code", "_sg"}
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
answer_has("PC06", "Increasing n increases modeled utilization")
assert 2**3 == 8
answer_has("PC39", "8 total processes")
answer_has("PC41", "HP, CT, Bye, HC", "wait(&child_status)")

assert {r["id"] for r in bank.questions["SIGNALS"].values()} == {
    f"SG{i:02}" for i in range(1, 31) if i not in {17, 22, 24, 28}
}
signals = bank.questions["SIGNALS"]
assert sum(r["subcategory"] == "General" for r in signals.values()) == 16
assert sum("```c" in q for q in signals) == 10
for prompt, record in signals.items():
    assert record["explanation"].strip(), record["id"]
    assert any("8.1 Signals.pptx, slides " in s for s in record["sources"])
    if "```c" in prompt:
        assert any("midterm-2-code-examples.md" in s for s in record["sources"])
for ident, quote in {
    "SG01": "Tell me what I'm doing wrong",
    "SG02": "generic signal theory stuff",
    "SG19": "Tell me what you expect to happen",
    "SG20": "does it leave zombies behind?",
}.items():
    prompt, record = records[ident]
    assert prompt.startswith("⭐ "), ident
    assert any(quote in s and "line 85" in s for s in record["sources"]), ident
signal_prompt, signal_record = records["SG01"]
assert signal_prompt.startswith("⭐ ")
assert "sigprocmask(SIG_BLOCK, &mask, &prev);" in signal_prompt
assert "SIG_SETMASK" in signal_record["answer"]
assert "sigsuspend(&mask)" in signal_record["answer"]
assert signal_record["explanation"].strip()
assert any("entries 34-36" in source for source in signal_record["sources"])
print("PASS: 31 PROCESSES CUSTOM and 26 SIGNALS; unique IDs, sources, explanations, code references, four starred Signals forms; process ordering and counts.")
