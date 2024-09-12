from api.models import Pedido
from rest_framework import serializers

STATUSES = (
    ("EM_ANALISE", "Em análise"),
    ("ACEITO", "Aceito"),
    ("EM_SEPARACAO", "Em separação"),
    ("CANCELADO", "Cancelado"),
    ("EM_PREPARO", "Em preparo"),
    ("EM_TRANSITO", "Em trânsito"),
    ("ENTREGUE", "Entregue"),
)


class PedidoSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=STATUSES, default="EM_ANALISE")

    class Meta:
        model = Pedido
        fields = ["id", "status", "updated_at", "created_at"]
        read_only_fields = ["id", "updated_at", "created_at"]

    def validate_status(self, value):
        # Obter a lista de valores válidos de status a partir do modelo Pedido
        valid_statuses = Pedido.STATUSES.keys()
        if value not in valid_statuses:
            raise serializers.ValidationError(
                "Status inválido. Escolha um status válido."
            )
        return value
