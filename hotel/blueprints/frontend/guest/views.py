from flask import Blueprint, jsonify, render_template, request, redirect, url_for,session,flash
from extension import db
import os

guest = Blueprint('guest', __name__, template_folder="templates")

#@guest.route('/guest')
#def guest():
	
#	return(asdfghjkl)

@guest.route('/guest')
@login_required
def guest():

	return render_template('/guest/guest.html', rooms=rooms)