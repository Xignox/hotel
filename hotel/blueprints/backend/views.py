from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from blueprints.backend.model.reservations.models import Reservation
from blueprints.backend.model.roles.models import Role
from blueprints.backend.model.rooms.models import Rooms
from blueprints.backend.model.payments.models import Payment
from blueprints.backend.model.users.models import User
from blueprints.backend.form.rooms.forms import RoomsForm
from blueprints.backend.form.reservations.forms import ReservationForm
from blueprints.backend.form.roles.forms import RoleForm
from blueprints.backend.form.users.forms import UserForm,SearchForm

from passlib.hash import sha256_crypt
from extension import db
from sqlalchemy import or_

backend = Blueprint('backend', __name__, template_folder="templates")


@backend.route('/')
def index():
    return 'WELCOME TO SSCR-dC Hotel'  

@backend.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html')  

@backend.route('/payments')
def payments():
    return render_template('payments/payments.html') 

@backend.route('/users', methods=['GET', 'POST'])
def users_index():
    form = SearchForm()
    users = User.query.all()

    if form.validate_on_submit():

        search = form.search.data
        users = User.query.filter(or_(
            User.firstname.like('%'+search+'%'),
            User.lastname.like('%'+search+'%'),
            User.mobile.like('%'+search+'%'),
            User.role.like('%'+search+'%'),
            User.email.like('%'+search+'%'))).all()

    return render_template('users/index.html', form = form, users=users)

@backend.route('/users/create',methods=['GET','POST'])
def users_create():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        middlename = request.form.get('middlename')
        address = request.form.get('address')
        mobile = request.form.get('mobile')
        email = request.form.get('email')
        role = request.form.get('role')
        password = request.form.get('password')
        pw_hash = sha256_crypt.encrypt(str(password))
        #created_at = request.form.get('created_at')
        #updated_at = request.form.get('updated_at')

        users = User (
            firstname=firstname,
            lastname=lastname,
            middlename=middlename,
            address=address,
            mobile=mobile,
            email=email,
            role=role,
            password=pw_hash,
            #created_at=created_at,
            #updated_at=updated_at

        )

        users.store()

        return redirect(url_for('backend.users_index'))
    return render_template('users/create.html',form=form)

@backend.route('/users/<string:id>', methods=['GET'])
def users_show(id):
    users = User.query.filter_by(id=id).first() 

    return render_template('users/show.html', users=users)

@backend.route('/users/<string:id>/edit', methods=['GET','POST'])
def users_edit(id):
    form = UserForm(request.form)
    users = User.query.filter_by(id=id).first()

    if request.method == 'POST' and form.validate():

        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        middlename = request.form.get('middlename')
        address = request.form.get('address')
        mobile = request.form.get('mobile')
        email = request.form.get('email')
        role = request.form.get('role')
        password = request.form.get('password')
        pw_hash = sha256_crypt.encrypt(str(password))
        method = request.form.get('_method')
        users = User.query.get(id)
        

        if method == 'PUT':
            users.update (firstname=firstname,lastname=lastname,middlename=middlename,address=address, mobile=mobile,email=email,role=role,password=password)

        return redirect(url_for('backend.users_index'))

    return render_template('users/edit.html', form=form,users=users)

@backend.route('/users/<string:id>/delete', methods=['GET','POST'])
def usersdelete(id):
    users = User.query.get(id) 
    db.session.delete(users)
    db.session.commit()
    return redirect(url_for('backend.users_index'))

        
@backend.route('/roles', methods=['GET', 'POST'])
def roles_index():
    form = SearchForm()
    roles = Role.query.all()
    if form.validate_on_submit():

        search = form.search.data
        roles = Role.query.filter((Role.name.like('%'+search+'%'))).all()

    return render_template('roles/index.html',form=form,roles=roles)


@backend.route('/roles/create',methods=['GET','POST'])
def roles_create():
    form = RoleForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form.get('name')
        description = request.form.get('description')

        roles = Role(name=name,description=description)
        roles.store()
        return redirect(url_for('backend.roles_index'))

    return render_template('roles/create.html', form=form)

@backend.route('/roles/<string:id>', methods=['GET'])
def roles_show(id):
    roles = Role.query.filter_by(id=id).first()

    return render_template('roles/show.html', roles=roles)

@backend.route('/roles/<string:id>/edit', methods=['GET','POST'])
def roles_edit(id):
    form = RoleForm(request.form)
    roles = Role.query.filter_by(id=id).first()

    if request.method == 'POST' and form.validate():

        name = request.form.get('name')
        description = request.form.get('description')
        method = request.form.get('_method')
        roles = Role.query.get(id)

        if method == 'PUT':
            roles.update(name=name, description=description)

        return redirect(url_for('backend.roles_index'))

    return render_template('roles/edit.html',form=form, roles=roles)

@backend.route('/roles/<string:id>/delete', methods=['GET', 'POST'])
def rolesdelete(id):
    roles = Role.query.get(id) 
    db.session.delete(roles)
    db.session.commit()
    return redirect(url_for('backend.roles_index'))

@backend.route('/reservations',methods=['GET','POST'])
def reservations_index():
    form = SearchForm(request.form)
    reservations = Reservation.query.all()
    if form.validate_on_submit():
        search = form.search.data
        reservations = Reservation.query.filter(or_(
            Reservation.users_id.like('%'+search+'%'),
            Reservation.rooms_id.like('%'+search+'%'))).all()

    return render_template('reservations/index.html',form=form,reservations=reservations)

