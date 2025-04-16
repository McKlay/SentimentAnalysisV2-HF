import gradio as gr
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load model and tokenizer from Hugging Face Hub
MODEL_DIR = "McKlay/sentiment-analysis-v2"
tokenizer = BertTokenizer.from_pretrained(MODEL_DIR)
model = BertForSequenceClassification.from_pretrained(MODEL_DIR)
model.eval()

# Define prediction function
def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    labels = ['Negative', 'Positive']
    return {labels[i]: float(probs[0][i]) for i in range(2)}

# Launch Gradio interface
gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=3, placeholder="Enter a comment..."),
    outputs=gr.Label(num_top_classes=2),
    title="Sentiment Analysis V2 (Gradio)",
    description="Real-time sentiment analysis using a BERT-based model. Powered by 🤗 Transformers and Gradio."
).launch()
