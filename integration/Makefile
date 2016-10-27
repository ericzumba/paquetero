dev: rebuild down
	docker-compose \
		-f docker-compose.yml \
		run --rm \
		--entrypoint=cucumber \
		paquetero-integ

down:
	docker-compose down

rebuild: rebuild-app
	docker build .

rebuild-app:
	cd .. && make image 
	
