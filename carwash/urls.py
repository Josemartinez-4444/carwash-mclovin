from django.contrib import admin
from django.urls import path
from dashboard.views import home, login_view
from clientes.views import lista_clientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login_view),
    path('clientes/', lista_clientes),
]