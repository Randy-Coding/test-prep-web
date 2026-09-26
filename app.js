const $ = (id) => document.getElementById(id);
let banks = {};
let pool = [];
let session = [];
let missed = [];
let position = 0;
let score = 0;

function shuffle(items) {
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

function checked(container) {
  return [...$(container).querySelectorAll('input:checked')].map((input) => input.value);
}

function show(view) {
  for (const id of ['setup', 'exam', 'results']) $(id).hidden = id !== view;
  window.scrollTo(0, 0);
}

function renderTopics() {
  const topics = banks[$('bank').value] || {};
  $('topics').replaceChildren();
  Object.entries(topics).forEach(([name, entries]) => {
    const label = document.createElement('label');
    label.className = 'topic';
    const input = document.createElement('input');
    input.type = 'checkbox';
    input.value = name;
    input.checked = true;
    label.append(input, document.createTextNode(`${name} (${entries.length})`));
    $('topics').append(label);
  });
  updatePool();
}

function updatePool() {
  const topics = banks[$('bank').value] || {};
  pool = checked('topics').flatMap((name) => topics[name] || []);
  $('question-count').textContent = `${pool.length} question${pool.length === 1 ? '' : 's'} selected`;
  const size = Number($('chunk-size').value);
  const chunked = $('chunk-size').value !== '' && Number.isInteger(size) && size > 0;
  $('chunks-wrap').hidden = !chunked || pool.length === 0;
  $('chunks').replaceChildren();
  if (chunked) {
    const count = Math.ceil(pool.length / size);
    for (let i = 0; i < count; i++) {
      const label = document.createElement('label');
      label.className = 'topic';
      const input = document.createElement('input');
      input.type = 'checkbox';
      input.value = String(i);
      input.checked = true;
      label.append(input, document.createTextNode(`Chunk ${i + 1} (${Math.min(size, pool.length - i * size)})`));
      $('chunks').append(label);
    }
  }
}

function renderQuestion() {
  $('progress').textContent = `Question ${position + 1} of ${session.length}`;
  $('score').textContent = `Score ${score}/${position}`;
  $('progress-fill').style.width = `${position / session.length * 100}%`;
  $('question').textContent = session[position].question;
  $('answer').textContent = session[position].answer;
  $('answer-panel').hidden = true;
  $('reveal').hidden = false;
}

function begin(items) {
  session = shuffle(items);
  missed = [];
  position = 0;
  score = 0;
  show('exam');
  renderQuestion();
}

function finish() {
  show('results');
  $('result-title').textContent = missed.length ? 'Keep going.' : 'You did it!';
  $('result-score').textContent = `Final score: ${score}/${session.length} (${Math.round(score / session.length * 100)}%)`;
  $('retry').hidden = missed.length === 0;
  $('missed').replaceChildren();
  if (missed.length) {
    const heading = document.createElement('h3');
    heading.textContent = `Questions you missed (${missed.length})`;
    $('missed').append(heading);
    missed.forEach((item) => {
      const row = document.createElement('div');
      row.className = 'missed-item';
      const q = document.createElement('strong');
      q.textContent = item.question;
      const a = document.createElement('span');
      a.textContent = item.answer;
      row.append(q, a);
      $('missed').append(row);
    });
  }
}

function grade(correct) {
  if (correct) score++;
  else missed.push(session[position]);
  position++;
  if (position === session.length) finish();
  else renderQuestion();
}

$('bank').addEventListener('change', renderTopics);
$('topics').addEventListener('change', updatePool);
$('chunk-size').addEventListener('input', updatePool);
$('toggle-topics').addEventListener('click', () => {
  const inputs = [...$('topics').querySelectorAll('input')];
  const next = !inputs.every((input) => input.checked);
  inputs.forEach((input) => { input.checked = next; });
  updatePool();
});
$('start').addEventListener('click', () => {
  $('setup-error').textContent = '';
  if (!pool.length) {
    $('setup-error').textContent = 'Select at least one topic with questions.';
    return;
  }
  const rawSize = $('chunk-size').value;
  let items = shuffle(pool);
  if (rawSize !== '') {
    const size = Number(rawSize);
    if (!Number.isInteger(size) || size < 1) {
      $('setup-error').textContent = 'Chunk size must be a positive whole number.';
      return;
    }
    const chunks = Array.from({ length: Math.ceil(items.length / size) }, (_, i) => items.slice(i * size, (i + 1) * size));
    items = checked('chunks').flatMap((index) => chunks[Number(index)] || []);
    if (!items.length) {
      $('setup-error').textContent = 'Select at least one chunk.';
      return;
    }
  }
  begin(items);
});
$('reveal').addEventListener('click', () => {
  $('reveal').hidden = true;
  $('answer-panel').hidden = false;
});
$('correct').addEventListener('click', () => grade(true));
$('incorrect').addEventListener('click', () => grade(false));
$('retry').addEventListener('click', () => begin(missed));
$('restart').addEventListener('click', () => show('setup'));

fetch('/api/banks').then((response) => {
  if (!response.ok) throw new Error('Could not load question banks.');
  return response.json();
}).then((data) => {
  banks = data;
  Object.keys(banks).forEach((name) => {
    const option = document.createElement('option');
    option.value = name;
    option.textContent = name;
    $('bank').append(option);
  });
  if (banks.CSE416) $('bank').value = 'CSE416';
  renderTopics();
}).catch((error) => { $('setup-error').textContent = error.message; });
