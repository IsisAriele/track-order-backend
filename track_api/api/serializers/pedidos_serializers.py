from api.models import Pedido
from rest_framework import serializers


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["status", "updated_at", "created_at"]
        read_only_fields = ["updated_at", "created_at"]

    def validate_status(self, value):
        # Obter a lista de valores válidos de status a partir do modelo Pedido
        valid_statuses = Pedido.STATUSES.keys()
        if value not in valid_statuses:
            raise serializers.ValidationError(
                "Status inválido. Escolha um status válido."
            )
        return value
