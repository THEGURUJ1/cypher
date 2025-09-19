"""
SnapCaption – AI Photo-to-Caption Generator
-------------------------------------------
This script allows users to upload an image and automatically
generate catchy social media captions. 

Architecture:
1. Vision Agent (BLIP): Extracts scene description from the uploaded image.
2. Creative Agent (Groq LLM): Generates fun, short captions based on the description.
3. Orchestrator: Connects Vision + Creative agents.

Author: Your Name
Hackathon Submission
"""

import os
from typing import Tuple

from groq import Groq
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from google.colab import files


# ==============================
#  Global Configuration
# ==============================

# ⚠️ Replace with your own API key (or set as environment variable)
GROQ_API_KEY = "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"

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Load BLIP model (for image → text conversion)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


# ==============================
#  Agents
# ==============================

def vision_agent(image_path: str) -> str:
    """
    Vision Agent:
    Takes an image file path, processes it with BLIP,
    and returns a short scene description.
    
    Args:
        image_path (str): Path to the uploaded image.
    
    Returns:
        str: Scene description extracted from the image.
    """
    try:
        image = Image.open(image_path).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")
        output_ids = model.generate(**inputs)
        description = processor.decode(output_ids[0], skip_special_tokens=True)
        return f"Scene description: {description}"
    except Exception as e:
        return f"Error in Vision Agent: {str(e)}"


def creative_agent(scene_context: str) -> str:
    """
    Creative Agent:
    Uses Groq LLM to generate short, catchy captions
    from the scene description.
    
    Args:
        scene_context (str): Description of the image scene.
    
    Returns:
        str: AI-generated caption.
    """
    try:
        completion = client.chat.completions.create(
            model="gemma2-9b-it",  # Alternate option: "llama-3.1-8b-instant"
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are SnapCaption, an AI social media caption generator. "
                        "Take a short description of a photo and create 1–2 catchy, "
                        "fun captions under 15 words with emojis."
                    )
                },
                {"role": "user", "content": scene_context}
            ],
            temperature=0.9,
            max_completion_tokens=50,
            top_p=1,
            stream=False
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error in Creative Agent: {str(e)}"


def generate_caption(image_path: str) -> Tuple[str, str]:
    """
    Orchestrator:
    Runs the Vision Agent + Creative Agent in sequence.
    
    Args:
        image_path (str): Path to the uploaded image.
    
    Returns:
        Tuple[str, str]: (Scene description, AI-generated caption)
    """
    scene = vision_agent(image_path)
    caption = creative_agent(scene)
    return scene, caption


# ==============================
#  Main Application
# ==============================

if __name__ == "__main__":
    print("📎 Please upload an image file (JPG/PNG)...")
    uploaded_files = files.upload()

    for file_name in uploaded_files.keys():
        print(f"\n✅ File received: {file_name}")
        scene_text, caption_text = generate_caption(file_name)
        print("🔍 Vision Agent Output:", scene_text)
        print("✨ Generated Caption:", caption_text)