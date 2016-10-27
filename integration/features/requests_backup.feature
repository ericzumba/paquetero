Feature: Requests backup
	Client should request backup via http
	Backup should be stored locally
	Backup should be compressed
	Backup should be sent to S3

Scenario: Everything goes well
  Given there are 3 books indexed
  When I request a backup
  Then I should see 'Backup requested'
  And I should see 'Backup is ready'
