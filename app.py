from flask import Flask, send_file
import random

app = Flask(__name__)

def load_quotes():
    with open("quotes.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]

quotes = load_quotes()

@app.route('/')
def index():
    quote = random.choice(quotes)
    
    # Read index.html content and replace placeholder with quote
    with open("index.html", "r") as f:
        html = f.read().replace("{{ quote }}", quote)
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
