from flask import Blueprint, render_template, request, flash
from BMICalc import BMICalc

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def bmi():
    if request.method == 'POST':
        feet = float(request.form.get('height1'))
        inch = float(request.form.get('height2'))
        lbs = float(request.form.get('weight'))
        h = (feet * 12.0 + inch) * 0.025
        w = lbs * 0.45
        bmi = BMICalc(h,w)
        message1 = 'Your bmi is ' + str(bmi.bmi_value())
        message2 = 'you are considered ' + str(bmi.giveBMI())
        flash(message1, category='success')
        flash(message2, category='success')

    return render_template("bmi.html")