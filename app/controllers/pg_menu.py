from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from app import app, db, lm
from app.models.tables import User, Client
from app.models.forms import LoginForm, UserForm, ClientForm, CategoryForm, ProductForm


@app.route("/admin")
def admin():
    return render_template('menu_admin.html')


@app.route("/produtos")
@app.route("/")
def produtos():
    return render_template('menu_produtos.html')


@app.route("/carrinho")
def carrinho():
    return render_template('menu_carrinho.html')


@app.route("/perfil")
def perfil():
    return render_template('menu_perfil.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Olá " + user.firstname + ", seu login foi realizado com sucesso!")
            if (user.status == 'admin'):
                return redirect(url_for("admin"))
            else:
                return redirect(url_for("produtos"))
        else:
            flash("Algum campo é inválido!")
    return render_template('menu_login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Você foi desconectado!")
    return redirect(url_for("produtos"))
