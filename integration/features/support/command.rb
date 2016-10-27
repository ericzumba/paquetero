Before do 
  @aws_id = ENV['AWS_ACCESS_KEY_ID'] 
  @aws_key = ENV['AWS_SECRET_ACCESS_KEY']
  @image = ENV['IMAGE_UNDER_TEST']

  def command(cmd)
    `docker run -e AWS_ACCESS_KEY_ID=#{@aws_id} -e AWS_SECRET_ACCESS_KEY=#{@aws_key} -v /tmp:/tmp -i #{@image} #{cmd}`
  end
end

