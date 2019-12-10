from flask import current_app as app
from flask import render_template, flash, redirect, url_for, request
from . import app, db, bcrypt
from .forms import LoginForm, createAccount, PostForm, mailForm, forgotForm, passwordResetForm
from .models import User, Post
from flask_login import current_user, login_user, login_required
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse
from flask_bootstrap import Bootstrap
from flask_mail import Message, Mail
from itsdangerous import URLSafeTimedSerializer

Bootstrap(app)

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'stufftodocmpe131@gmail.com'
app.config["MAIL_PASSWORD"] = 'cmpe131sjsu'

mail.init_app(app)

@app.route('/')
@app.route('/index')
@login_required
def index():
    '''Main home page

        *login required*

        :return: Display all of user's Tasks
    '''
    post = Post.query.all()
    return render_template('index.html', user=current_user, post=post)

#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Login

        :return: Display the login page user to login to app
    '''
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        # look at first result first()
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # return to page before user got asked to login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    return render_template('LLogin.html', title='Sign in', form=form)

#______________________________________________________________________________

#logout
@app.route('/logout')
@login_required
def logout():
    '''Logout

    *login required*

    :return: Logs user out of account and redirected to login page
    '''
    logout_user()
    return redirect(url_for('index'))

#______________________________________________________________________________

#register
@app.route('/register', methods=['GET', 'POST'])
def register():
    '''Registration for new users

    :return: If user enters valid email, username, and password, user's credentials are saved to db
    '''
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = createAccount()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

#______________________________________________________________________________

#add task
@app.route('/add', methods =['GET','POST'])
@login_required
def add():
    '''Create a new task

    :return: Creates a new task that is saved in the db
    '''
    form = PostForm()
    if request.method == 'POST' :
        nameTitle = request.form.get('nameTitle')
        content = request.form.get('content')
        post = Post(nameTitle=nameTitle, content=content, complete=False, author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        flash('Successfully created a task!', 'success')
        return redirect(url_for('index'))
    return render_template('task.html', form=form, legend='Create Task', title='New Tasks')

#______________________________________________________________________________

#delete task
@app.route('/delete<int:id>')
@login_required
def delete(id):
    '''Delete task by id

        *login required*

        :return: Delete task by id
    '''
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

#______________________________________________________________________________

#edit task
@app.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    '''Edit task page

        *login required*

        :return: Get task data by id, check task's owner and if task's is writable
    '''
    post = Post.query.filter_by(id = id).first()
    form = PostForm()
    if request.method == 'POST':
            post.nameTitle = request.form.get('nameTitle')
            post.content =  request.form.get('content')
            post.complete = form.complete.data
            db.session.commit()
            flash('Successfully Edited', 'success')
            return redirect(url_for('index'))
    return render_template('task.html', title='Edit', legend='Edit Task', form=form, post=post)

#______________________________________________________________________________

#complete task
@app.route('/complete/<int:id>')
@login_required
def complete(id):
    ''' Mark task as complete

    :param id:
    :return: Get task by id, classify as complete
    '''
    post = Post.query.filter_by(id = id).first()
    post.complete = True
    db.session.commit()
    return redirect(url_for('index'))

#______________________________________________________________________________

#send email message

@app.route('/mail', methods=['GET', 'POST'])
def mes():
    '''Send message to other user's via email

    :return: Form to fill in a message and send via Flask mail
    '''
    form = mailForm()
    if request.method == "POST":
        message = Message(form.subject.data, sender=current_user.email, recipients=[form.email.data], )
        message.body = """
            StuffToDo
              
                %s sent a mesage.
                Content: 
                    %s 
            """ % (
            current_user.email,
            form.content.data,
        )
        mail.send(message)
        flash("Congratulation! Your message has been sent successfully!", "success")
        return redirect(url_for("index"))
    return render_template('mail.html', title="Send Message", legend="Send Message", form =form, url='mes')

#______________________________________________________________________________

#share task

@app.route('/share/<int:id>', methods=['GET', 'POST'])
def share(id):
    '''Share tasks with other users

    :param id:
    :return: User shares a task with other users through email via Flask mail
    '''
    form = mailForm()
    post = Post.query.filter_by(id = id).first()
    if request.method == "POST":
        shareTask = Message(subject='Task Shared', sender=current_user.email, recipients=[form.email.data], )
        shareTask.body = """
            StuffToDo
              
                %s shared a task.
                Content: 
                    Name of Task: %s
                    Task Description: %s 
            """ % (
            current_user.email,
            post.nameTitle,
            post.content,
        )
        mail.send(shareTask)
        flash("Congratulation! Your message has been sent successfully!", "success")
        return redirect(url_for('index'))
    return render_template('mail.html', title='Share Task', legend='Share Task', form=form, post=post, url='share')

#______________________________________________________________________________

def sendResetEmail(user):
    '''Email with reset link

    :param user:
    :return: An email is sent to user after requesting a reset link
    '''
    token = user.getResetToken()
    msg = Message('Password Reset Request', sender='noreply@stuffToDo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('resetToken', token=token, _external=True)}

If you did not make this request, ignore this email and no changes will be made.
    '''

@app.route('/reset_password', methods=['GET', 'POST'])
def resetRequest():
    '''Forgot password option on login

    :return: Redirects user to a template, prompts user to enter an email to reset password
    '''
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forgotForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        sendResetEmail(user)
        flash('An email has been sent with instructions to reset your password.', 'success')
        return redirect(url_for('login'))
    return render_template('forgotPassword.html', title='Reset Password', form=form)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def resetToken(token):
    '''Generates a link for reset

    :param token:
    :return: Link is sent via email to user who requests a reset, only valid for 30 mins. Uses a token generated by getResetToken().
    '''
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verifyResetToken(token)
    if user is None:
        flash('That is an invalid or expired token', 'danger')
        return redirect(url_for('resetRequest'))
    form = passwordResetForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Congratulations, your password has been updated!', 'success')
        return redirect(url_for('login'))
    return render_template('resetToken.html', title='Reset Password', form=form)

#_________________________________________________________________________________________

if __name__ =='__main__':
    db.create_all()
    app.run(debug=True)

