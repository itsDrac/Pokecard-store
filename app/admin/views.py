from flask_admin.contrib.mongoengine import ModelView

class UserView(ModelView):
    column_filters = ['name']

    column_searchable_list = ('name', 'password')

class ProdView(ModelView):
    pass

class TypeView(ModelView):
    can_export = True
