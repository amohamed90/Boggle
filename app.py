from flask import Flask, render_template, request, session, jsonify
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

    return render_template("index.html",
                           board=board,
                           high_score=high_score,
                           num_of_plays=num_of_plays)


@app.route("/submit", methods=["POST"])
def validate_word():
    #request.json because axios sends info with json
    word = request.json["word"]
    board = session["board"]
    validity = boggle_game.check_valid_word(board, word)
    
    if validity == "ok":
        return jsonify({"msg": f"Added:{word}", "cls": "success"})
    elif validity == "not-word":
        return jsonify({"msg": f"{word} is not a valid English word.", "cls": "fail"}) 
    else: 
        return jsonify({"msg": f"{word} is not a word on the board.", "cls": "fail"}) 
