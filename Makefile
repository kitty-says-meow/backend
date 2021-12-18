include .env
export

init:
	mkdir data && cp .env.sample .env && docker volume create --name ict_hack_db -d local

dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build

run:
	docker-compose up -d --build

stop:
	docker-compose stop

logs:
	docker-compose logs --tail=1000 --follow

bash:
	docker exec -it ${COMPOSE_PROJECT_NAME}_web_1 bash

psql:
	docker exec -it ${COMPOSE_PROJECT_NAME}_db_1 psql --username ${POSTGRES_USER}

shell:
	docker exec -it ${COMPOSE_PROJECT_NAME}_web_1 python manage.py shell_plus

test:
	docker exec -it ${COMPOSE_PROJECT_NAME}_web_1 bash -c "python manage.py test"
