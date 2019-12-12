from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from app import app, db, lm
from app.models.tables import User, Client
from app.models.forms import LoginForm, UserForm, ClientForm


@app.route("/cad_admin")
def cad_admin():
    return render_template('cad_admin.html')


@app.route("/cad_produto")
def cad_produto():
    return render_template('cad_produto.html')


@app.route("/cad_categoria")
def cad_categoria():
    return render_template('cad_categoria.html')


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
