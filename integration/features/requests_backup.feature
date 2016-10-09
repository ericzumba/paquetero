Feature: Requests backup
	Client should request backup via http
	Backup should be stored locally
	Backup should be compressed
	Backup should be sent to S3

Scenario: Everything goes well
	Given there is one indexed document
