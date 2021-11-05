from flask import Blueprint
from flask_restful import Api
from .resources.aves import *
from .resources.peixes import *
from .resources.herpto import *

bp_api = Blueprint(
    'rest_api',
    __name__,
    url_prefix='/api/'
) 

api = Api(bp_api)
#AVES
api.add_resource(Coleta_Aves, 'aves')
api.add_resource(AvesByCodigo, 'aves/<string:codigo>')
#PEIXES
api.add_resource(Collection_Peixes, 'peixes')
api.add_resource(PeixesByCodigo, 'peixes/<string:codigo>')
#HERPTO
api.add_resource(Collection_Herpto, 'herpto')
api.add_resource(HerptoByCodigo, 'herpto/<string:codigo>')
