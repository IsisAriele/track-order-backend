from api.views.users_views import RegisterUserView, LoginUserView
from django.urls import path

urlpatterns = [
    path("cadastro", RegisterUserView.as_view(), name="cadastro"),
    path("login", LoginUserView.as_view(), name="login"),
]
