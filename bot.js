cat > bot.js << 'EOF'
require("dotenv").config();
const TelegramBot = require("node-telegram-bot-api");
const axios = require("axios");

const bot = new TelegramBot(process.env.TELEGRAM_TOKEN, { polling: true });

// simple in-memory memory (NOT DB)
const memory = {};

function getMemory(id) {
  if (!memory[id]) memory[id] = [];
  return memory[id];
}

function saveMemory(id, role, content) {
  const mem = getMemory(id);
  mem.push({ role, content });
  if (mem.length > 15) mem.shift();
}

function buildMessages(id, text) {
  const system = {
    role: "system",
    content: `
You are Omega AI.

Identity:
- Created by Thomas Lee Harvey
- You are a persistent assistant
- You maintain conversational continuity
- You respond naturally and intelligently
`
  };

  const mem = getMemory(id).map(m => ({
    role: m.role,
    content: m.content
  }));

  return [system, ...mem, { role: "user", content: text }];
}

async function askOmega(messages) {
  const res = await axios.post(
    "https://openrouter.ai/api/v1/chat/completions",
    {
      model: "openai/gpt-4o-mini",
      messages
    },
    {
      headers: {
        Authorization: `Bearer ${process.env.OPENROUTER_API_KEY}`,
        "Content-Type": "application/json"
      }
    }
  );

  return res.data.choices[0].message.content;
}

bot.on("message", async (msg) => {
  const id = msg.chat.id;
  const text = msg.text;

  if (!text) return;

  try {
    saveMemory(id, "user", text);

    bot.sendChatAction(id, "typing");

    const messages = buildMessages(id, text);
    const reply = await askOmega(messages);

    saveMemory(id, "assistant", reply);

    bot.sendMessage(id, reply);
  } catch (err) {
    console.log(err.message);
    bot.sendMessage(id, "🧠 Omega error (cloud or API issue)");
  }
});

console.log("🧠 Omega Telegram Bot Online");
EOF
