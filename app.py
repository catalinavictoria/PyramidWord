from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/pyramid_word', methods=['GET', 'POST'])
def pyramid_word():
    # save input from the user into a variable
    user_input = request.form['word']
    # eliminate whitespaces
    str = user_input.replace(" ", "")
    # declare needed variables
    result = ""
    # check for empty string
    if len(str) == 0:
        result = "Not a pyramid word"
        return render_template('result.html', result=result)
    # initialize a counter
    word_count = Counter()
    # traverse the string to get the letters
    for letter in str:
        word_count[letter] += 1
    # sorting count of letter
    sorted_count = sorted(word_count.values())
    # compare index and num, if they don't differ by one, the word is not a pyramid
    for i, num in enumerate(sorted_count):
        if num - i != 1:
            result = "Not a pyramid word :("
            return render_template('result.html', result=result)
    result = "It's pyramid!"
    return render_template('result.html', result=result)
    

if __name__=="__main_":
    app.run()
