from flask_restful import Resource, abort, reqparse
from flask import request, jsonify
from crg.ext.db import session
from crg.ext.db.models import *
from datetime import datetime
from .filters import filterEspecie, filterGenero, filterLocal

def filterDate(q, args):
    fromDate = datetime.strptime(args.get('fromDate'), '%d/%m/%Y').date() if 'fromDate' in args else None
    toDate = datetime.strptime(args.get('toDate'), '%d/%m/%Y').date() if 'toDate' in args else None
    if fromDate and toDate:
        q = q.filter(Peixes.data_coleta >= fromDate, Peixes.data_coleta <= toDate ) 
        return q
    elif fromDate:
        q = q.filter(Peixes.data_coleta >= fromDate)
        return q
    elif toDate:
        q = q.filter(Peixes.data_coleta <= toDate)
        return q
    return q

class Collection_Peixes(Resource):
    def get(self):
        args = request.args
        offset = args.get('offset') if 'offset' in args else 0
        limit = args.get('limit') if 'limit' in args else 10
        q = session.query(Peixes) 
        q = filterDate(q, args)
        q = filterEspecie(q, args)
        q = filterGenero(q, args)
        q = filterLocal(q, args)
        r = q.offset(offset).limit(limit).all()
        result = [i.json() for i in r]
        response = {'records': q.count(), 'start': offset, 'response': result }
        return jsonify(response)

class PeixesByCodigo(Resource):
    def get(self, codigo):
        q = session.query(Peixes).filter(Peixes.codigo == codigo).first()
        return jsonify(q.json())