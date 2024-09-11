from api.serializers.pedidos_serializers import PedidoSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class PedidosView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            pedido = serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        pedidos = request.user.pedidos.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
