backup:
	./backup.sh $(HOST) $(CORE) $(LOCATION) $(SSH_KEY) $(SSH_USER)

restore:
	./restore.sh $(HOST) $(CORE) $(LOCATION)
