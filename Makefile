ORG:=ericzumba
PROJECT_NAME:=paquetero

IMAGE_NAME:=$(ORG)/$(PROJECT_NAME)

RUN_CMD:=docker run \
	-v $(LOCATION):$(LOCATION) \
	-i $(IMAGE_NAME) \
	$(CMD) \
	--host="$(HOST)" \
	--core="$(CORE)" \
	--location="$(LOCATION)"

image:
	docker build . -t $(IMAGE_NAME) 

run:
	$(shell echo $(RUN_CMD)) 

dev: image
	$(shell echo $(RUN_CMD))	

push: image
	docker push $(IMAGE_NAME) 

remote: push
	ssh -i $(SSH_KEY) $(SSH_USER)@$(HOST) '$(RUN_CMD)'	
