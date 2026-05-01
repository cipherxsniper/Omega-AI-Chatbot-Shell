cat > server.js << 'EOF'
const express = require("express");
const app = express();

app.use(express.json());

app.get("/health", (req, res) => {
  res.json({ status: "Omega Online", time: new Date().toISOString() });
});

app.post("/chat", (req, res) => {
  res.json({ ok: true, message: "Use Telegram bot for chat layer" });
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, "0.0.0.0", () => {
  console.log("🧠 Omega Cloud Brain running on", PORT);
});
EOF
