from django.urls import path

from .views.index import index
from .views import *

urlpatterns = [
    path('empresa/', EmpresaList.as_view(), name='empresa-list'),
]