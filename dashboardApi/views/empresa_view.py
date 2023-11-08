from rest_framework import generics
from ..models.empresa import Empresa
from ..serializers.empresa_serializer import EmpresaSerializer


class EmpresaList(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
