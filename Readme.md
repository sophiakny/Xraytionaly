## Xraytionaly – AI Assistant for Medical Image Analysis  

![Xraytionaly Logo](xrationaly-git-image.png)

Xraytionaly is an innovative AI-powered platform designed to assist medical professionals in analyzing chest X-rays efficiently. Our goal is to reduce the workload on radiologists, minimize human error, and improve diagnostic accuracy, especially in overloaded medical institutions.  

### 🌟 Why Xraytionaly?  
✔ **Automated X-ray analysis** – AI detects anomalies and provides insights.  
✔ **User-friendly design** – Seamless experience for medical professionals.  
✔ **Symptom-based enhancement** *(Pro version)* – Improve AI accuracy by adding symptoms.  
✔ **Secure and fast results** – Reports are integrated into electronic medical records.  

### 💼 Who is it for?  
🏥 **Clinics** – Reduce costs, optimize workflow, and speed up diagnostics.  
👨‍⚕️ **Doctors** – Get fast AI-generated reports and focus on complex cases.  
🧑‍⚕️ **Patients** – Access examination history and receive doctor recommendations.  

### 🔧 Technologies Used  
**Backend:** Flask, PyTorch, TorchXRayVision, NumPy, ImageIO, Pillow.  
**Frontend:** HTML, CSS, JavaScript.  

### 📊 Business Model  
Xraytionaly operates on a **subscription-based model** for medical institutions:  
🔹 **Basic** – AI-powered X-ray analysis.  
🔹 **Pro** – Enhanced accuracy with symptom input.  

Our vision is to bridge the gap in radiology services by providing **an accessible, intelligent, and efficient AI-powered assistant** for medical institutions worldwide. 🚀  



## 🚀 Local Setup Guide  

Follow these steps to run **Xraytionaly** locally on your Windows machine.  

### 🖥 Frontend Setup  
1. Open a terminal and navigate to the `frontend` folder:  
   ```sh
   cd frontend
   ```  
2. Install dependencies:  
   ```sh
   npm install
   ```  
3. Start the frontend server:  
   ```sh
   node server.js
   ```  

### 🛠 Backend Setup  
1. Open a terminal and navigate to the `backend` folder:  
   ```sh
   cd backend
   ```  
2. Create a virtual environment:  
   ```sh
   python -m venv venv
   ```  
3. Activate the virtual environment:  
   ```sh
   venv\Scripts\activate
   ```  
4. Install required dependencies:  
   ```sh
   pip install -r requirements.txt
   ```  
5. Start the backend server:  
   ```sh
   python server.py
   ```  

> ✅ **Note:** These setup steps are required only the first time. For subsequent runs, simply start the servers. 🚀  
