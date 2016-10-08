ORG:=ericzumba
PROJECT_NAME:=paquetero

IMAGE_NAME:=$(ORG)/$(PROJECT_NAME)

ENV_VAR:= -e AWS_ACCESS_KEY_ID=$(AWS_ACCESS_KEY_ID) \
	-e AWS_SECRET_ACCESS_KEY=$(AWS_SECRET_ACCESS_KEY)

RUN_CMD:=docker run \
	$(ENV_VAR) \
	-v $(LOCATION):$(LOCATION) \
	-i $(IMAGE_NAME) \
	$(CMD) \
	--host="$(HOST)" \
	--core="$(CORE)" \
	--location="$(LOCATION)" \
	--s3-bucket="$(S3_BUCKET)"

image:
	docker build . -t $(IMAGE_NAME) 

run:
	$(shell echo $(RUN_CMD)) 

dev: image
	$(shell echo $(RUN_CMD))	

push: image
	docker push $(IMAGE_NAME) 

compose: image 
	docker-compose run $(ENV_VAR) $(PROJECT_NAME)

remote: push
	ssh -i $(SSH_KEY) $(SSH_USER)@$(HOST) '$(RUN_CMD)'	
