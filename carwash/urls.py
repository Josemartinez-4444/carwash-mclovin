from django.contrib import admin
from django.urls import path
from dashboard.views import home, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login_view),
]