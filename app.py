import gradio as gr
import matplotlib.pyplot as plt
import pandas as pd
import torch
from transformers import BertTokenizer, BertForSequenceClassification, BertConfig
from safetensors.torch import load_file
from huggingface_hub import hf_hub_download
import pickle

# Hugging Face model repo ID
MODEL_REPO = "McKlay/sentiment-analysis-v2"

# Load files from Hugging Face Hub
config_path = hf_hub_download(repo_id=MODEL_REPO, filename="config.json")
model_path = hf_hub_download(repo_id=MODEL_REPO, filename="model.safetensors")
label_encoder_path = hf_hub_download(repo_id=MODEL_REPO, filename="label_encoder.pkl")

# Load model components
tokenizer = BertTokenizer.from_pretrained(MODEL_REPO)
with open(label_encoder_path, "rb") as f:
    label_encoder = pickle.load(f)

config = BertConfig.from_json_file(config_path)
model = BertForSequenceClassification(config)
model.load_state_dict(load_file(model_path))
model.eval()

# In-memory history
history = []

# Prediction function
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=1)
        pred_label_id = torch.argmax(probs, dim=1).item()
        pred_label = label_encoder.inverse_transform([pred_label_id])[0]
        confidence = float(probs[0][pred_label_id]) * 100
    return pred_label, confidence

# Gradio app logic
def analyze(text):
    sentiment, confidence = predict_sentiment(text)
    history.append({
        "Text": text,
        "Sentiment": sentiment,
        "Confidence": confidence
    })

    emoji_map = {
        "negative": "😠",
        "neutral": "😐",
        "positive": "😊"
    }
    sentiment_display = emoji_map.get(sentiment.lower(), "❓")

    result_markdown = f"""
### 🧠 Prediction: **{sentiment.upper()} {sentiment_display}**  
**Confidence:** {confidence:.2f}%"""

    hist_md = ""
    for item in reversed(history):
        hist_md += f"""
**{item['Sentiment']}**: {item['Text']}  
*Confidence: {item['Confidence']:.2f}%*  
---
"""

    # Chart
    df = pd.DataFrame(history)
    sentiment_counts = df['Sentiment'].value_counts()
    fig, ax = plt.subplots()
    color_map = {
        "positive": "#4ade80",
        "neutral": "#facc15",
        "negative": "#f87171"
    }
    ax.pie(
        sentiment_counts,
        labels=sentiment_counts.index,
        colors=[color_map.get(label.lower(), "#a1a1aa") for label in sentiment_counts.index],
        autopct='%1.1f%%',
        startangle=90
    )
    ax.axis('equal')

    csv_path = "prediction_history.csv"
    df.to_csv(csv_path, index=False)

    return result_markdown, hist_md, fig, csv_path

# Launch Gradio app
with gr.Blocks(css="""
#centered-layout {
    max-width: 900px;
    margin: auto;
    padding: 2rem;
    text-align: center;
}
#title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 1rem;
}
.gr-button {
    font-weight: 600;
}
""") as demo:
    with gr.Column(elem_id="centered-layout"):
        gr.Markdown("## 😊 Sentiment Analysis Tool", elem_id="title")
        gr.Markdown("Analyze any comment using your fine-tuned BERT model. Supports Positive, Negative, and Neutral classification.")

        input_box = gr.Textbox(label="💬 Enter Comment", lines=4, placeholder="Type a comment...")
        analyze_btn = gr.Button("🔍 Analyze Sentiment")
        result_display = gr.Markdown()

        chart_output = gr.Plot(label="📊 Sentiment Distribution")

        with gr.Row():
            clear_btn = gr.Button("🧹 Clear History")
            csv_download = gr.File(label="📥 Export History")

        with gr.Accordion("📜 Prediction History", open=False):
            history_box = gr.Markdown()

        analyze_btn.click(analyze, inputs=input_box, outputs=[result_display, history_box, chart_output, csv_download])

        def clear_history():
            history.clear()
            return "", "", plt.figure(), None

        clear_btn.click(clear_history, outputs=[result_display, history_box, chart_output, csv_download])

demo.launch()
