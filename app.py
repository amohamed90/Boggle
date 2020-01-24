from flask import Flask, render_template, request, session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "sgdshfgsykudfgdsuilfhlsdif"

boggle_game = Boggle()

@app.route("/")
def load_game():
    board = boggle_game.make_board()
    session["board"] = board
    high_score = session.get("high_score", 0)
    num_of_plays = session.get("num_of_plays", 0)

    return render_template("index.html", board=board, high_score=high_score, num_of_plays=num_of_plays)