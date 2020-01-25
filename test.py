from unittest import TestCase
from app import app
from flask import session, jsonify
from boggle import Boggle
from app import boggle_game

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_load_game(self):
        with app.test_client() as client:
            resp = client.get("/")

            self.assertEqual(resp.status_code, 200)
            self.assertNotEqual(session["board"], [])


    def test_validation(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["board"] = [["B","O","A","R","D"],
                                          ["B","O","A","R","D"],
                                          ["B","O","A","R","D"],
                                          ["B","O","A","R","D"],
                                          ["B","O","A","R","D"]]
            resp = (client.post("/submit", json={"word": "board"})).json

            self.assertEqual(resp["cls"], "success")
