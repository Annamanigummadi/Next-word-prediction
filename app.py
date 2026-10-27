from flask import Flask, render_template, request
from collections import defaultdict
app = Flask(__name__)
# ---------- Read Corpus ----------
with open("corpus.txt", "r") as f:
    text = f.read().lower()
words = text.split()
# ---------- Build Bigram Model ----------
bigram_count = defaultdict(int)
total_count = defaultdict(int)
for i in range(len(words) - 1):
    w1 = words[i]
    w2 = words[i + 1]
    bigram_count[(w1, w2)] += 1
    total_count[w1] += 1
# ---------- Prediction Function (Top-3) ----------
def predict_next_words(prev_word, top_n=3):
    probs = {}
    for (w1, w2), count in bigram_count.items():
        if w1 == prev_word:
            probs[w2] = count / total_count[w1]

   if not probs:
    return [("No prediction found", 0.0)]
    # Sort by probability
    sorted_words = sorted(probs.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]  # list of tuples (word, prob)
# ---------- Flask Routes ----------
@app.route("/", methods=["GET", "POST"])
def home():
    predictions = []
    if request.method == "POST":
        sentence = request.form["sentence"]
        if sentence.strip() != "":
            last_word = sentence.lower().split()[-1]
            predictions = predict_next_words(last_word)
    return render_template("index.html", predictions=predictions, sentence=request.form.get("sentence", ""))
# ---------- Run Flask ----------
if __name__ == "__main__":
    app.run(debug=True)
