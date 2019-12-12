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
