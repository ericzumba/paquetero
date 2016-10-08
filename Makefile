ORG:=ericzumba
PROJECT_NAME:=paquetero

IMAGE_NAME:=$(ORG)/$(PROJECT_NAME)

ENV_VARS:= -e AWS_ACCESS_KEY_ID=$(AWS_ACCESS_KEY_ID) \
	-e AWS_SECRET_ACCESS_KEY=$(AWS_SECRET_ACCESS_KEY)

CMD_OPTS:= $(CMD) \
	--host="$(HOST)" \
	--core="$(CORE)" \
	--location="$(LOCATION)" \
	--s3-bucket="$(S3_BUCKET)"

RUN_CMD:=docker run \
	$(ENV_VARS) \
	-v $(LOCATION):$(LOCATION) \
	-i $(IMAGE_NAME) \
	$(CMD_OPTS)

image:
	docker build . -t $(IMAGE_NAME) 

run:
	$(shell echo $(RUN_CMD)) 

dev: image
	$(shell echo $(RUN_CMD))	

push: image
	docker push $(IMAGE_NAME) 

compose: image 
	docker-compose run $(ENV_VARS) $(PROJECT_NAME) $(CMD_OPTS)

remote: push
	ssh -i $(SSH_KEY) $(SSH_USER)@$(HOST) '$(RUN_CMD)'	
