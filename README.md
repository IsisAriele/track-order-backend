# track-order-backend

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
