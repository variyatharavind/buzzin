from flask import Flask, render_template, request
import os
import yaml

app = Flask(__name__)

BOARDS_DIR = os.path.join(os.path.dirname(__file__), 'boards')
VALUES = [100, 200, 300, 400, 500]

def load_boards():
    boards = {}
    for fname in os.listdir(BOARDS_DIR):
        if fname.endswith('.yaml'):
            with open(os.path.join(BOARDS_DIR, fname), 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                board_id = os.path.splitext(fname)[0]
                boards[board_id] = {
                    'name': data.get('name', board_id.title()),
                    'categories': list(data['questions'].keys()),
                    'questions': data['questions']
                }
    return boards

ALL_BOARDS = load_boards()

@app.route('/', methods=['GET'])
def home():
    board_id = request.args.get('board')
    if not board_id or board_id not in ALL_BOARDS:
        board_id = list(ALL_BOARDS.keys())[0]  # default to first
    board = ALL_BOARDS[board_id]
    return render_template(
        'index.html',
        board_id=board_id,
        board_name=board['name'],
        board_list=[{'id': k, 'name': v['name']} for k, v in ALL_BOARDS.items()],
        categories=board['categories'],
        values=VALUES,
        questions=board['questions']
    )

if __name__ == '__main__':
    app.run(debug=True)
