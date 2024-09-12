from api.models import Pedido
from api.serializers.pedidos_serializers import PedidoSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class PedidosView(APIView):
    # o is_authenticated é um decorator que verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            pedido = serializer.save(user=request.user) # request.user é o usuário autenticado (quem vem a partir do token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        pedidos = request.user.pedidos.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdatePedidoView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        try:
            pedido = request.user.pedidos.get(pk=pk)
        except Pedido.DoesNotExist:
            return Response(
                {"error": "Pedido não encontrado."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = PedidoSerializer(pedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
