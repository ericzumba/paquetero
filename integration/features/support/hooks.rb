Before do 
  insist(5) do # Solr takes some time to start
    @solr = RSolr.connect :url => 'http://solr:8983/solr'	
    @solr.get '/'
  end
  @solr.get 'admin/cores', params: { action: 'CREATE', name: 'books' }
  @solr = RSolr.connect :url => 'http://solr:8983/solr/books'	
end

After do
  @solr.delete_by_query  '*:*'
  @solr.commit
end
