from flask import Blueprint, jsonify, render_template, request, redirect, url_for,session,flash
from blueprints.backend.model.users.models import User
from blueprints.frontend.login.forms import LoginForm
#from blueprints.frontend.form.signup.forms import SignupForm
#from blueprints.frontend.models.signup.models import Signup
from flask_login import LoginManager, login_user, login_required, logout_user,current_user
from extension import db
from passlib.hash import sha256_crypt
import os

login = Blueprint('login', __name__, template_folder="templates")


@login.route('/login', methods=['GET','POST'])
def login_index():
	if current_user.is_authenticated and not current_user.is_anonymous:
		return redirect(url_for('backend.users_index'))
	form = LoginForm()
	if request.method == 'POST' and form.validate():
		user=User.query.filter_by(email=form.email.data).first()
		password_candidate=form.password.data
		if sha256_crypt.verify(password_candidate, user.password):
			user.authenticated = True
			login_user(user)
			return redirect(url_for('backend.users_index'))
			flash('Invalid username password')
		return redirect(url_for('login.login_index'))	
	return render_template('login/login.html',form=form)

@login.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login.login_index'))

@login.route('/home')
def home():
  return render_template('home/home.html')

@login.route('/cashier')
def cashier():
    return render_template('cashier/cashier.html')

@login.route('/hotel')
def hotel():
    return render_template('hotel/hotel.html')

#@frontend.route('/signup',methods=['GET','POST'])
#def signup_create():
    #form = SignupForm(request.form)
    #if request.method == 'POST' and form.validate():
     #   firstname = request.form.get('firstname')
      #  lastname = request.form.get('lastname')
       # middlename = request.form.get('middlename')
        #address = request.form.get('address')
        #mobile = request.form.get('mobile')
        #email = request.form.get('email')
        #role = request.form.get('role')
        #password = request.form.get('password')
        #pw_hash = sha256_crypt.encrypt(str(password))
        #created_at = request.form.get('created_at')
        #updated_at = request.form.get('updated_at')

        #users = Signup (
         #   firstname=firstname,
          #  lastname=lastname,
           # middlename=middlename,
         #   address=address,
          #  mobile=mobile,
           # email=email,
            #role=role,
         #   password=pw_hash,
            #created_at=created_at,
            #updated_at=updated_at

        #)

        #users.store()

#        return redirect(url_for('frontend.login'))
 #   return render_template('users/create.html',form=form)