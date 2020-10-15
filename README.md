# PyramidWord
 Fetch Rewards Coding Exercise for Backend Software Engineering Internship.
 
## Challenge
Write a web service that takes in a string and returns a boolean to indicate whether a word is a pyramid word. A word is a "pyramid word" if you can arrange the letters in increasing frequency, starting with 1 and continuing without gaps and without duplicates.

For example: banana is a pyramid word because you have 1 "b", 2 "n's", and 3 "a's". Bandana is not a pyramid word because you have 1 "b" and 1 "d".

## Implementation
This project implements a web service using Python and Flask micro web framework.

It has a file containing the application, a test_pyramid class for test cases, and an is_pyramid_word POST method that accepts a string and gets called by the application and returns a boolean value, displaying it on the browser.

**Assumptions and Limitations**  
It's been assumed this web service would receive a single valid word as a input for handling the user's input.
- If the user enters multiple words, the web service will handle this input by removing whitespaces and will treat the resulting word as a single word.
- If the user enters a valid (string) word with trailing tabs, the web service will remove the tabs and check the word for pyramid or not.
- If the user enters an invalid input (such as int or float), the web service will immediately return false (the input is not a pyramid word).
- If the user enters an empty string as input, the web service will immediately return false (the input is not a pyramid word).

## Environment
- Python 3.8.5
- Flask 1.1.2

## Usage
1. Clone repository `git clone https://github.com/catalinavictoria/PyramidWord`
2. Install Python 3.8.5 (I used Homebrew for MacOS) typing command `brew install python3`
3. Create virtual environment typing command `python3 -m venv env`
4. Install Flask 1.1.2 typing command `pip3 install flask`

## How to load the webpage
1. Type command `python3 -m flask run`
2. Copy and paste `http://127.0.0.1:5000/` to the web browser.

## How to run test cases
Type command `python3 -m unittest`
