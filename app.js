const $ = (id) => document.getElementById(id);
let banks = {};
let pool = [];
let session = [];
let missed = [];
let position = 0;
let score = 0;
let mode = 'exam';
let view = 'setup';
let revealed = false;
let flipped = false;
let snapshots = { exam: null, flashcards: null };
const STORAGE_KEY = 'test-prep-web-state-v1';

function save() {
  if ((view === 'exam' || view === 'results') && session.length) {
    snapshots.exam = { view, session, missed, position, score, revealed };
  } else if (view === 'flashcards' && session.length) {
    snapshots.flashcards = { view, session, position, flipped };
  }
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      mode, view, session, missed, position, score, revealed, flipped,
      snapshots,
      bank: $('bank').value, topics: checked('topics'),
      chunkSize: $('chunk-size').value, chunks: checked('chunks')
    }));
  } catch (_) { /* Browsers with storage disabled can still run the app. */ }
}

function savedState() {
  try { return JSON.parse(localStorage.getItem(STORAGE_KEY)); }
  catch (_) { return null; }
}

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

function show(nextView) {
  view = nextView;
  $('hero').hidden = view !== 'setup';
  for (const id of ['setup', 'exam', 'results', 'flashcards']) $(id).hidden = id !== view;
  updateNav();
  save();
  window.scrollTo(0, 0);
}

function setMode(next) {
  mode = next;
  $('exam-mode').classList.toggle('active', mode === 'exam');
  $('flash-mode').classList.toggle('active', mode === 'flashcards');
  $('chunk-options').hidden = mode === 'flashcards';
  $('start').textContent = mode === 'exam' ? 'Start exam →' : 'Start flashcards →';
  updateNav();
  save();
}

function updateNav() {
  const active = view === 'setup' ? 'home' : view === 'flashcards' ? 'flashcards' : 'exam';
  for (const name of ['home', 'exam', 'flashcards']) {
    const button = $(`nav-${name}`);
    button.classList.toggle('active', name === active);
    if (name === active) button.setAttribute('aria-current', 'page');
    else button.removeAttribute('aria-current');
  }
}

function navigate(target) {
  save();
  show('setup');
  if (target === 'home') return;
  setMode(target);
  const state = snapshots[target];
  if (!state || !Array.isArray(state.session) || !state.session.length) return;
  session = state.session;
  position = state.position;
  if (target === 'flashcards' && position < session.length) {
    flipped = Boolean(state.flipped);
    show('flashcards');
    renderCard();
  } else if (target === 'exam') {
    missed = state.missed || [];
    score = state.score || 0;
    revealed = Boolean(state.revealed);
    if (state.view === 'results') finish();
    else if (position < session.length) { show('exam'); renderQuestion(); }
  }
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
  $('answer-panel').hidden = !revealed;
  $('reveal').hidden = revealed;
}

function begin(items) {
  session = shuffle(items);
  missed = [];
  position = 0;
  score = 0;
  revealed = false;
  show('exam');
  renderQuestion();
  save();
}

function renderCard() {
  const card = session[position];
  $('card-progress').textContent = `Card ${position + 1} of ${session.length}`;
  $('card-question').textContent = card.question;
  $('card-answer').textContent = card.answer;
  $('flash-card').classList.toggle('flipped', flipped);
  $('flash-card').setAttribute('aria-label', flipped ? 'Show question' : 'Show answer');
  $('previous-card').disabled = position === 0;
  $('next-card').disabled = position === session.length - 1;
}

function flipCard() {
  flipped = !flipped;
  renderCard();
  save();
}

function beginCards(items) {
  session = shuffle(items);
  position = 0;
  flipped = false;
  show('flashcards');
  renderCard();
  save();
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
  revealed = false;
  if (position === session.length) finish();
  else renderQuestion();
  save();
}

$('bank').addEventListener('change', () => { renderTopics(); save(); });
$('nav-home').addEventListener('click', () => navigate('home'));
$('nav-exam').addEventListener('click', () => navigate('exam'));
$('nav-flashcards').addEventListener('click', () => navigate('flashcards'));
$('topics').addEventListener('change', () => { updatePool(); save(); });
$('chunk-size').addEventListener('input', () => { updatePool(); save(); });
$('chunks').addEventListener('change', save);
$('exam-mode').addEventListener('click', () => setMode('exam'));
$('flash-mode').addEventListener('click', () => setMode('flashcards'));
$('toggle-topics').addEventListener('click', () => {
  const inputs = [...$('topics').querySelectorAll('input')];
  const next = !inputs.every((input) => input.checked);
  inputs.forEach((input) => { input.checked = next; });
  updatePool();
  save();
});
$('start').addEventListener('click', () => {
  $('setup-error').textContent = '';
  if (!pool.length) {
    $('setup-error').textContent = 'Select at least one topic with questions.';
    return;
  }
  const rawSize = $('chunk-size').value;
  let items = shuffle(pool);
  if (mode === 'exam' && rawSize !== '') {
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
  if (mode === 'exam') begin(items);
  else beginCards(items);
});
$('reveal').addEventListener('click', () => {
  revealed = true;
  $('reveal').hidden = true;
  $('answer-panel').hidden = false;
  save();
});
$('correct').addEventListener('click', () => grade(true));
$('incorrect').addEventListener('click', () => grade(false));
$('retry').addEventListener('click', () => begin(missed));
$('restart').addEventListener('click', () => show('setup'));
$('back-setup').addEventListener('click', () => show('setup'));
$('flash-card').addEventListener('click', flipCard);
$('previous-card').addEventListener('click', () => { if (position > 0) { position--; flipped = false; renderCard(); save(); } });
$('next-card').addEventListener('click', () => { if (position < session.length - 1) { position++; flipped = false; renderCard(); save(); } });
$('shuffle-cards').addEventListener('click', () => { session = shuffle(session); position = 0; flipped = false; renderCard(); save(); });

fetch('/banks.json').then((response) => {
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
  const state = savedState();
  if (state?.bank && banks[state.bank]) $('bank').value = state.bank;
  else if (banks.CSE416) $('bank').value = 'CSE416';
  renderTopics();
  if (state) {
    snapshots = state.snapshots || { exam: null, flashcards: null };
    if (!state.snapshots && Array.isArray(state.session) && state.session.length && state.view !== 'setup') {
      const key = state.view === 'flashcards' ? 'flashcards' : 'exam';
      snapshots[key] = state;
    }
    setMode(state.mode === 'flashcards' ? 'flashcards' : 'exam');
    $('topics').querySelectorAll('input').forEach((input) => { input.checked = state.topics?.includes(input.value) ?? true; });
    $('chunk-size').value = state.chunkSize || '';
    updatePool();
    $('chunks').querySelectorAll('input').forEach((input) => { input.checked = state.chunks?.includes(input.value) ?? true; });
    if (Array.isArray(state.session) && state.session.length && Number.isInteger(state.position) && state.position >= 0 && state.position <= state.session.length) {
      session = state.session;
      missed = Array.isArray(state.missed) ? state.missed : [];
      position = state.position;
      score = Number.isInteger(state.score) ? state.score : 0;
      revealed = Boolean(state.revealed);
      flipped = Boolean(state.flipped);
      if (state.view === 'exam' && position < session.length) { show('exam'); renderQuestion(); }
      else if (state.view === 'flashcards' && position < session.length) { show('flashcards'); renderCard(); }
      else if (state.view === 'results') finish();
    }
  }
  save();
}).catch((error) => { $('setup-error').textContent = error.message; });
