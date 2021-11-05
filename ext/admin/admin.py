from flask_admin import Admin
from flask_admin.contrib.sqla.view import ModelView
from crg.ext.db import session, login_manager
from crg.ext.db.models import *
from flask_login import current_user

class UsuariosView(ModelView):

    column_exclude_list = ['password']
    def is_accessible(self):
        try:
            visible = current_user.admin
        except:
            visible = False
        return visible

class OrdemView(ModelView):
    form_excluded_columns = ['familia']
    form_args = {
    'name': {
        'label': 'Nome'
    }
}
    def is_accessible(self):
        try:
            visible = current_user.admin
        except:
            visible = False
        return visible

class FamiliaView(ModelView):
    form_excluded_columns = ['genero']
    def is_accessible(self):
        try:
            visible = current_user.admin
        except:
            visible = False
        return visible

class GeneroView(ModelView):
    form_excluded_columns = ['especie']
    def is_accessible(self):
        try:
            visible = current_user.admin
        except:
            visible = False
        return visible

class EspecieView(ModelView):
    #form_excluded_columns = ['coleta']
    def is_accessible(self):
        try:
            visible = current_user.admin
        except:
            visible = False
        return visible

class ColetorView(ModelView):
    #form_excluded_columns = ['coleta']
    def is_accessible(self):
        try:
            visible = current_user.admin
        except:
            visible = False
        return visible

class LocalView(ModelView):
    #form_excluded_columns = ['coleta']
    def is_accessible(self):
        try:
            visible = current_user.admin
        except:
            visible = False
        return visible

class ColetaView(ModelView):
    column_filters = ['coletor']
    can_view_details = True
    column_display_all_relations = True
    column_labels = dict(coletor='Coletores')
    column_list = ['codigo', 'data', 'especie', 'local']
    #inline_models = (Coletor,)
    def is_accessible(self):
        try:
            visible = current_user.admin
        except:
            visible = False
        return visible

class SolicitanteView(ModelView):
    form_excluded_columns = ['emprestimo']
    def is_accessible(self):
        try:
            visible = current_user.admin
        except:
            visible = False
        return visible

class EmprestimoView(ModelView):
    #form_excluded_columns = ['emprestimo']
    def is_accessible(self):
        try:
            visible = current_user.admin
        except:
            visible = False
        return visible

admin = Admin(name='CRG')
admin.add_view(UsuariosView(User, session))
admin.add_view(OrdemView(Ordem, session))
admin.add_view(FamiliaView(Familia, session))
admin.add_view(GeneroView(Genero, session))
admin.add_view(EspecieView(Especie, session))
admin.add_view(ColetorView(Coletor, session))
admin.add_view(LocalView(Local, session))
admin.add_view(ColetaView(Aves, session))
admin.add_view(SolicitanteView(Solicitante, session))
admin.add_view(EmprestimoView(Emprestimo, session))