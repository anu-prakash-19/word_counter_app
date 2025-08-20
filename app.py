from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def word_counter():
    count = None
    text = ""
    if request.method == "POST":
        text = request.form["text"]
        words = text.split()
        count = len(words)
    return render_template("index.html", count=count, text=text)

if __name__ == "__main__":
    app.run(debug=True)
