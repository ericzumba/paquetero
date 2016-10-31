Before do 
  AWS_ACCESS_KEY_ID     = ENV['AWS_ACCESS_KEY_ID'] 
  AWS_SECRET_ACCESS_KEY = ENV['AWS_SECRET_ACCESS_KEY']
  BUCKET                = ENV['BUCKET']
  GUEST_VOLUME          = ENV['GUEST_VOLUME']
  HOST_VOLUME           = ENV['HOST_VOLUME']
  IMAGE_UNDER_TEST      = ENV['IMAGE_UNDER_TEST']
  SOLR_HOST             = ENV['SOLR_HOST']

  def command(cmd, core)
    "docker run \
      --rm \
      --net=integration_default \
      -e AWS_ACCESS_KEY_ID=#{AWS_ACCESS_KEY_ID} \
      -e AWS_SECRET_ACCESS_KEY=#{AWS_SECRET_ACCESS_KEY} \
      -v #{HOST_VOLUME}:#{GUEST_VOLUME} \
      -i #{IMAGE_UNDER_TEST} #{cmd} \
        --max-retries=0 \
        --time-between-retries=0 \
        --host=#{SOLR_HOST} \
        --core=#{core} \
        --location=#{GUEST_VOLUME} \
        --s3-bucket=#{BUCKET} \
        --backup-alias=#{core}" 
  end
end

