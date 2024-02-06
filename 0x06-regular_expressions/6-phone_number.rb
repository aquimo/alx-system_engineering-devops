#!/usr/bin/env ruby
# Ruby script that accepts on expression matching method
# The regular expressiondigit phone number
puts ARGV[0].scan(/^\d{10}$/).join

