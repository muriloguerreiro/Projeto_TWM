from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from app import app, db, lm
from app.models.tables import User, Client, Category, Product
from app.models.forms import LoginForm, UserForm, ClientForm, CategoryForm, ProductForm


@app.route("/cad_admin", methods=['GET', 'POST'])
def cad_admin():
    form = UserForm()
    i = User(form.firstname.data, form.lastname.data, form.email.data, form.username.data, form.password.data, "administrador")
    if form.validate_on_submit():
        db.session.add(i)
        db.session.commit()
        flash('Administrador cadastrado com sucesso!')
        return redirect(url_for("admin"))
    return render_template('cad_admin.html', form=form)


@app.route("/cad_categoria", methods=['GET', 'POST'])
def cad_categoria():
    form = CategoryForm()
    i = Category(form.name_category.data)
    if form.validate_on_submit():
        db.session.add(i)
        db.session.commit()
        flash('Categoria cadastrada com sucesso!')
        return redirect(url_for("admin"))
    return render_template('cad_categoria.html', form=form)


@app.route("/cad_produto", methods=['GET', 'POST'])
def cad_produto():
    form = ProductForm()
    i = Product(form.category_id.data, form.name_product.data, form.desc_product.data, form.preco.data)
    if form.validate_on_submit():
        db.session.add(i)
        db.session.commit()
        flash('Produto cadastrado com sucesso!')
        return redirect(url_for("admin"))
    return render_template('cad_produto.html', form=form)


@app.route("/list_admin")
def list_admin():
    return render_template('list_admin.html')


@app.route("/list_cliente")
def list_cliente():
    return render_template('list_cliente.html')


@app.route("/list_produto")
def list_produto():
    return render_template('list_produto.html')


@app.route("/list_categoria")
def list_categoria():
    return render_template('list_categoria.html')
