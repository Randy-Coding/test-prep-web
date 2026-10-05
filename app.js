const $ = (id) => document.getElementById(id);
let banks = {};
let pool = [];
let session = [];
let missed = [];
let position = 0;
let score = 0;
let grades = [];
let revealedQuestions = [];
let mode = 'exam';
let view = 'setup';
let revealed = false;
let flipped = false;
let snapshots = { exam: null, flashcards: null };
const STORAGE_KEY = 'test-prep-web-state-v1';

function save() {
  if ((view === 'exam' || view === 'results') && session.length) {
    snapshots.exam = { view, session, missed, position, score, grades, revealedQuestions, revealed };
  } else if (view === 'flashcards' && session.length) {
    snapshots.flashcards = { view, session, position, flipped };
  }
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      mode, view, session, missed, position, score, grades, revealedQuestions, revealed, flipped,
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

function restoreGrades(state) {
  if (Array.isArray(state.grades) && state.grades.length === session.length) {
    return state.grades.map((grade) => grade === true ? true : grade === false ? false : null);
  }
  const restored = Array(session.length).fill(null);
  const previouslyMissed = new Set((state.missed || []).map((item) => item.question));
  const completedCount = Math.min(Number.isInteger(state.position) ? state.position : 0, session.length);
  for (let index = 0; index < completedCount; index++) {
    restored[index] = !previouslyMissed.has(session[index].question);
  }
  return restored;
}

function restoreRevealedQuestions(state) {
  let restored;
  if (Array.isArray(state.revealedQuestions) && state.revealedQuestions.length === session.length) {
    restored = state.revealedQuestions.map((wasRevealed, index) => {
      const legacyInconclusive = Array.isArray(state.completed)
        && state.completed[index]
        && Array.isArray(state.grades)
        && state.grades[index] === null;
      return Boolean(wasRevealed) && !legacyInconclusive;
    });
  } else {
    restored = grades.map((grade) => grade !== null);
  }
  if (state.revealed && state.position >= 0 && state.position < restored.length) {
    restored[state.position] = true;
  }
  return restored;
}

function updateGradeSummary() {
  score = grades.filter((grade) => grade === true).length;
  missed = session.filter((_, index) => grades[index] === false);
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
    grades = restoreGrades(state);
    revealedQuestions = restoreRevealedQuestions(state);
    updateGradeSummary();
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

function renderImage(item, image) {
  image.hidden = !item.image;
  if (item.image) image.src = item.image;
  else image.removeAttribute('src');
}

function renderImageLink(item, link) {
  link.hidden = !item.image;
  if (item.image) link.href = item.image;
  else link.removeAttribute('href');
}

function formatCodeBlock(source) {
  let input = String(source).trim();
  if (input.includes('\n')) return input;
  const nestedLoops = input.match(/^for\s*(\([^)]*\))\s*for\s*(\([^)]*\))\s*(.+;)$/);
  if (nestedLoops) {
    return [
      `for ${nestedLoops[1]} {`,
      `    for ${nestedLoops[2]} {`,
      `        ${nestedLoops[3].trim()}`,
      '    }',
      '}',
    ].join('\n');
  }
  const singleLoop = input.match(/^for\s*(\([^)]*\))\s*(.+;)$/);
  if (singleLoop) {
    return [
      `for ${singleLoop[1]} {`,
      `    ${singleLoop[2].trim()}`,
      '}',
    ].join('\n');
  }
  input = input.replace(/for\s*(\([^)]*\))\s*(?!\{)([^{};]+;)/g, 'for $1 { $2 }');
  let output = '';
  let indent = 0;
  let parenDepth = 0;
  let quote = '';
  const padding = () => '    '.repeat(indent);
  const newline = () => {
    output = output.trimEnd();
    if (!output.endsWith('\n')) output += '\n';
    output += padding();
  };
  for (let index = 0; index < input.length; index++) {
    const char = input[index];
    const next = input[index + 1] || '';
    if (quote) {
      output += char;
      if (char === quote && input[index - 1] !== '\\') quote = '';
      continue;
    }
    if (char === '"' || char === "'") {
      quote = char;
      output += char;
    } else if (char === '(') {
      parenDepth++;
      output += char;
    } else if (char === ')') {
      parenDepth--;
      output += char;
      const rest = input.slice(index + 1);
      const line = output.slice(output.lastIndexOf('\n') + 1).trimStart();
      if (parenDepth === 0 && /^(for|if|while)\b/.test(line) && !/^\s*\{/.test(rest)) {
        indent++;
        newline();
      }
    } else if (char === '{') {
      output = output.trimEnd() + ' {';
      indent++;
      newline();
    } else if (char === '}') {
      indent = Math.max(0, indent - 1);
      output = output.trimEnd();
      if (!output.endsWith('\n')) output += '\n';
      output += padding() + '}';
      if (next && next !== ';') newline();
    } else if (char === ';') {
      output += char;
      if (parenDepth === 0 && next) newline();
    } else if (/\s/.test(char)) {
      if (output && !/[\s\n]$/.test(output)) output += ' ';
    } else {
      output += char;
    }
  }
  return output.trim();
}

