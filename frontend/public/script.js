document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("fileInput");
    const preview = document.getElementById("preview");
    const uploadBtn = document.getElementById("uploadBtn");
    const loadingText = document.getElementById("loadingText");
    const statusDiv = document.getElementById("status");

    // Функція для відображення прев'ю зображення
    fileInput.addEventListener("change", function () {
        const file = fileInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                preview.src = e.target.result;
                preview.style.display = "block";
            };
            reader.readAsDataURL(file);
        }
    });

    // Відправка зображення на сервер Flask
    uploadBtn.addEventListener("click", async function () {
        if (!fileInput.files.length) {
            alert("Будь ласка, виберіть файл!");
            return;
        }

        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        loadingText.style.display = "block"; // Показати анімацію завантаження

        try {
            const response = await fetch("http://127.0.0.1:5000/upload", {
                method: "POST",
                body: formData
            });

            const result = await response.json();
            statusDiv.innerHTML = `<p>✅ Відповідь сервера: ${JSON.stringify(result)}</p>`;
        } catch (error) {
            console.error("Помилка:", error);
            statusDiv.innerHTML = "<p style='color: red;'>❌ Помилка завантаження</p>";
        } finally {
            loadingText.style.display = "none"; // Приховати анімацію після завершення
        }
    });
});
