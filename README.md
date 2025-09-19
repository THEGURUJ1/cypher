# 📸 SnapCaption – AI Photo-to-Caption Generator

## 🚀 Overview
SnapCaption is an AI-powered tool that generates **catchy social media captions** from photos in real time.  
It combines **BLIP** (for image understanding) and **Groq LLMs** (for ultra-fast caption generation).  
Perfect for influencers, meme pages, and anyone who wants instant, fun captions.

---

## ✨ Features
- 🖼 Upload any photo (dog, beach, selfie, etc.)
- 🔍 Vision Agent (BLIP) → Extracts scene description
- ✨ Creative Agent (Groq LLM) → Generates 1–2 catchy captions under 15 words
- ⚡ Sub-second inference powered by **Groq API**
- 📱 Runs easily in **Google Colab** (mobile friendly)

---

## 🛠 Tech Stack
- **Python 3.10+**
- **Groq API** (`gemma2-9b-it`, `llama-3.1-8b-instant`)
- **Hugging Face Transformers** (`Salesforce/blip-image-captioning-base`)
- **Pillow** (for image processing)
- **Google Colab / Jupyter** (runtime)

---

## 📂 Project Structure

SnapCaption/ │── app.py              # Main script (Vision + Creative agents) │── requirements.txt    # Python dependencies │── README.md           # Project documentation

---

## 🔧 Setup & Installation

1. **Clone this repo**
   ```bash
   git clone https://github.com/<your-username>/SnapCaption.git
   cd SnapCaption

2. Install dependencies

pip install -r requirements.txt


3. Set your Groq API key

Open app.py and replace:

GROQ_API_KEY = "your_api_key_here"

Or, set it as an environment variable:

export GROQ_API_KEY="your_api_key_here"



4. Run the app

python app.py


5. Upload an image

When prompted, upload a JPG/PNG file.

The app will print:

Scene description (Vision Agent)

Catchy caption (Creative Agent)






---

📱 Try it in Colab

Want a quick demo?
👉 Open in Google Colab and run without local setup.


---

📸 Example

Input Image: Two friends smiling on a beach during sunset
Vision Agent Output: Scene description: two people standing on the beach at sunset
Creative Agent Caption: Golden hour vibes 🌅✨


---

📈 Future Improvements

Add multiple caption styles (funny, poetic, professional)

Deploy Streamlit web app with live upload

Direct posting to Instagram/Twitter via MCP



---

👨‍💻 Author

Built with ❤️ for cyoher 2025.
By Abhishek Bhandare 