@backend.route('/reservations/create',methods=['GET','POST'])
def reservations_create():
    form = ReservationForm(request.form)
    users = User.query.all()
    rooms = Rooms.query.all()
   

    if request.method == 'POST' and form.validate():
        users_id = request.form.get('users_id')
        rooms_id = request.form.get('rooms_id')
        date_in = request.form.get('date_in')
        date_out = request.form.get('date_out')
        child_count = request.form.get('child_count')
        adult_count= request.form.get('adult_count')

        reservations = Reservation (
            users_id=users_id, 
            rooms_id=rooms_id,
            date_in = date_in,
            date_out=date_out,
            child_count=child_count, 
            adult_count=adult_count
            
        )
        reservations.store()

        return redirect(url_for('backend.reservations_index'))

    return render_template('reservations/create.html',form=form,users=users,rooms=rooms)    

@backend.route('/reservations/<string:id>', methods=['GET'])
def reservations_show(id):
    reservations = Reservation.query.filter_by(id=id).first()

    return render_template('reservations/show.html', reservations=reservations)

@backend.route('/reservations/<string:id>/edit', methods=['GET','POST'])
def reservations_edit(id):
    form = ReservationForm(request.form)
    users = Users.query.all()
    rooms = Rooms.query.all()
    reservations = Reservation.query.filter_by(id=id).first()

    if request.method == 'POST' and form.validate():

        users_id = request.form.get('users_id')
        rooms_id = request.form.get('rooms_id')
        date_in = request.form.get('date_in')
        date_out = request.form.get('date_out')
        child_count = request.form.get('child_count')
        adult_count= request.form.get('adult_count')
        method = request.form.get('_method')
        reservations = Reservation.query.get(id)

        if method == 'PUT':
            reservations.update (
                users_id=users_id, 
                rooms_id=rooms_id,
                date_in = date_in,
                date_out=date_out,
                child_count=child_count, 
                adult_count=adult_count
            )

        return redirect(url_for('backend.reservations_index'))

    return render_template('reservations/edit.html',form=form, reservations=reservations,rooms=rooms,users=users)

@backend.route('/reservations/<string:id>/delete', methods=['GET', 'POST'])
def reservationsdelete(id):
    reservations = Reservation.query.get(id) 
    db.session.delete(reservations)
    db.session.commit()
    return redirect(url_for('backend.reservations_index'))

@backend.route('/rooms', methods=['GET', 'POST'])
def rooms_index():
    form = SearchForm()
    rooms = Rooms.query.all()

    if form.validate_on_submit():

        search = form.search.data
        rooms = Rooms.query.filter(or_(
            Rooms.room_type.like('%'+search+'%'),
            Rooms.status.like('%'+search+'%'),
            Rooms.price.like('%'+search+'%'))).all()

    return render_template('rooms/index.html', form = form, rooms=rooms)

@backend.route('/rooms/create',methods=['GET','POST'])
def rooms_create():
    form = RoomsForm(request.form)
    if request.method == 'POST' and form.validate():

        room_type = request.form.get('room_type')
        status = request.form.get('status')
        price = request.form.get('price')
        

        rooms = Rooms (
           
            room_type = room_type,
            status = status,
            price = price
        )

        rooms.store()

        return redirect(url_for('backend.rooms_index'))        
    return render_template('rooms/create.html',form=form)
    
@backend.route('/rooms/<string:id>', methods=['GET'])
def rooms_show(id):
    rooms = Rooms.query.filter_by(id=id).first()
    #user = Map(
      #  style="width: 100%;height: 500px;",
       # identifier="user",
       # varname="user",
        #lat=14.4348822,
        #lng=120.9472825,
        #markers=[ [terminals.latitude,terminals.longitude,terminals.address]])

    return render_template('rooms/show.html', rooms=rooms)

@backend.route('/rooms/<string:id>/edit', methods=['GET','POST'])
def rooms_edit(id):
    form = RoomsForm(request.form)
    rooms = Rooms.query.filter_by(id=id).first()

    if request.method == 'POST' and form.validate():

        room_type = request.form.get('room_type')
        status = request.form.get('status')
        price = request.form.get('price')
        method = request.form.get('_method')
        rooms = Rooms.query.get(id)

        if method == 'PUT':
            rooms.update (
            
                room_type=room_type, 
                status=status, 
                price=price
                
            )

        return redirect(url_for('backend.rooms_index'))

    return render_template('rooms/edit.html', form=form,rooms=rooms)

@backend.route('/rooms/<string:id>/delete', methods=['GET', 'POST'])
def roomsdelete(id):
    rooms = Rooms.query.get(id) 
    db.session.delete(rooms)
    db.session.commit()
    return redirect(url_for('backend.rooms_index'))



@backend.route('/payments/<string:id>', methods=['GET'])
def payments_show(id):

    payments = Payment.query.filter_by(id=id).first()

    reservations = Reservation.query.filter_by(id=id).first()

    return render_template('payments/show.html', payments=payments, reservations=reservations)


@backend.route('/payments/<string:id>/edit', methods=['GET'])
def payments_edit(id):

    payments = Payment.query.filter_by(id=id).first()
    return render_template('/payments/edit.html', payments=payments)

@backend.route('/payments/<string:id>', methods=['POST'])
def payments_update_or_destroy(id):

    reserve_id = request.form.get('reserve_id')
    first
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    mode = request.form.get('mode')
    method = request.form.get('_method')
    payments = Payment.query.get(id)

    if method == 'PUT':
        payments.update (
            reserve_id=reserve_id, 
            firstname=firstname, 
            lastname=lastname, 
            mode=mode
        )
    return redirect(url_for('backend.payments'))

@backend.route('/payments/<string:id>/delete', methods=['GET', 'POST'])
def delete(id):
    payments = Payment.query.get(id) 
    db.session.delete(payments)
    db.session.commit()
    return redirect(url_for('backend/payments'))