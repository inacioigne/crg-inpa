from sqlalchemy import Table, Column, Integer, String, Boolean, Date, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.event import listen
import datetime
from crg.ext.db import Base, login_manager, session
#from ext.db import Base, login_manager, session
import bcrypt
from sqlalchemy import event
from flask_login import UserMixin

ColetaAves = Table('coletaAves', Base.metadata,
    Column('idColetor', Integer, ForeignKey('coletor.id')),
    Column('idAves', Integer, ForeignKey('aves.id')))

ColetaPeixes = Table('coletaPeixes', Base.metadata,
    Column('idColetor', Integer, ForeignKey('coletor.id')),
    Column('idPeixes', Integer, ForeignKey('peixes.id')))

ColetaHerpto = Table('coletaHerpto', Base.metadata,
    Column('idColetor', Integer, ForeignKey('coletor.id')),
    Column('idHerpto', Integer, ForeignKey('herpto.id')))

class Aves(Base):
    __tablename__ = 'aves'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(15))
    data_coleta = Column(Date)
    data_preparacao = Column(Date)
    conservacao = Column(String(100))
    metodo = Column(String(50))
    sexo = Column(String(50))
    expedicao = Column(String(50))
    musculo = Column(Boolean)
    coracao = Column(Boolean)
    figado = Column(Boolean)
    sangue = Column(Boolean)
    preservacao = Column(String(50))
    emprestado = Column(Boolean, default=False)
    observacao = Column(Text(200))
    
    idEspecie = Column(Integer, ForeignKey('especie.id'))
    idLocal = Column(Integer, ForeignKey('local.id'))
    idEmprestimo = Column(Integer, ForeignKey('emprestimo.id'))
    idUser = Column(Integer, ForeignKey('user.id'))
    
    especie = relationship('Especie', back_populates='aves')
    coletor = relationship('Coletor', secondary = ColetaAves, back_populates='aves')
    local = relationship('Local', back_populates='aves')
    emprestimo = relationship('Emprestimo', back_populates='aves')
    user = relationship('User', back_populates='aves')

    def json(self):

       return {
            'id': self.id,
            'codigo':self.codigo,
            'data': self.data_coleta.strftime('%d/%m/%Y') if isinstance(self.data_coleta, datetime.date) else None,
            'preparacao': self.data_preparacao.strftime('%d/%m/%Y') if isinstance(self.data_preparacao, datetime.date) else None,
            'conservacao': self.conservacao,
            'metodo': self.metodo,
            'sexo': self.sexo,
            'expedicao': self.expedicao,
            'musculo': self.musculo,
            'coracao': self.coracao,
            'figado': self.figado,
            'sangue': self.sangue,
            'preservacao': self.preservacao,
            'emprestado': self.emprestado,
            'observacao': self.observacao,
            'genero': self.especie.genero.nome,
            'especie':self.especie.nome,
            'local': self.local.nome,
            'latitude': self.local.latitude,
            'longitude': self.local.longitude,
            'coletores': [str(i) for i in self.coletor]
        }

    def __repr__(self):
        return self.codigo

class Peixes(Base):
    __tablename__ = 'peixes'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(15))
    data_coleta = Column(Date)
    caixa = Column(String(50))
    voucher = Column(String(50))
    drenagem = Column(String(100))
    subdrenagem = Column(String(100))
    local_pesca = Column(String(200))
    responsavel = Column(String(100))
    comprimento_padrao = Column(String(50))
    emprestado = Column(Boolean, default=False)
    observacao = Column(Text(200))
    
    idEspecie = Column(Integer, ForeignKey('especie.id'))
    idLocal = Column(Integer, ForeignKey('local.id'))
    idEmprestimo = Column(Integer, ForeignKey('emprestimo.id'))
    idUser = Column(Integer, ForeignKey('user.id'))
    
    especie = relationship('Especie', back_populates='peixes')
    coletor = relationship('Coletor', secondary = ColetaPeixes, back_populates='peixes')
    local = relationship('Local', back_populates='peixes')
    emprestimo = relationship('Emprestimo', back_populates='peixes')
    user = relationship('User', back_populates='peixes')

    def json(self):

       return {
            'id': self.id,
            'codigo':self.codigo,
            'data': self.data_coleta.strftime('%d/%m/%Y') if isinstance(self.data_coleta, datetime.date) else None,
            'caixa': self.caixa,
            'voucher': self.voucher,
            'drenagem': self.drenagem,
            'subdrenagem': self.subdrenagem,
            'local_pesca': self.local_pesca,
            'responsavel': self.responsavel,
            'comprimento_padrao': self.comprimento_padrao,
            'emprestado': self.emprestado,
            'observacao': self.observacao,
            'genero': self.especie.genero.nome,
            'especie':self.especie.nome,
            'local': self.local.nome,
            'latitude': self.local.latitude,
            'longitude': self.local.longitude,
            'coletores': [str(i) for i in self.coletor]
        }

    def __repr__(self):
        return self.codigo

