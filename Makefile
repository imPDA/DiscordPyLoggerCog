DC = docker compose
BOT_FILE = -f ./docker-compose/bot.yaml

build:
	${DC} ${BOT_FILE} build
up:
	${DC} ${BOT_FILE} up -d --build
	make logs
up-a:
	${DC} ${BOT_FILE} up
logs:
	${DC} ${BOT_FILE} logs --follow
down:
	${DC} ${BOT_FILE} down
restart:
	make down
	make up
exec:
	docker exec -it log_bot_test sh
