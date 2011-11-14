# This script takes a number of pieces of data from the edison API and converts them to facts
require 'net/http'
require 'yaml'

edisonserver = 'edison'
edisonport = 80


server = Net::HTTP.new(edisonserver,edisonport)
this_host = Facter.fqdn 

# Get the puppet classes and metadata from the /puppet url
factheaders,factdata = server.get("/api/puppet/#{this_host}/?format=yaml")
factdata_hash = YAML::load(factdata)

# create the "puppet_classes" fact
Facter.add('puppet_classes') do
	setcode do
		factdata_hash['classes']
	end
end

# setup the parameters
factdata_hash['metadata'].each do |key,value|
	Facter.add(key.lstrip()) do
		setcode do
			value
		end		
	end
end

# get the system facts from the /host url
hostheaders,hostdata = server.get("/api/hosts/#{this_host}/?format=yaml")
hostdata_hash = YAML::load(hostdata)

# setup the parameters
hostdata_hash.each do |key,value|
	Facter.add(key.lstrip()) do
		setcode do
			value
		end		
	end
end
