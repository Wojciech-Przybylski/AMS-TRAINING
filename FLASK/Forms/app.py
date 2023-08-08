from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

food = ['pizza', 'spaghetti', 'chilli']


class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    dob = StringField('Date of Birth')
    fav_number = StringField('Favourite Number')
    fav_food = SelectField('Choose your favourite food', choices=food)
    submit = SubmitField('Add Info')
    
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        fav_number = form.fav_number.data
        fav_food = form.fav_food.data

        if len(first_name) == 0 or len(last_name) == 0 or len(dob) == 0 or len(fav_number) == 0:
            message = "Fill in all the criteria"
        else:
            message = f'Thank you, \n {first_name} {last_name} \n Date of birth: {dob} \n Your favourite number is: {fav_number}, Your favourite food is: {fav_food}'

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')