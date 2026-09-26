# Test Prep Web

A local web version of the question-bank exam. Choose a course and topics, optionally split the randomized questions into chunks, reveal answers, self-grade, and retry missed questions.

## Run

Requires Python 3. No packages to install.

```sh
python server.py
```

Open <http://localhost:8000>. Use `python server.py --port 8080` to choose another port.

## Question banks

The Python files in `question_banks/` each define a `questions` dictionary. Values can be topic dictionaries of question/answer pairs, or direct question/answer pairs for a single-topic bank. Restart the server to pick up changes to the files.

The server binds to localhost. Grading and session state live in the browser and are reset when the page is reloaded.
