from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	#email = StringField ('What is your UofT Email address?', validators=[Required()])

	#def validate_email(form, field):
		#if '@' not in field.data:
		#	raise ValidationError("Please include an '@' in the email address. {form.data.email} is missing an '@'")
	
	submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootsrap = Bootstrap(app)
moment = Moment(app)


@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	#email = None
	#email_domain = 'utoronto'
	#non_uoft = False
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data

		#session['email'] = form.email.data
		#uoft_email = session.get('email')
		#if uoft_email is not None and email_domain not in uoft_email:
		#	non_uoft = True
		#	session['email'] = None
		#	flash('Looks like you have changed your email!')
		
		return redirect(url_for('index'))
	return render_template('index.html',
		form = form, name = session.get('name'))
		#email = session.get('email'), non_uoft_email = non_uoft )

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name, current_time=datetime.utcnow())
	
	if __name__ == '__main__':    
		app.run(debug=True)
		