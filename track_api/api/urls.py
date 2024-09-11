from api.views.pedidos_views import PedidosView
from api.views.users_views import LoginUserView, RegisterUserView
from django.urls import path

urlpatterns = [
    path("cadastro", RegisterUserView.as_view(), name="cadastro"),
    path("login", LoginUserView.as_view(), name="login"),
    path("pedidos", PedidosView.as_view(), name="criar-listar-pedidos"),
]
