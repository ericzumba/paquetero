test: rebuild
	docker volume create --name tmp_integ
	docker-compose \
		-f docker-compose.yml \
		run --rm \
		--entrypoint=cucumber  \
		paquetero_integ
	docker-compose down
	docker volume rm tmp_integ


bash: 
	docker volume create --name tmp_integ
	docker-compose \
		-f docker-compose.yml \
		run --rm \
		--entrypoint="/bin/bash"  \
		paquetero_integ
	docker-compose down
	docker volume rm tmp_integ

rebuild: rebuild-app
	docker build .

rebuild-app:
	cd .. && make image 
	
