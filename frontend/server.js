const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

// Обслуговуємо статичні файли (HTML, CSS, JS)
app.use(express.static(path.join(__dirname, "public")));

app.listen(PORT, () => {
    console.log(`Фронтенд-сервер запущено на http://localhost:${PORT}`);
});

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "", "index.html"));
});