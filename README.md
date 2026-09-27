# Test Prep Web

A local web version of the question-bank exam. Choose a course and chapters/topics, optionally split randomized exam questions into chunks, reveal answers, self-grade, and retry missed questions. Flashcard mode lets you flip through cards from selected chapters and reshuffle the deck.

## Run

Requires Python 3. No packages to install.

```sh
python server.py
```

Open <http://localhost:8000>. Use `python server.py --port 8080` to choose another port.

## Deploy to Vercel

Push this repository to GitHub, then import it as a new Vercel project. The included `vercel.json` selects the **Other** framework, runs `python3 build_static.py`, and publishes `dist/`. No environment variables are needed. Each deployment rebuilds `banks.json` from the Python question banks.

You can check the output locally with `python build_static.py`, then `python -m http.server 8000 --directory dist`.

## Question banks

The Python files in `question_banks/` each define a `questions` dictionary. Values can be topic dictionaries of question/answer pairs, or direct question/answer pairs for a single-topic bank. A question can also have a record with `choices` (A-D), `correct_answer`, `explanation`, and an optional repository-relative `image` path such as `cse320/Cache Diagram.png`. These records show the choices and diagram in exams, flashcards, and missed-question review. The local server serves referenced images under `/assets/cse320/`; the static build copies them there. Restart the server to pick up changes to the files.

The server binds to localhost. Session progress, selected chapters, scores, and the current flashcard are saved automatically in the browser's local storage. Reloading the page resumes the current session. Storage is local to this browser and origin; clearing site data removes it.
