from flask import Flask, render_template, request
from pyramid import is_pyramid_word

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/pyramid_word', methods=['GET', 'POST'])
def pyramid_word():
    # take user input
    user_input = request.form['word']
    # check for pyramid
    if is_pyramid_word(user_input):
        msg = "It's pyramid!"
    else:
        msg = "Not a pyramid word :("
    return render_template('result.html', msg=msg)


if __name__=="__main_":
    app.run()
