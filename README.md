# 🩺 Medical Chatbot with PDF Knowledge Base </br>

This project is a medical chatbot that uses custom knowledge base extracted from a PDF (e.g., 71763-gale-encyclopedia-of-medicine.-vol.-1.-2nd-ed.pdf). </br>
It allows users to ask health-related questions and receive accurate, context-aware answers.

## 🚀 Features
📄 Custom Knowledge Base – Trained on your medical PDF (e.g., Gale Encyclopedia of Medicine).

💬 Interactive Chat UI – Simple and modern web interface.

☁ Flask Backend – Handles AI requests and PDF-based responses.

🎨 Light Mode Design – Clean and modern styling with HTML + CSS.

##  Project Structure
├── chatbot.py        # Flask backend for handling chat requests </br>
├── index.html        # Frontend chat interface </br>
├── style.css         # Styling for chat UI </br>
├── requirements.txt  # Python dependencies </br>
├── medical.pdf       # Your medical reference PDF </br>
└── README.md         # This file

## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
git clone https://github.com/muchirikinyua/medical-chatbot.git
cd medical-chatbot
### 2️⃣ Install Dependencies
pip install -r requirements.txt
### 3️⃣ Add Your PDF

Place your medical PDF in the project root.

Update chatbot.py to load your file name.

### 4️⃣ Run the Chatbot
python chatbot.py
### 5️⃣ Open in Browser
http://127.0.0.1:5000
### 🛠 Requirements
Python 3.8+

Flask

PyPDF2 or pdfplumber

OpenAI API key (if using GPT)

