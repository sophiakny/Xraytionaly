from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import numpy as np
from PIL import Image
from io import BytesIO
import torchxrayvision as xrv
import torch, torchvision

def format_disease_probabilities(disease_probs):

    filtered_diseases = {
        disease: prob for disease, prob in disease_probs.items() if prob > 45
    }

    sorted_diseases = sorted(filtered_diseases.items(), key=lambda x: -x[1])[:5] 
    
    result = "Possible diseases:<br>" 
    descriptions = [f"{disease} ({prob:.1f}%)" for disease, prob in sorted_diseases]
    
    result += "<br>".join(descriptions) 
    
    return result



app = Flask(__name__)
CORS(app) 

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify("Файл не знайдено"), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify("Файл не вибрано"), 400


    image = Image.open(BytesIO(file.read()))
    image = image.convert("RGB")
    
  
    img = np.array(image)

    img = xrv.datasets.normalize(img, 255)
    img = img.mean(2)[None, ...] 
    transform = torchvision.transforms.Compose([xrv.datasets.XRayCenterCrop(),xrv.datasets.XRayResizer(224)])

    img = transform(img)
    img = torch.from_numpy(img)
    model = xrv.models.DenseNet(weights="densenet121-res224-all")
    outputs = model(img[None,...]) 
    dictRes = dict(zip(model.pathologies,outputs[0].detach().numpy()))
    dictResSort = {k: v * 100 for k, v in sorted(dictRes.items(), key=lambda item: -item[1])} 

    return jsonify(format_disease_probabilities(dictResSort))

if __name__ == "__main__":
    app.run(debug=True)