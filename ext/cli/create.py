from ext.db import Base, session, engine
from ext.db.models import *
from datetime import datetime
import pandas as pd

def create_user():

    user = User(
        username = 'admin',
        email = 'admin@email.com',
        password = '8486',
        admin = True
    )

    session.add(user)
    session.commit()

def create_Aves(df):

    for index, row in df.iterrows():
        print(index)

        coleta = Aves(
            codigo = row.codigo,
            data_coleta = datetime.strptime(row.data_coleta, '%d/%m/%Y').date() if isinstance(row.data_coleta, str) else None,
            data_preparacao = datetime.strptime(row.data_preparacao, '%d/%m/%Y').date() if isinstance(row.data_preparacao, str) else None,
            conservacao = row.conservacao if isinstance(row.conservacao, str) else None,
            metodo = row.metodo_coleta if isinstance(row.metodo_coleta, str) else None,
            sexo = row.sexo if isinstance(row.sexo, str) else None,
            expedicao = row.expedicao if isinstance(row.expedicao, str) else None,
            musculo = True if row.musculo == 'X' else False,
            coracao = True if row.coracao == 'X' else False,
            figado = True if row.figado == 'X' else False,
            sangue = True if row.sangue == 'X' else False,
            preservacao = row.preservacao if isinstance(row.preservacao, str) else None,
            observacao = row.observacoes if isinstance(row.observacoes, str) else None
        )

        #LOCAL
        if isinstance(row.local, str):

            local = session.query(Local).filter_by(nome = row.local).first()
            if local:
                coleta.local = local
            else:
                local = Local(
                    nome = row.local,
                    estado = row.estado if isinstance(row.estado, str) else None,
                    latitude = row.latitude if not pd.isna(row.latitude) else None,
                    longitude = row.longitude if not pd.isna(row.longitude) else None
                )
                coleta.local = local

        #COLETOR
        if isinstance(row.coletor, str):
            coletores = row.coletor.split(';')
            for c in coletores:
                coletor = session.query(Coletor).filter_by(nome = c).first()
                if coletor:
                    coleta.coletor.append(coletor)
                else:
                    coletor = Coletor(nome = c)
                    coleta.coletor.append(coletor)

        #ESPECIE
        especie = session.query(Especie).filter_by(nome = row.especie).first()
        if especie:
            coleta.especie = especie
        else:
            especie = Especie(nome = row.especie if isinstance(row.especie, str) else None)

            #GENERO
            genero = session.query(Genero).filter_by(nome = row.genero).first()
            if genero:
                especie.genero = genero
                coleta.especie = especie
            else:
                genero = Genero(nome = row.genero if isinstance(row.genero, str) else None)
                especie.genero = genero
                coleta.especie = especie
        
        session.add(coleta)
        session.commit()
        
