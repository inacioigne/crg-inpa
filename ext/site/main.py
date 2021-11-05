from flask import flash, Blueprint, render_template, request, redirect, url_for
from crg.ext.db import session, login_manager
from crg.ext.form.forms import LoginForm, CreateAccountForm
from crg.ext.db.models import User
from flask_login import login_user, logout_user
import bcrypt
import requests
from crg.ext.email import mail
from flask_mail import Message



bp = Blueprint('main', __name__)

@bp.route('/acervo')
def aves():
    return render_template('search/aves.html')

@bp.route('/peixes')
def peixes():
    return render_template('search/peixes.html')

@bp.route('/herpto')
def herpto():
    return render_template('search/herpto.html')

@bp.route('/detalhesaves/<string:codigo>', methods=['GET', 'POST'])
def detalhesAves(codigo):
    r = requests.get('http://127.0.0.1:5000/api/aves/'+codigo).json()
    print(r)
    if request.method == "POST": 
        #fcodigo = request.form['fcodigo']
        #especie = request.form['fespecie']
        solicitante = request.form['fsolicitante']
        cargo = request.form['fcargo']
        fone = request.form['fFone']
        email = request.form['fEmail']
        institution = request.form['fInstitution']
        departamet = request.form['fdepartament']
        endereco = request.form['fEndereco']
        cep = request.form['fcep']
        cidade = request.form['fCidade']
        pais = request.form['fPais']
        comments = request.form['comments']

        message = Message('Solicitação de Empréstimo',
        recipients=['inacioigne@gmail.com'])

        message.html = '<div>\
                        <h1>Solicitação de Emprestimo</h1>\
                        <hr>\
                        <table style="border-collapse: collapse; font-size: 18px;" >\
                            <tr style="background: rgb(210, 217, 224); height: 50px;">\
                            <th style="border-bottom: solid 1px; border-right: solid 1px;">Código</th>\
                            <td style="border-bottom: solid 1px;"> <a href="http://127.0.0.1:5000/detalhesaves/INPA.A.001">{}</a> </td>\
                            </tr>\
                            <tr style="height: 50px;">\
                            <th style="border-bottom: solid 1px; border-right: solid 1px;">Espécie</th>\
                            <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                            <tr style="background: rgb(210, 217, 224); height: 50px;">\
                                <th style="border-bottom: solid 1px; border-right: solid 1px;">Solicitante</th>\
                                <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                            <tr style="height: 50px;">\
                                <th style="border-bottom: solid 1px; border-right: solid 1px;">Cargo</th>\
                                <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                            <tr style="background: rgb(210, 217, 224); height: 50px;">\
                                <th style="border-bottom: solid 1px; border-right: solid 1px;">Telefone</th>\
                                <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                            <tr style="height: 50px;">\
                                <th style="border-bottom: solid 1px; border-right: solid 1px;">Email</th>\
                                <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                            <tr style="background: rgb(210, 217, 224); height: 50px;">\
                                <th style="border-bottom: solid 1px; border-right: solid 1px;">Instituição</th>\
                                <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                            <tr style="height: 50px;">\
                                <th style="border-bottom: solid 1px; border-right: solid 1px;">Departamento</th>\
                                <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                            <tr style="background: rgb(210, 217, 224); height: 50px;">\
                                <th style="border-bottom: solid 1px; border-right: solid 1px;">Endereço</th>\
                                <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                            <tr style="height: 50px;">\
                                <th style="border-bottom: solid 1px; border-right: solid 1px;">Cep</th>\
                                <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                            <tr style="background: rgb(210, 217, 224); height: 50px;">\
                                <th style="border-bottom: solid 1px; border-right: solid 1px;">Cidade</th>\
                                <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                            <tr style="height: 50px;">\
                                <th style="border-bottom: solid 1px; border-right: solid 1px;">Pais</th>\
                                <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                            <tr style="background: rgb(210, 217, 224); height: 50px;">\
                                <th style="border-bottom: solid 1px; border-right: solid 1px;">Observações</th>\
                                <td style="border-bottom: solid 1px;">{}</td>\
                            </tr>\
                        </table>\
                    </div>'.format(r['codigo'],r['especie'],solicitante,cargo,fone,email,institution,departamet,endereco,cep,cidade,pais,comments)

        mail.send(message)

        success = "success"
      
        return render_template('details/details.html', response=r, success=success)

    return render_template('details/details.html', response=r)

@bp.route('/detalhespeixes/<string:codigo>')
def detalhesPeixes(codigo):
    r = requests.get('http://127.0.0.1:5000/api/peixes/'+codigo).json()
    return render_template('details/details.html', response=r)

@bp.route('/detalhes_herpto/<string:codigo>')
def detalhesHerpto(codigo):
    r = requests.get('http://127.0.0.1:5000/api/herpto/'+codigo).json()
    return render_template('details/details.html', response=r)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        # read form data
        username = request.form['username']
        password = request.form['password']
        # Locate user
        user = session.query(User).filter_by(username=username).first()
        # Check the password

        if user and bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8')):
            login_user(user)
            #flash(user.username)
            #return render_template('/admin/index.html')
            return redirect(url_for('admin.index'))
        # Something (user or pass) is not ok
        return render_template('/accounts/login.html', msg='Usuário ou Senha incorreta',form=login_form )
    return render_template('/accounts/login.html', form=login_form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    print(request.form)
    if 'register' in request.form:
        username = request.form['username']
        email = request.form['email']

        # Check usename exists
        user = session.query(User).filter_by(username=username).first()
        if user:
            return render_template( 'accounts/register.html',
                                    msg='Nome de usuário já cadastrado',
                                    success=False,
                                    form=create_account_form)
        # Check email exists
        userEmail = session.query(User).filter_by(email=email).first()
        if userEmail:
            return render_template( 'accounts/register.html',
                                    msg='Email já cadastrado',
                                    success=False,
                                    form=create_account_form)
        #criar usuário
        user = User(
            username = username,
            email = email,
            password = request.form['password']
        )
        print(user.email)

        session.add(user)
        session.commit()

        #return render_template( 'accounts/register.html',
        #                        msg='User created please <a href="/login">login</a>',
        #                        success=True,
        #                        form=create_account_form)
        return redirect(url_for('main.login'))
    else:
        return render_template( 'accounts/register.html', form=create_account_form)


@bp.route('/acervo')
def acervo():

    return render_template('acervo.html')

@bp.route('/coleta/<string:codigo>')
def coletaDetails(codigo):

    url = 'http://127.0.0.1:5000/api/aves/'+codigo
    response = requests.get(url).json()

    return render_template('details.html', response=response)


@bp.route('/modal')
def modal():

    return render_template('/details/modal.html')

@bp.route('/email')
def email():
    return render_template('/sendEmail.html')

@bp.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == "POST":
        codigo = request.form['codigo']
        especie = request.form['fespecie']
        #email = request.form['email']
        #subject = request.form['subject']
        #msg = request.form['message']

        message = Message('Solicitação de Empréstimo',
        recipients=['inacioigne@gmail.com'])

        message.body = especie
        mail.send(message)

        success = "Message Send"

        return render_template('result.html', success=success)
