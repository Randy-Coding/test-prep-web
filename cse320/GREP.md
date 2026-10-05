# Needle in a Haystack — CSE 320

## Overview

After the starship *Needle* vanished, investigators recovered a log archive under `logs/voyage/`. Eight verification codes are hidden inside. Your job is to find them using **`head`**, **`tail`**, **`grep`**, and **`wc`** from the command line.

The dataset has four parts:

| Location | What's there |
|----------|----------------|
| `voyage_master.log` | One very large ship-wide log file |
| `treasure_flood/` | Many small logs spread across nested folders |
| `treasure_count/` | Another tree of small logs |
| `haystack/` | A third tree of subsystem logs, plus a few notable files at the top level |

---

## Provided files

| Path | Description |
|------|-------------|
| `README.md` | This document |
| `logs/voyage/` | Your personalized log archive (see table above) |

You do **not** need to modify these files for credit. Work from the `logs/voyage/` directory (or use paths relative to it).

---

## Where the treasures are

Each treasure is a **32-bit hex value** (written like `0x........`). The hints below describe *where to look*, not the exact command to run.

**Treasure 01** — Open the voyage master log and look at the **very beginning**. A briefing line near the top contains a `treasure_verify=` token.

**Treasure 02** — In the **same** voyage master log, look at the **very end**. A sign-off line near the bottom contains another `treasure_verify=` token.

**Treasure 03** — Somewhere under `treasure_flood/`, almost every log line looks the same — except **one** line that marks the real prize. Search the whole tree until you find the odd one out.

**Treasure 04** — Under `treasure_count/`, the verification code is the **total number of times** the word treasure appears across **all** files in that tree. You will need to search the entire directory and count carefully.

**Treasure 05** — Back in `voyage_master.log`, a single special line is buried **deep in the middle** of the file (not at the head or tail). The **line number** where that line appears *is* the treasure value (convert the decimal line number to hex).

**Treasure 06** — One log file somewhere under `haystack/` contains a unique buried marker. You will need to search recursively through the haystack.

**Treasure 07** — The haystack holds a **chain of three clues** each in the first line of the indicated file. Start from a map file sitting at the **top level** of `haystack/`, read what it points to, then follow each hop until you reach the final prize value.

**Treasure 08** — Still in `haystack/`, hex digits are **woven into the letters** of the word `TREASURE` (one digit after each letter, including after the final E). Find that pattern and read off the digits.

---

## Command-line toolkit

These commands are generally useful for exploring the dataset. They are **not** the full recipe for any one treasure — you still need to decide *what* to search for and *where*.

### `head` — start of a file

```bash
head voyage_master.log              # first 10 lines (default)
head -n 3 voyage_master.log         # first 3 lines
head -n 1 haystack/README.txt       # just the first line
```

### `tail` — end of a file

```bash
tail voyage_master.log              # last 10 lines (default)
tail -n 5 voyage_master.log         # last 5 lines
tail -n 1 haystack/treasure_map.log # last line only
```

### `grep` — search for text

```bash
grep treasure voyage_master.log           # lines containing "treasure"
grep -i error haystack/comms/relay/alpha/hop01.log   # case-insensitive
grep -n prize voyage_master.log         # show line numbers
grep -c treasure treasure_count/README.txt   # count matching lines in one file
grep -r treasure haystack/              # search all files under a directory
grep -r --include='*.log' cargo haystack/    # only .log files
grep -o '0x[0-9a-f]\+' voyage_master.log     # print only the matching part
grep -oh treasure treasure_count/ | head    # one match per line, first few hits
grep -E 'value:0x[0-9a-f]+' haystack/nav/charts/chart01/fix.log   # extended regex
grep -v treasure treasure_flood/captain/shard00/log_001.log  # lines that do NOT match
```

### `wc` — count lines, words, bytes

```bash
wc -l voyage_master.log             # number of lines in a file
wc -l haystack/galley/shifts/shift01/inventory.log
grep -r treasure treasure_count/ | wc -l    # count lines returned by grep
grep -roh treasure treasure_count/ | wc -l  # count individual word matches (whole word)
```

### Combining tools

```bash
grep treasure voyage_master.log | head -5     # first 5 matching lines
grep -r WARN haystack/ | wc -l               # how many lines contain "WARN"
tail -n 20 voyage_master.log | grep verify  # search only the last 20 lines
```

### Other helpers (optional)

```bash
find haystack -name '*.log' | head          # list log file paths
find haystack -type f | wc -l              # how many files in the haystack
cat haystack/README.txt                     # print a whole small file
less voyage_master.log                      # scroll through a large file (q to quit)
```

---

## Academic integrity

You may discuss command-line techniques and general strategies with classmates. **Your submitted treasure values must be your own** — do not share completed answer lists or copy another student’s results.
