from flask import Flask, request, render_template
import requests

app = Flask(__name__)

HF_TOKEN = "PONE_TU_TOKEN_AQUI" 
MODEL = "gpt2"  

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form["question"]

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{MODEL}",
        headers={"Authorization": f"Bearer {HF_TOKEN}"},
        json={"inputs": question}
    )

    try:
        answer = response.json()[0]["generated_text"]
    except:
        answer = "No pude generar respuesta, intentá de nuevo."

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run()