from flask import Flask, request, jsonify
from flask_cors import CORS  # Додаємо CORS
import os
import numpy as np
from PIL import Image
from io import BytesIO
import torchxrayvision as xrv
import torch, torchvision


app = Flask(__name__)
CORS(app)  # Додає підтримку CORS

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Створюємо папку, якщо її немає

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"message": "Файл не знайдено"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"message": "Файл не вибрано"}), 400

    # Зчитуємо файл без збереження
    image = Image.open(BytesIO(file.read()))
    image = image.convert("RGB")  # Конвертуємо в RGB (якщо PNG або інші формати)
    
    # Перетворюємо зображення в numpy array
    img = np.array(image)

    img = xrv.datasets.normalize(img, 255) # convert 8-bit image to [-1024, 1024] range
    img = img.mean(2)[None, ...] # Make single color channel
    transform = torchvision.transforms.Compose([xrv.datasets.XRayCenterCrop(),xrv.datasets.XRayResizer(224)])

    img = transform(img)
    img = torch.from_numpy(img)
    model = xrv.models.DenseNet(weights="densenet121-res224-all")
    outputs = model(img[None,...]) # or model.features(img[None,...]) 
    dictRes = dict(zip(model.pathologies,outputs[0].detach().numpy()))
    dictResSort = {k: v for k, v in sorted(dictRes.items(), key=lambda item: item[1])}

    return jsonify({
        "message": "Файл успішно завантажено",
        "dictResSort": str(dictResSort)
    })

if __name__ == "__main__":
    app.run(debug=True)
