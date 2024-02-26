from flask import Flask, render_template
import string
import random

app = Flask(__name__)

def generate_password(length, letters, symbols, numbers):
    alphabets = ""
    if letters:
        alphabets += string.ascii_letters
    if symbols:
        alphabets += string.punctuation
    if numbers:
        alphabets += string.digits
    if not alphabets:
        return "You didn't select anything!"
    for i in range(length):
        password += random.choice(alphabets)
    return password

@app.route('/', methods=['POST'])
def index(request):
    if request.method == 'POST':
        length = int (request.POST.get('length'))
        letters = "letters" in request.form
        numbers = "numbers" in request.form
        symbols = "symbols" in request.form
        password = generate_password(length, letters, numbers, symbols)
    return render_template("index.html")



app.run(debug = True)