from flask import Flask, render_template, request
from pyramid import is_pyramid_word

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    """
    This method renders the form.html template, where the user enters the expected word.
    :param: none
    :return: a rendered HTML file.
    """
    return render_template('form.html')

@app.route('/pyramid_word', methods=['POST'])
def pyramid_word():
    """
    This is a POST method that retreives the information from the HTML input element.
    It takes the user input calls the is_pyramid_word method to test if the word is pyramid or not.
    After rendering the result.html template, it displays a message indicating if the entered word is pyramid or not.
    :param: none
    :return: a rendered HTML file, containing a display message.
    """
    # take user input
    user_input = request.form['word']
    # check for pyramid
    if is_pyramid_word(user_input):
        msg = "It's pyramid!"
    else:
        msg = "Not a pyramid word :("
    return render_template('result.html', msg=msg)

if __name__=="__main__":
    app.run()
