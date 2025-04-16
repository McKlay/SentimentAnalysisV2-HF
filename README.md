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

# 🧠 Universal Comment Sentiment Analyzer

A fast and user-friendly sentiment analysis tool powered by a fine-tuned BERT model, capable of classifying comments into **Positive**, **Negative**, or **Neutral** sentiments.

## 🚀 Features

- 🔍 Real-time sentiment analysis
- 📈 Live sentiment distribution pie chart
- 📜 Accordion-style prediction history
- 📥 Export results as CSV
- 🎨 Responsive and styled with custom CSS

## 🧠 Model Info

- **Base model:** `bert-base-uncased`
- **Fine-tuned on:** YouTube comments and open-domain feedback
- **Hosted on Hugging Face:** [`McKlay/sentiment-analysis-v2`](https://huggingface.co/McKlay/sentiment-analysis-v2)

## 🛠️ How It Works

- Loads the tokenizer, model weights, config, and label encoder directly from Hugging Face Model Hub
- Uses Gradio for a sleek web UI
- Classifies single input comments and provides a confidence score

## 📊 Sample Outputs

| Text | Sentiment | Confidence |
|------|-----------|------------|
| "Amazing explanation!" | Positive | 98.45% |
| "This topic is confusing..." | Neutral | 87.13% |
| "Worst tutorial ever." | Negative | 92.09% |

## 🧪 Try it now

Type any comment in the text box and hit **Analyze Sentiment** to see the result and visual breakdown!

---

### 👨‍💻 Author

Clay Mark Sarte  
[Hugging Face Profile](https://huggingface.co/McKlay)