class Herpto(Base):
    __tablename__ = 'herpto'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(15))
    inpa_h = Column(String(50))
    data_coleta = Column(Date)
    emprestado = Column(Boolean, default=False)
    observacao = Column(Text(200))

    idEspecie = Column(Integer, ForeignKey('especie.id'))
    idLocal = Column(Integer, ForeignKey('local.id'))
    idEmprestimo = Column(Integer, ForeignKey('emprestimo.id'))
    idUser = Column(Integer, ForeignKey('user.id'))

    especie = relationship('Especie', back_populates='herpto')
    coletor = relationship('Coletor', secondary = ColetaHerpto, back_populates='herpto')
    local = relationship('Local', back_populates='herpto')
    emprestimo = relationship('Emprestimo', back_populates='herpto')
    user = relationship('User', back_populates='herpto')

    def json(self):

       return {
            'id': self.id,
            'codigo':self.codigo,
            'data': self.data_coleta.strftime('%d/%m/%Y') if isinstance(self.data_coleta, datetime.date) else None,
            'emprestado': self.emprestado,
            'observacao': self.observacao,
            'genero': self.especie.genero.nome,
            'especie':self.especie.nome,
            'local': self.local.nome if self.local else None,
            'latitude': self.local.latitude if self.local else None,
            'longitude': self.local.longitude if self.local else None,
            'coletores': [str(i) for i in self.coletor]
        }

    def __repr__(self):
        return self.codigo

class Especie(Base):
    __tablename__ = 'especie'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    nomeComun = Column(String(50))

    idGenero = Column(Integer, ForeignKey('genero.id'))

    genero = relationship('Genero', back_populates='especie')
    aves = relationship('Aves', back_populates='especie')
    peixes = relationship('Peixes', back_populates='especie')
    herpto = relationship('Herpto', back_populates='especie')

    def __repr__(self):
        return str(self.nome)

class Genero(Base):
    __tablename__ = 'genero'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))

    idFamilia = Column(Integer, ForeignKey('familia.id'))

    familia = relationship('Familia', back_populates='genero')
    especie = relationship('Especie', back_populates='genero')

    def __repr__(self):
        return str(self.nome)

class Familia(Base):
    __tablename__ = 'familia'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))

    idOrdem = Column(Integer, ForeignKey('ordem.id'))

    ordem = relationship('Ordem', back_populates='familia')
    genero = relationship('Genero', back_populates='familia')

    def __repr__(self):
        return str(self.nome)

class Ordem(Base):
    __tablename__ = 'ordem'
    id = Column(Integer, primary_key=True)
    nome = Column(String(20), unique=True)

    familia = relationship('Familia', back_populates='ordem')

    def __repr__(self):
        return str(self.nome)

class Coletor(Base):
    __tablename__ = 'coletor'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))

    aves = relationship('Aves', secondary = ColetaAves, back_populates='coletor')
    peixes = relationship('Peixes', secondary = ColetaPeixes, back_populates='coletor')
    herpto = relationship('Herpto', secondary = ColetaHerpto, back_populates='coletor')

    def __repr__(self):
        return self.nome

class Local(Base):
    __tablename__ = 'local'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    pais = Column(String(50))
    estado = Column(String(50))
    municipio = Column(String(50))
    latitude = Column(String(50))
    longitude = Column(String(50))
    procedencia_coordenada = Column(String(30))

    aves = relationship('Aves', back_populates='local')
    peixes = relationship('Peixes', back_populates='local')
    herpto = relationship('Herpto', back_populates='local')

    def __repr__(self):
        return self.nome

#MODEL EMPRESTIMO
class Emprestimo(Base):
    __tablename__ = 'emprestimo'
    id = Column(Integer, primary_key=True)
    data_emprestimo = Column(Date)
    date_devolucao = Column(Date)
    status = Column(String(20))

    idUser = Column(Integer, ForeignKey('user.id'))

    aves = relationship('Aves', back_populates='emprestimo')
    peixes = relationship('Peixes', back_populates='emprestimo')
    herpto = relationship('Herpto', back_populates='emprestimo')
    solicitante = relationship('Solicitante', back_populates='emprestimo')
    user = relationship('User', back_populates='emprestimo')

class Solicitante(Base):
    __tablename__ = 'solicitante'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30))
    instituicao = Column(String(50))
    email = Column(String(30))
    telefone = Column(String(15))
    endereco = Column(String(50))
    cep = Column(String(10))
    cidade = Column(String(20))
    estado = Column(String(20))
    pais = Column(String(20))

    idEmprestimo = Column(Integer, ForeignKey('emprestimo.id'))

    emprestimo = relationship('Emprestimo', back_populates='solicitante')


#MODEL USER
class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(15), unique=True)
    email = Column(String(30), unique=True)
    password = Column(String(255))
    admin = Column(Boolean, default=False)

    aves = relationship('Aves', back_populates='user')
    peixes = relationship('Peixes', back_populates='user')
    herpto = relationship('Herpto', back_populates='user')
    emprestimo = relationship('Emprestimo', back_populates='user')

    def __repr__(self):
        return str(self.username)

@event.listens_for(User.password, 'set', retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        pwhash = bcrypt.hashpw(value.encode('utf8'), bcrypt.gensalt())
        return pwhash.decode('utf8')
    return value
