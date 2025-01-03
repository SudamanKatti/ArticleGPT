from flask import Flask, request, render_template, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
from sentence_transformers import SentenceTransformer, util
from textblob import TextBlob

app = Flask(__name__)

model_path = "model/content/Results2/checkpoint-5015"
tokenizer_path = "model"
tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
model = GPT2LMHeadModel.from_pretrained(model_path)


embedding_model = SentenceTransformer('all-MiniLM-L6-v2')


history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, num_return_sequences=1,max_length=250,pad_token_id=model.config.eos_token_id, eos_token_id=model.config.eos_token_id, do_sample=True, top_k=50,top_p=0.96)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Save prompt and response in history
    history.append({"prompt": prompt, "response": response})

    return jsonify({"response": response})

# Metrics functions
def calculate_relevancy(prompt, response):
    try:
        prompt_embedding = embedding_model.encode(prompt, convert_to_tensor=True)
        response_embedding = embedding_model.encode(response, convert_to_tensor=True)
        return util.cos_sim(prompt_embedding, response_embedding).item()
    except Exception as e:
        print(f"Error in relevancy calculation: {e}")
        return 0


def calculate_answerability(prompt, response):
    try:
        prompt_embedding = embedding_model.encode(prompt, convert_to_tensor=True)
        response_embedding = embedding_model.encode(response, convert_to_tensor=True)
        return 1 - (len(response.split())/len(response.split())) * util.cos_sim(prompt_embedding, response_embedding).item()
    except Exception as e:
        print(f"Error in answerability calculation: {e}")
        return 0

def calculate_style(response):
    try:
        blob = TextBlob(response)
        return blob.sentiment.polarity
    except:
        return 0

      

@app.route("/metrics", methods=["GET", "POST"])
def metrics():
    if not history:
        return render_template("metrics.html", metrics=[])

    metrics_data = []
    for item in history:
        scores = {
            "relevancy": calculate_relevancy(item["prompt"], item["response"]),
            "answerability": calculate_answerability(item["prompt"], item["response"]),
            "style": calculate_style(item["response"])
        }
        metrics_data.append({
            "prompt": item["prompt"],
            "response": item["response"],
            "scores": scores
        })

    return render_template("metrics.html", metrics=metrics_data)

if __name__ == "__main__":
    app.run(debug=True)
