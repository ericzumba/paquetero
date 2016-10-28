require 'rsolr'
require 'fileutils'

Given(/^it has a core named books$/) do
  @solr.get 'admin/cores', params: { action: 'CREATE', name: 'books' }
  @solr = RSolr.connect :url => 'http://solr:8983/solr/books'	
end

Given(/^there are (\d+) books indexed$/) do |books|
  (1..books.to_i).each do |i|
    @solr.add(id: i)
  end
  @solr.commit
end

When(/^I request a backup$/) do
  cmd = command("backup", "books")
  puts cmd
  puts @command_output = `#{cmd}` 
end

Then(/^I should see ('[^\']*')$/) do |message|
  @command_output.include?(message) 
end
