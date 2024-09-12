# track-order-backend

## Introdução
O sistema de gerenciamento e acompanhamento de pedidos em tempo real permite que o cliente mantenha uma conexão aberta com o servidor via WebSocket, garantindo atualizações instantâneas do status do pedido a cada 3 segundos, até que seja marcado como "entregue". Essa abordagem melhora a experiência do usuário, eliminando a necessidade de atualizações manuais constantes. Além disso, a API Gateway é responsável por gerenciar o tráfego e rotear as solicitações de forma eficiente e segura, garantindo que todas as requisições sejam encaminhadas corretamente para os serviços apropriados.


## Dependências

- Docker
- Docker Compose
- Python 3.11

## Primeiros Passos

```bash
docker compose up -d db
```

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Serviços

### API

Para executar a API:
```
cd track_api
python manage.py runserver 9000
```

### Websocket

```
cd track_websocket
python app.py
```

## Kong
Kong é uma API Gateway de código aberto que gerencia, autentica, protege e monitora o tráfego entre clientes e microserviços de maneira eficiente.

Instalar o Kong: https://docs.konghq.com/gateway/latest/install/linux/ubuntu/

Copiar "kong.conf":
```bash
sudo cp /etc/kong/kong.conf.default kong.conf
```

Adicione a seguinte linha no arquivo "kong.conf" (no declarative_config, adicionar o caminho absoluto do "kong.yml"):
```
database = off
declarative_config = /home/isisariele/kong.yml
```

Iniciar o Kong:
```bash
sudo kong start -c kong.conf
```

Para parar:
```bash
sudo kong stop
```

## API

Comando para atualizar o pedido:

```bash
curl --request PUT \
  --url http://localhost:9000/api/pedidos/1 \
  --header 'Authorization: Token b70221bc8a6a625d2a23729f47fd3e25bd9dc55d' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.0.0' \
  --data '{
	"status": "EM_TRANSITO"
}'
```
