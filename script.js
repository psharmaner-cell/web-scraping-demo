const messages = document.getElementById('messages');
const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');

let quotes = [];

async function loadQuotes() {
  try {
    const response = await fetch('assets/data/sample-quotes.json');
    if (!response.ok) {
      throw new Error('Could not load quote data');
    }
    quotes = await response.json();
  } catch (error) {
    console.error(error);
    quotes = [];
  }
}

function addMessage(text, role) {
  const message = document.createElement('div');
  message.className = `message ${role}`;
  message.textContent = text;
  messages.appendChild(message);
  messages.scrollTop = messages.scrollHeight;
}

function getBotReply(userText) {
  const text = userText.toLowerCase();

  if (text.includes('scrap') || text.includes('dataset')) {
    return 'This demo uses a static dataset and a JavaScript-powered chatbot UI that works on GitHub Pages.';
  }

  if (text.includes('quote') || text.includes('inspiration')) {
    if (quotes.length > 0) {
      const sample = quotes[0];
      return `Sample quote: “${sample.text}” — ${sample.author}`;
    }
    return 'A sample quote will appear here once the dataset is loaded.';
  }

  if (text.includes('python')) {
    return 'Python-based scraping cannot run on GitHub Pages. This version uses JavaScript instead, which is compatible with static hosting.';
  }

  if (text.includes('hello') || text.includes('hi')) {
    return 'Hello! I can explain the GitHub Pages version of this web scraping demo.';
  }

  return 'I can help with GitHub Pages compatibility, dataset ideas, or the static chatbot experience.';
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const userText = input.value.trim();
  if (!userText) {
    return;
  }

  addMessage(userText, 'user');
  input.value = '';
  const reply = getBotReply(userText);
  setTimeout(() => addMessage(reply, 'bot'), 250);
});

loadQuotes().then(() => {
  addMessage('Welcome! Ask about scraping, datasets, or GitHub Pages support.', 'bot');
});
