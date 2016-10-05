image:
	docker build . -t ericzumba/socopia

run:
	docker run -i ericzumba/socopia 

dev: image
	docker run -i ericzumba/socopia backup 
