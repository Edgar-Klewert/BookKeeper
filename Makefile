# Buildar imagem Docker
build:
	docker build -t bookkeeper-app .

# Rodar usando docker-compose
up:
	docker-compose up

# Parar docker-compose
down:
	docker-compose down

# Rodar container diretamente
run:
	docker run -it bookkeeper-app

# Ver logs em tempo real (local)
logs:
	tail -f logs/bookkeeper.log

# Testes (se criar)
test:
	pytest

# Testes com cobertura
cov:
	pytest --cov=.
