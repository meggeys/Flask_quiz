from flask import Flask
from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask import session
from Flask_quiz.auth import login_required

bp = Blueprint('quit', __name__)
app = Flask(__name__)
app.secret_key="SECRETKEY"


@bp.route('/')
@login_required
def index():
	return render_template('quiz/index.html')

@bp.route('/', methods = ['GET', 'POST'])
def show_answer():
	if request.method == 'POST':

		# if the submit button for question 1 is clicked
		if "Question 1" in request.form and request.form['Question 1'] == 'Submit answer':

			# save the answer from the user for the session
			session["form_antwort_1"] = request.form["answer1"]

			# right answer for question 1
			session["answer_1"] = "Chocolate."

			# set key to True to trigger the "if" for question 1 in index.html
			session["show_answer1"] = True

		# if the submit button for the points question is clicked
		elif "Points1_btn" in request.form and request.form["Points1_btn"] == "Submit answer":

			# if "yes" is selected
			if "Points" in request.form and request.form["Points"] == "Yes":
				session["points_1"] = 1
			else:
				session["points_1"] = 0

		# same as for question 1
		elif "Question 2" in request.form and request.form['Question 2'] == 'Submit answer':
			session["form_antwort_2"] = request.form["answer2"]
			session["answer_2"] = "Cookies."
			session["show_answer2"] = True
		elif "Points2_btn" in request.form and request.form["Points2_btn"] == "Auswahl bestätigen":
			if "Points" in request.form and request.form["Points"] == "Yes":
				session["points_2"] = 1
			else:
				session["points_2"] = 0

		# add all points together
		points = session.get("points_1", 0) + session.get("points_2", 0)
		return render_template(
			'quiz/index.html',
			user_result2 = session.get("form_antwort_2", ""), result2=session.get("antwort_2", ""), expl_2=session.get("Erklaerung_2", ""), show_answer2=session.get("show_answer2", False),
			user_result1 = session.get("form_antwort_1", ""), result1=session.get("antwort_1", ""), expl_1=session.get("Erklaerung_1", ""), show_answer1=session.get("show_answer1", False),
			points=points
							)
