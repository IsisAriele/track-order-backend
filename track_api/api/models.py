from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Pedido(BaseModel):
    STATUSES = {
        "EM_ANALISE": "Em análise",
        "ACEITO": "Aceito",
        "EM_SEPARACAO": "Em separação",
        "CANCELADO": "Cancelado",
        "EM_PREPARO": "Em preparo",
        "EM_TRANSITO": "Em trânsito",
        "ENTREGUE": "Entregue",
    }

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="pedidos")
    status = models.CharField(
        max_length=255,
        choices=STATUSES,
        default=STATUSES["EM_ANALISE"],
    )

    def __str__(self):
        return f"{self.id} - {self.user} - ({self.created_at})"
