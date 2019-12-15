from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    status = db.Column(db.String)
    client = db.relationship('Client', uselist=False, backref='users')


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, firstname, lastname, email, username, password, status):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password
        self.status = status

    def __repr__(self):
        return "<User %r>" % self.username


class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    data_nasc = db.Column(db.String)
    cpf = db.Column(db.Integer, unique=True)
    estado = db.Column(db.String)
    cidade = db.Column(db.String)
    bairro = db.Column(db.String)
    rua = db.Column(db.String)
    numero = db.Column(db.Integer)
    complemento = db.Column(db.String)

    def get_id(self):
        return str(self.id)

    def __init__(self, user_id, data_nasc, cpf, estado, cidade, bairro, rua, numero, complemento):
        self.user_id = user_id
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.complemento = complemento


class Category(db.Model):
    __tablename__ = "categories"

    id_category = db.Column(db.Integer, primary_key=True)
    name_category = db.Column(db.String, unique=True)
    #products = db.relationship('Product', order_by="Product.id_product")
    products = db.relationship('Product', backref='categories', lazy=True)

    def get_id(self):
        return str(self.id_category)

    def __init__(self, name_category):
        self.name_category = name_category


class Product(db.Model):
    __tablename__ = "products"

    id_product = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id_category"), nullable=False)
    name_product = db.Column(db.String, unique=True)
    desc_product = db.Column(db.String)
    preco = db.Column(db.Integer)

    def get_id(self):
        return str(self.id_product)

    def __init__(self, category_id, name_product, desc_product, preco):
        self.category_id = category_id
        self.name_product = name_product
        self.desc_product = desc_product
        self.preco = preco


