# 🤖 AI Image Classifier using FastAPI & TensorFlow

A cloud-ready AI image classification web application built using **FastAPI**, **TensorFlow**, and **MobileNetV2**.

Users can upload an image through a modern web interface, and the application predicts the **Top 5 ImageNet classes** with confidence scores.

---

## 📸 Demo

### Home Page

(Add screenshot here)

### Prediction Result

(Add screenshot here)

---

## 🚀 Features

- Upload any image
- AI-powered image classification
- Top 5 predictions
- Confidence percentage bars
- Modern responsive UI
- FastAPI backend
- TensorFlow MobileNetV2
- Clean project structure

---

## 🛠 Tech Stack

- Python
- FastAPI
- TensorFlow
- MobileNetV2
- HTML
- CSS
- Jinja2
- Pillow
- NumPy

---

## 📂 Project Structure

```
01-Cloud-Image-Processing-Pipeline
│
├── app
│   ├── main.py
│   ├── model.py
│   ├── routes.py
│   └── services.py
│
├── templates
│   └── index.html
│
├── uploads
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/RoshanR-tech/Cloud-and-Backend-Projects.git
```

Go into the project

```bash
cd Cloud-and-Backend-Projects/01-Cloud-Image-Processing-Pipeline
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate it

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

## 🧠 Model Used

- TensorFlow MobileNetV2
- ImageNet pretrained weights

---

## 🎯 Future Improvements

- Drag & Drop Upload
- Docker Support
- AWS EC2 Deployment
- S3 Image Storage
- User Authentication
- History of Predictions

---

## 👨‍💻 Author

**Roshan R**

GitHub:

https://github.com/RoshanR-tech
