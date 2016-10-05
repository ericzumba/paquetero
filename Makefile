image:
	docker build . -t ericzumba/paquetero

run:
	docker run -i ericzumba/paquetero

dev: image
	docker run -i ericzumba/paquetero backup --host="$(HOST)" --core="$(CORE)" --location="$(LOCATION)"
