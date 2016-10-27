Before do 
  AWS_ACCESS_KEY_ID     = ENV['AWS_ACCESS_KEY_ID'] 
  AWS_SECRET_ACCESS_KEY = ENV['AWS_SECRET_ACCESS_KEY']
  BUCKET                = ENV['BUCKET']
  IMAGE_UNDER_TEST      = ENV['IMAGE_UNDER_TEST']
  SHARED_VOLUME         = ENV['SHARED_VOLUME']
  SOLR_HOST             = ENV['SOLR_HOST']

  def command(cmd, core)
    `docker run \
      --net=integration_default \
      -e AWS_ACCESS_KEY_ID=#{AWS_ACCESS_KEY_ID} \
      -e AWS_SECRET_ACCESS_KEY=#{AWS_SECRET_ACCESS_KEY} \
      -v #{SHARED_VOLUME}:#{SHARED_VOLUME} \
      -i #{IMAGE_UNDER_TEST} #{cmd} \
        --max-retries=0 \
        --time-between-retries=0 \
        --host=#{SOLR_HOST} \
        --core=#{core} \
        --location=#{SHARED_VOLUME} \
        --s3-bucket=#{BUCKET}`
  end
end

