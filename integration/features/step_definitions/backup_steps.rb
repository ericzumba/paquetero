require 'rsolr'
require 'fileutils'

Given(/^solr is running$/) do
  insist(5) do # Solr takes some time to start
    @solr = RSolr.connect :url => 'http://solr:8983/solr'	
    @solr.get '/'
  end
end

Given(/^it has a core named books$/) do
  FileUtils.mkdir_p '/opt/solr/server/solr/books'
  @solr.get 'admin/cores', params: { action: 'CREATE', name: 'books' }
  @solr = RSolr.connect :url => 'http://solr:8983/solr/books'	
end

Given(/^there is one indexed document$/) do
  @solr.add(id: 1)
  @solr.commit
end

