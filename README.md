---
title: Sentiment Analysis V2 (Gradio)
emoji: 🧠
colorFrom: gray
colorTo: purple
sdk: gradio
sdk_version: "4.27.0"
app_file: app.py
pinned: true
---

# 🧠 Sentiment Analysis V2 (Gradio Version)

A lightweight sentiment classification web app using a fine-tuned **BERT** model.

> Hosted entirely on [🤗 Hugging Face Spaces](https://huggingface.co/spaces/McKlay/SentimentAnalysisV2-HF) using **Gradio** and **Transformers**.

---

## ⚙️ Tech Stack
- 🤗 **Transformers** for BERT-based text classification
- 🔥 **PyTorch** for model inference
- 🎨 **Gradio** for building the web interface
- 🚀 **Hugging Face Spaces** for free app hosting

---

## 🧪 Try It Out
Paste a sentence into the textbox and get real-time sentiment probabilities (positive/negative) with confidence levels.

---

## 📁 File Structure
SentimentAnalysisV2-HF/ 
├── app.py # Main Gradio app 
├── model/ # empty, the model is located in model hub McKlay/sentiment-analysis-v2 
├── requirements.txt # Dependency file 
├── .gitignore └── README.md

---

## ✅ How It Works

1. Loads the tokenizer and model from the `model/` folder.
2. Processes input text and runs inference using BERT.
3. Returns the confidence scores for each sentiment label.
4. All of this happens **live** in your browser via Gradio!

---

## ✨ Author

**Clay Mark Sarte**  
[GitHub: @McKlay](https://github.com/McKlay)  
Passionate about AI, ML, and building useful tools with minimal stack.

---

## 📜 License

MIT License — free to use and modify.

