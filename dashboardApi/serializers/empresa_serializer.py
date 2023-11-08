from rest_framework import serializers
from ..models.empresa import Empresa, fieldsEmpresa


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = fieldsEmpresa