function renderFormatted(text, container) {
  container.replaceChildren();
  const source = String(text ?? '');
  const fenced = source.split(/```(?:[a-zA-Z0-9_+-]+)?\n?([\s\S]*?)```/g);
  fenced.forEach((part, index) => {
    if (index % 2 === 1) {
      const pre = document.createElement('span');
      pre.className = 'code-block';
      const code = document.createElement('code');
      code.textContent = formatCodeBlock(part.replace(/^\n|\n$/g, ''));
      pre.append(code);
      container.append(pre);
      return;
    }
    let afterBlock = false;
    part.split(/(`[^`]+`)/g).forEach((piece) => {
      if (piece.startsWith('`') && piece.endsWith('`')) {
        const value = piece.slice(1, -1);
        const isBlock = value.includes('\n') || value.includes(';') || value.includes('{') || value.length > 60;
        if (isBlock) {
          const pre = document.createElement('span');
          pre.className = 'code-block';
          const code = document.createElement('code');
          code.textContent = formatCodeBlock(value);
          pre.append(code);
          container.append(pre);
          afterBlock = true;
        } else {
          const code = document.createElement('code');
          code.className = 'inline-code';
          code.textContent = value;
          container.append(code);
          afterBlock = false;
        }
      } else if (piece) {
        let prose = piece;
        if (afterBlock) prose = prose.replace(/^\s*[,.:;]\s*/, '\n\n');
        const cue = prose.trim();
        if (/^(In|For)$/.test(cue)) prose = 'Consider this code:\n\n';
        else if (cue === 'Given') prose = 'Given this code:\n\n';
        else if (cue === 'After') prose = 'After executing:\n\n';
        else if (cue === 'Compare') prose = 'Compare these snippets:\n\n';
        container.append(document.createTextNode(prose));
        afterBlock = false;
      }
    });
  });
}

function renderChoices(item, container, showCorrect = false) {
  container.replaceChildren();
  container.hidden = !item.choices;
  if (!item.choices) return;
  for (const letter of ['A', 'B', 'C', 'D']) {
    const choice = document.createElement('div');
    choice.className = 'choice';
    if (showCorrect && letter === item.correct_answer) choice.classList.add('correct-choice');
    const label = document.createElement('strong');
    label.textContent = `${letter}.`;
    const content = document.createElement('div');
    content.className = 'choice-content';
    renderFormatted(item.choices[letter], content);
    choice.append(label, content);
    container.append(choice);
  }
}

function renderQuestion() {
  const item = session[position];
  const graded = grades.filter((grade) => grade !== null).length;
  $('progress').textContent = `Question ${position + 1} of ${session.length}`;
  $('score').textContent = `Score ${score}/${graded}`;
  $('progress-fill').style.width = `${(position + 1) / session.length * 100}%`;
  renderFormatted(item.question, $('question'));
  renderImage(item, $('question-image'));
  renderImageLink(item, $('question-image-link'));
  renderChoices(item, $('choices'), revealed);
  renderFormatted(item.answer, $('answer'));
  $('answer-panel').hidden = !revealed;
  $('reveal').hidden = revealed;
}

function begin(items) {
  session = shuffle(items);
  missed = [];
  position = 0;
  score = 0;
  grades = Array(session.length).fill(null);
  revealedQuestions = Array(session.length).fill(false);
  revealed = false;
  show('exam');
  renderQuestion();
  save();
}

function renderCard() {
  const card = session[position];
  $('card-progress').textContent = `Card ${position + 1} of ${session.length}`;
  renderFormatted(card.question, $('card-question'));
  renderImage(card, $('card-image'));
  renderImageLink(card, $('card-image-link'));
  renderChoices(card, $('card-choices'));
  renderFormatted(card.answer, $('card-answer'));
  renderImage(card, $('card-answer-image'));
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

function revealExamAnswer() {
  if (revealed) return;
  revealed = true;
  revealedQuestions[position] = true;
  renderQuestion();
  save();
}

function moveCard(step) {
  const next = position + step;
  if (next < 0 || next >= session.length) return;
  position = next;
  flipped = false;
  renderCard();
  save();
}

function moveExam(step) {
  if (step > 0 && revealed && grades[position] === null) {
    grades[position] = false;
    updateGradeSummary();
    if (grades.every((grade) => grade !== null)) {
      finish();
      save();
      return;
    }
  }

  const next = position + step;
  if (next < 0 || next >= session.length) {
    save();
    return;
  }
  position = next;
  revealed = revealedQuestions[position];
  renderQuestion();
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
  updateGradeSummary();
  const graded = grades.filter((grade) => grade !== null).length;
  const reviewItems = session.filter((_, index) => grades[index] === false);
  show('results');
  $('result-title').textContent = reviewItems.length ? 'Keep going.' : 'You did it!';
  $('result-score').textContent = graded
    ? `Final score: ${score}/${graded} (${Math.round(score / graded * 100)}%)`
    : 'No questions were graded.';
  $('retry').hidden = reviewItems.length === 0;
  $('retry').onclick = () => begin(reviewItems);
  $('missed').replaceChildren();
  if (reviewItems.length) {
    const heading = document.createElement('h3');
    heading.textContent = `Questions you missed (${reviewItems.length})`;
    $('missed').append(heading);
    reviewItems.forEach((item) => {
      const row = document.createElement('div');
      row.className = 'missed-item';
      const q = document.createElement('div');
      q.className = 'missed-question';
      renderFormatted(item.question, q);
      const a = document.createElement('div');
      a.className = 'missed-answer';
      renderFormatted(item.answer, a);
      row.append(q);
      if (item.image) {
        const link = document.createElement('a');
        link.className = 'diagram-link';
        link.target = '_blank';
        link.rel = 'noopener';
        renderImageLink(item, link);
        const image = document.createElement('img');
        image.className = 'question-image';
        image.alt = 'Diagram for this question';
        renderImage(item, image);
        link.append(image, document.createTextNode('Open diagram full size'));
        row.append(link);
      }
      if (item.choices) {
        const choices = document.createElement('div');
        choices.className = 'choices';
        renderChoices(item, choices, true);
        row.append(choices);
      }
      row.append(a);
      $('missed').append(row);
    });
  }
}

function grade(correct) {
  grades[position] = correct;
  revealedQuestions[position] = true;
  updateGradeSummary();
  revealed = false;
  if (grades.every((grade) => grade !== null)) {
    finish();
  } else {
    let next = position;
    do { next = (next + 1) % session.length; }
    while (grades[next] !== null);
    position = next;
    revealed = revealedQuestions[position];
    renderQuestion();
  }
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
$('reveal').addEventListener('click', revealExamAnswer);
$('correct').addEventListener('click', () => grade(true));
$('incorrect').addEventListener('click', () => grade(false));
$('restart').addEventListener('click', () => show('setup'));
$('back-setup').addEventListener('click', () => show('setup'));
$('flash-card').addEventListener('click', flipCard);
$('previous-card').addEventListener('click', () => moveCard(-1));
$('next-card').addEventListener('click', () => moveCard(1));
$('shuffle-cards').addEventListener('click', () => { session = shuffle(session); position = 0; flipped = false; renderCard(); save(); });

document.addEventListener('keydown', (event) => {
  if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
  const target = event.target;
  if (target instanceof Element && target.closest('input, select, textarea, [contenteditable="true"]')) return;

  if (event.key === 'Enter' || event.key === ' ') {
    if (target instanceof Element && target.closest('button, a')) return;
    if (view === 'exam') {
      event.preventDefault();
      if (revealed) grade(true);
      else revealExamAnswer();
    } else if (view === 'flashcards' && !flipped) {
      event.preventDefault();
      flipped = true;
      renderCard();
      save();
    }
    return;
  }

  if (event.key === 'ArrowLeft') {
    if (view !== 'exam' && view !== 'flashcards') return;
    event.preventDefault();
    if (view === 'exam') moveExam(-1);
    else moveCard(-1);
  } else if (event.key === 'ArrowRight') {
    if (view !== 'exam' && view !== 'flashcards') return;
    event.preventDefault();
    if (view === 'exam') moveExam(1);
    else moveCard(1);
  }
});

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
      grades = restoreGrades(state);
      revealedQuestions = restoreRevealedQuestions(state);
      updateGradeSummary();
      revealed = Boolean(state.revealed);
      flipped = Boolean(state.flipped);
      if (state.view === 'exam' && position < session.length) { show('exam'); renderQuestion(); }
      else if (state.view === 'flashcards' && position < session.length) { show('flashcards'); renderCard(); }
      else if (state.view === 'results') finish();
    }
  }
  save();
}).catch((error) => { $('setup-error').textContent = error.message; });
