require 'rsolr'
require 'fileutils'

Given(/^solr is running$/) do
	@solr = RSolr.connect :url => 'http://solr:8983/solr'	
end

Given(/^it has a core named books$/) do
  FileUtils.mkdir_p '/opt/solr/server/solr/books'
  insist(5) do
    @solr.get 'admin/cores', params: { action: 'CREATE', name: 'books' }
  end
end

Given(/^there is one indexed document$/) do
  pending # Write code here that turns the phrase above into concrete actions
end

