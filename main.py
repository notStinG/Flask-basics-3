from flask import Flask, render_template


app = Flask(__name__)

@app_route("/")
def home():
    return render_template("index.html")

@app_route("/<text>")
def analyse(text):
    length = len(text)
    num_digit = 0
    num_vowel = 0
    for char in text:
        if char.isdigit():
            num_digit += 1
        if char.lower() in "aeiou":
            num_vowels += 1
    letter_freq = dict()
    for char in text:
        char.lower()
        if char not in letter_freq:
            letter_freq(char) = 1
        else:
            letter_freq(char) += 1
    return render_template("analysis.html", text=text, length=length\
                           , num_digits=num_digits, num_vowels = num_vowels\
                           , letter_freq=letter_freq)

if __name__ == "__main__":
    app.run(debug=True, port=6969)
