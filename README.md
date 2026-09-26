# Test Prep Web

A local web version of the question-bank exam. Choose a course and chapters/topics, optionally split randomized exam questions into chunks, reveal answers, self-grade, and retry missed questions. Flashcard mode lets you flip through cards from selected chapters and reshuffle the deck.

## Run

Requires Python 3. No packages to install.

```sh
python server.py
```

Open <http://localhost:8000>. Use `python server.py --port 8080` to choose another port.

## Question banks

The Python files in `question_banks/` each define a `questions` dictionary. Values can be topic dictionaries of question/answer pairs, or direct question/answer pairs for a single-topic bank. Restart the server to pick up changes to the files.

The server binds to localhost. Session progress, selected chapters, scores, and the current flashcard are saved automatically in the browser's local storage. Reloading the page resumes the current session. Storage is local to this browser and origin; clearing site data removes it.
