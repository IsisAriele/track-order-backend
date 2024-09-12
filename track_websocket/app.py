import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import psycopg2
from psycopg2 import sql

# Configurações de conexão ao banco de dados PostgreSQL
DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

class PedidoService:
    def __init__(self, pedido_id):
        self.pedido_id = pedido_id

    def get_status(self):
        # Conectar ao banco de dados e buscar o status do pedido
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            cursor = conn.cursor()
            query = sql.SQL("SELECT status FROM api_pedido WHERE id = %s")
            cursor.execute(query, (self.pedido_id,))
            result = cursor.fetchone()
            conn.close()

            if result:
                return result[0]
            else:
                return "Pedido não encontrado"
        except Exception as e:
            return f"Erro ao buscar status: {str(e)}"

# WebSocket handler
class PedidoWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, pedido_id):
        self.pedido_id = pedido_id
        self.service = PedidoService(pedido_id)
        self.write_message(f"Conectado ao acompanhamento do pedido {pedido_id}.")
        self.ioloop = tornado.ioloop.IOLoop.current()
        self.callback = tornado.ioloop.PeriodicCallback(self.enviar_atualizacao, 3000)  # Atualiza a cada 3 segundos
        self.callback.start()

    def enviar_atualizacao(self):
        status_atual = self.service.get_status()
        self.write_message(json.dumps({
            "pedido_id": self.pedido_id,
            "status": status_atual
        }))
        if status_atual == "ENTREGUE" or status_atual == "Pedido não encontrado":
            self.callback.stop()
            self.close()

    def on_close(self):
        print(f"Conexão fechada para o pedido {self.pedido_id}")

    def check_origin(self, origin):
        return True  # Permitir conexões de qualquer origem (em produção, ajuste conforme necessário)

# Configura a aplicação Tornado
def make_app():
    return tornado.web.Application([
        (r"/ws/pedidos/(.*)", PedidoWebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Servidor WebSocket rodando na porta 8888...")
    tornado.ioloop.IOLoop.current().start()
