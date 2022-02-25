from app.extinsions import admin
from app.user.models import User
from app.product.models import Product, Type
from app.admin.views import UserView, ProdView, TypeView

admin.add_view(UserView(User))
admin.add_view(ProdView(Product))
admin.add_view(TypeView(Type))
