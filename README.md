# PyramidWord
 Fetch Rewards Coding Exercise for Backend Software Engineering Internship.
 
## Challenge
Write a web service that takes in a string and returns a boolean to indicate whether or not a word is a pyramid word. A word is a "pyramid word" if you can arrange the letters in increasing frequency, starting with 1 and continuing without gaps and without duplicates.

For example: banana is a pyramid word because you have 1 "b", 2 "n's", and 3 "a's". bandana is not a pyramid word because you have 1 "b" and 1 "d".

## Implementation
This project implements a web service using Python and Flask micro web framework.

It has a file containing the application, a test_pyramid class for test cases and a is_pyramid_word POST method that accepts a string and gets called by the application and returns a boolean value, displaying it on the browser.

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
