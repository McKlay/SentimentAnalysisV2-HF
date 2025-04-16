---
title: 😊 Sentiment Analysis Tool
emoji: 🧠
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: "4.15.0"
app_file: app.py
pinned: false
---

[![HF Spaces](https://img.shields.io/badge/🤗%20HuggingFace-Space-blue?logo=huggingface&style=flat-square)](https://huggingface.co/spaces/McKlay/SentimentAnalysisV2-HF)
[![Gradio](https://img.shields.io/badge/Built%20with-Gradio-orange?logo=gradio&style=flat-square)](https://www.gradio.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# 🧠 Universal Comment Sentiment Analyzer

This interactive web app performs sentiment analysis on any comment using a fine-tuned BERT model. It predicts whether a comment is **Positive**, **Neutral**, or **Negative**, and visualizes the sentiment distribution in real time.

### ✨ Features

- 🔍 Instant sentiment prediction with confidence scores
- 📈 Pie chart visualization of sentiment trends
- 📜 Scrollable prediction history with collapsible view
- 💾 Exportable CSV of all predictions
- 🎨 Custom Gradio theme with dark mode aesthetics

### 🧠 Model Details

- Base: [`bert-base-uncased`](https://huggingface.co/bert-base-uncased)
- Fine-tuned on YouTube and general domain comments
- Label classes: `positive`, `neutral`, `negative`
- Hosted model: [`McKlay/sentiment-analysis-v2`](https://huggingface.co/McKlay/sentiment-analysis-v2)

### 📦 Technology Stack

- 🤗 `transformers`
- 🔥 `torch`
- 🎨 `gradio`
- 📊 `pandas`, `matplotlib`

---

### 📸 Thumbnail Preview

![App thumbnail](thumbnail.png)

---

### 👨‍💻 Author

**Clay Mark Sarte**  
[Hugging Face](https://huggingface.co/McKlay) • [GitHub](https://github.com/McKlay) • [LinkedIn](https://linkedin.com)

---

### 📝 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).