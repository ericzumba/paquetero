def insist(times, &block)
  begin
    yield 
  rescue => e
    if times > 0
      sleep 1
      insist(times - 1, &block)
    else
      raise e
    end
  end
end
