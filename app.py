from flask import Flask, render_template

app = Flask(__name__)

# Jeopardy questions data structure: category, value, question, answer
CATEGORIES = ["Science", "History", "Sports", "Music", "Movies"]
VALUES = [100, 200, 300, 400, 500]
QUESTIONS = {
    "Science": {
        100: {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
        200: {"question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon Dioxide"},
        300: {"question": "What is the chemical symbol for water?", "answer": "H2O"},
        400: {"question": "What force keeps us on the ground?", "answer": "Gravity"},
        500: {"question": "What part of the cell contains DNA?", "answer": "Nucleus"},
    },
    "History": {
        100: {"question": "Who was the first President of the United States?", "answer": "George Washington"},
        200: {"question": "In which year did World War II end?", "answer": "1945"},
        300: {"question": "What wall fell in 1989?", "answer": "Berlin Wall"},
        400: {"question": "Who wrote the Declaration of Independence?", "answer": "Thomas Jefferson"},
        500: {"question": "Which empire was ruled by Julius Caesar?", "answer": "Roman Empire"},
    },
    "Sports": {
        100: {"question": "How many players are on a soccer team?", "answer": "11"},
        200: {"question": "What sport uses a puck?", "answer": "Hockey"},
        300: {"question": "What is the highest score in a single frame of bowling?", "answer": "30"},
        400: {"question": "Which country invented baseball?", "answer": "USA"},
        500: {"question": "Who has won the most Olympic gold medals?", "answer": "Michael Phelps"},
    },
    "Music": {
        100: {"question": "Who is known as the King of Pop?", "answer": "Michael Jackson"},
        200: {"question": "What instrument has 88 keys?", "answer": "Piano"},
        300: {"question": "Who sang 'Imagine'?", "answer": "John Lennon"},
        400: {"question": "What is the highest female singing voice?", "answer": "Soprano"},
        500: {"question": "Which composer became deaf?", "answer": "Beethoven"},
    },
    "Movies": {
        100: {"question": "Who played Iron Man?", "answer": "Robert Downey Jr."},
        200: {"question": "What is the highest-grossing film of all time?", "answer": "Avatar"},
        300: {"question": "Who directed 'Jurassic Park'?", "answer": "Steven Spielberg"},
        400: {"question": "What movie features a ring and a hobbit?", "answer": "The Lord of the Rings"},
        500: {"question": "Who played the Joker in 'The Dark Knight'?", "answer": "Heath Ledger"},
    },
}

@app.route('/')
def home():
    return render_template('index.html', categories=CATEGORIES, values=VALUES, questions=QUESTIONS)

if __name__ == '__main__':
    app.run(debug=True)
