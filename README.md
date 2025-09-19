# 📸 SnapCaption – AI Photo-to-Caption Generator

## 🚀 Overview
SnapCaption is an AI-powered tool that generates **catchy social media captions** from photos in real time.  
It combines **BLIP** (for image understanding) and **Groq LLMs** (for ultra-fast caption generation).  
Perfect for influencers, meme pages, marketers, and anyone who wants instant, fun captions.

This project was built as a submission for **Cypher 2025 Hackathon** by **Abhishek**.

---

## ✨ Features
- 🖼 Upload any photo (dog, beach, selfie, etc.)
- 🔍 **Vision Agent (BLIP)** → Extracts scene description
- ✨ **Creative Agent (Groq LLM)** → Generates 1–2 catchy captions under 15 words
- ⚡ **Ultra-fast inference** powered by **Groq API**
- 📱 Works seamlessly in **Google Colab** (mobile friendly)

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

🧠 About Groq and Groq API

What is Groq?

Groq is a cutting-edge AI hardware and software company focused on ultra-low latency inference for large language models (LLMs).
Instead of traditional GPUs, Groq uses its LPU™ (Language Processing Unit) – a custom processor optimized for running AI models faster and more efficiently than GPUs or TPUs.

This makes Groq ideal for use cases where speed and real-time response are critical, such as:

Real-time chatbots

Live captioning

Instant translation

Hackathon demos where judges expect lightning-fast output


Groq API

The Groq API provides developers direct access to Groq’s accelerated LLM inference.
It works similarly to other AI APIs (like OpenAI or Anthropic), but with a unique focus on speed and scalability.

Key Features:

Ultra-low latency → Outputs in milliseconds instead of seconds

Supports multiple LLM families:

Gemma 2 (fine-tuned Google open models)

LLaMA 3.1 (Meta’s state-of-the-art LLMs)


Streaming support → Get token-by-token output instantly

Easy integration with Python, Node.js, or REST APIs


Why Groq is perfect for this project:

Hackathon demos need to be fast, fun, and magical. Waiting 5 seconds for a caption kills the flow. Groq ensures captions appear almost instantly.

Running models like gemma2-9b-it or llama-3.1-8b-instant gives high-quality, creative captions while keeping the response <1 second.



---

👨‍💻 Author

Built with ❤️ by Abhishek for Cypher 2025 Hackathon.