def create_Peixes(df):

    for index, row in df.iterrows():
        print(index)

        coleta = Peixes(
            codigo = row.codigo,
            data_coleta = datetime.strptime(row.data_coleta, '%d/%m/%Y').date() if isinstance(row.data_coleta, str) else None,
            caixa = row.caixa if isinstance(row.caixa, str) else None,
            voucher = row.voucher if isinstance(row.voucher, str) else None,
            drenagem = row.drenagem if isinstance(row.drenagem, str) else None,
            subdrenagem = row.subdrenagem if isinstance(row.subdrenagem, str) else None,
            local_pesca = row.local_pesca if isinstance(row.local_pesca, str) else None,
            responsavel = row.responsavel if isinstance(row.responsavel, str) else None,
            comprimento_padrao = row.comprimento_padrao if isinstance(row.comprimento_padrao, str) else None,
            observacao = row.observacoes if isinstance(row.observacoes, str) else None
        )
        #LOCAL
        if isinstance(row.local_coleta, str):

            local = session.query(Local).filter_by(nome = row.local_coleta).first()
            if local:
                coleta.local = local
            else:
                local = Local(
                    nome = row.local_coleta if isinstance(row.local_coleta, str) else None,
                    pais = row.pais if isinstance(row.pais, str) else None,
                    estado = row.estado if isinstance(row.estado, str) else None,
                    latitude = row.latitude if not pd.isna(row.latitude) else None,
                    longitude = row.longitude if not pd.isna(row.longitude) else None
                )
                coleta.local = local

        #COLETOR
        if isinstance(row.coletores, str):
            coletores = row.coletores.split(';')
            for c in coletores:
                coletor = session.query(Coletor).filter_by(nome = c).first()
                if coletor:
                    coleta.coletor.append(coletor)
                else:
                    coletor = Coletor(nome = c)
                    coleta.coletor.append(coletor)

        #ESPECIE
        e = row.especie if isinstance(row.especie, str) else None
        if e:
            especie = session.query(Especie).filter_by(nome = e).first()
            if especie:
                coleta.especie = especie
            else:
                especie = Especie(nome = e)
                coleta.especie = especie
                #GENERO
                g = row.genero if isinstance(row.genero, str) else None
                if g:
                    genero = session.query(Genero).filter_by(nome = g).first()
                    if genero:
                        especie.genero = genero
                    else:
                        genero = Genero(nome = row.genero)
                        especie.genero = genero
                        #FAMILIA
                        f = row.familia if isinstance(row.familia, str) else None
                        if f:
                            familia = session.query(Familia).filter_by(nome = f).first()
                            if familia:
                                genero.familia = familia
                            else:
                                familia = Familia(nome = f)
                                genero.familia = familia
                                #ORDEM
                                ordem = session.query(Ordem).filter_by(nome = row.ordem).first()
                                if ordem:
                                    familia.ordem = ordem
                                else:
                                    ordem = Ordem(nome = row.ordem)
                                    familia.ordem = ordem
                
        session.add(coleta)
        session.commit()

def create_Herpto(df):

    for index, row in df.iterrows():
        print(index)

        coleta = Herpto(
            codigo = row.codigo,
            inpa_h = row.inpa_h if isinstance(row.inpa_h, str) else None,
            data_coleta = datetime.strptime(row.data_coleta, '%d/%m/%Y').date() if isinstance(row.data_coleta, str) else None,
            observacao = row.observacao if isinstance(row.observacao, str) else None
        )

        #LOCAL
        if isinstance(row.local, str):

            local = session.query(Local).filter_by(nome = row.local).first()
            if local:
                coleta.local = local
            else:
                local = Local(
                    nome = row.local,
                    estado = row.estado if isinstance(row.estado, str) else None,
                    latitude = row.latitude if not pd.isna(row.latitude) else None,
                    longitude = row.longitude if not pd.isna(row.longitude) else None
                )
                coleta.local = local

        #COLETOR
        if isinstance(row.coletor, str):
            coletores = row.coletor.split(';')
            for c in coletores:
                coletor = session.query(Coletor).filter_by(nome = c).first()
                if coletor:
                    coleta.coletor.append(coletor)
                else:
                    coletor = Coletor(nome = c)
                    coleta.coletor.append(coletor)

        #ESPECIE
        especie = session.query(Especie).filter_by(nome = row.especie).first()
        if especie:
            coleta.especie = especie
        else:
            especie = Especie(nome = row.especie if isinstance(row.especie, str) else None)

            #GENERO
            genero = session.query(Genero).filter_by(nome = row.genero).first()
            if genero:
                especie.genero = genero
                coleta.especie = especie
            else:
                genero = Genero(nome = row.genero if isinstance(row.genero, str) else None)
                especie.genero = genero
                coleta.especie = especie
        
        session.add(coleta)
        session.commit()
#aves = pd.read_csv('files/aves.csv')
#peixes = pd.read_csv('files/peixes.csv')
herpto = pd.read_csv('files/herpto.csv')

