from flask import Flask, render_template
import random

app = Flask(__name__)

def load_quotes():
    with open("quotes.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]

quotes = load_quotes()

@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
