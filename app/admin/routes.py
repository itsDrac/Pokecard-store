from app.extinsions import admin
from app.user.models import User
from app.admin.views import UserView

admin.add_view(UserView(User))
