dev: rebuild down
	docker-compose \
		-f docker-compose.yml \
		run --rm \
		--entrypoint=cucumber \
		paquetero_integ

reset: down rm_volume create_volume

rm_volume:
	docker volume rm tmp

create_volume:
	docker volume create --name tmp

down:
	docker-compose down

rebuild: rebuild-app
	docker build .

rebuild-app:
	cd .. && make image 
	
