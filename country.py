#!/usr/bin/env python

# system modules
import ftplib
import os
import time

# my modules
import country_vars

### Edit variables ###

# How many hours before we grab a new version of the list
changed = 24

### You shouldn't edit anything below this point ###

# Let's grab the vars from country_vars.py
_nic_server = country_vars._nic_server()
_nic = country_vars._nic()
_country = country_vars._country()
_continent = country_vars._continent()
_country_continent = country_vars._country_continent()

# Store countries in a list, sort it and print it
_country_list = _country.values()
_country_list.sort()
print _country_list

# Asks which country we want to block
# TODO : loop to question if answer not in list
input_country = raw_input("Which country ? ")

# Grab the key for the value supplied, then check the continent and its code
try:
	input_countrycode = _country.keys()[_country.values().index(input_country)]
except ValueError:
	print('No such country')
	exit(3)

input_continentcode = _country_continent[input_countrycode]
input_continent = _continent[input_continentcode]

# Output
print "Country %s (code %s) is in %s (code %s)" % (input_country, input_countrycode, input_continent, input_continentcode)

# Getting all the variables needed to download the lists
ftp_url = _nic_server
ftp_path = _nic[input_continent][0]
iplist = _nic[input_continent][1]

# FTP download file
def getlist():
	dest = open(iplist,'w')
	ftp = ftplib.FTP(ftp_url)
	print "FTP server says:", ftp.login()
	# Traverse directories, there must be a more elegant way
	for i in ftp_path.split('/')[1:]:
		print "cwd to %s" % i
		ftp.cwd(i)
	print "FTP server says:", ftp.retrbinary('RETR %s' % iplist, dest.write)

# Download the file if it has been downloaded more than X hours ago (see variables at the top of this script)
if os.path.exists(iplist):
	iplist_mtime = os.path.getmtime(iplist)
	iplist_mtime_human = time.ctime(iplist_mtime)

	# Check if file has been downloaded within X hours
	if iplist_mtime <= time.time() - changed * 3600:
		download = True
	else:
		download = False

	print "The file %s already exists" % iplist
	print "It was last changed on %s" % iplist_mtime_human
	if download == False:
		print "It was last downloaded within %s hours" % changed
	elif download == True:
		print "It was downloaded more than %s hours ago" % changed
		print "We are going to download it from %s" % ftp_url
		getlist()
else:
	print "The file %s doesn't exist" % iplist
	print "We are going to download it from %s" % ftp_url
	getlist()

# Input : protocol
protocol = int(raw_input("Which protocol :\n1) IPv4\n2) IPv6\n3) Both\n> "))
_protocols = {1: 'ipv4', 2: 'ipv6', 3: 'both'}
try:
	input_protocol = _protocols[protocol]
except ValueError:
	print('Can\'t you type ?')
	exit(10)

ipvx_subnets = {
'ipv4':{ '16777216':'/8','8388608':'/9','4194304':'/10','2097152':'/11','1048576':'/12','524288':'/13','262144':'/14','131072':'/15','65536':'/16','32768':'/17','16384':'/18','8192':'/19','4096':'/20','2048':'/21','1024':'/22','512':'/23','256':'/24','128':'/25','64':'/26','32':'/27','16':'/28','8':'/29',
'768':'/CHECK',
'49152':'/CHECK',
'1536':'/CHECK',
'3072':'/CHECK',
'2560':'/CHECK',
'7860':'/CHECK',
'7680':'/CHECK',
'11520':'/CHECK',
'5120':'/CHECK',
'6400':'/CHECK',
'1792':'/CHECK',
'1280':'/CHECK',
'13312':'/CHECK',
},

'ipv6':{ 
'13':'/todo',
'15':'/todo',
'16':'/todo',
'17':'/todo',
'19':'/todo',
'20':'/todo',
'21':'/todo',
'22':'/todo',
'23':'/todo',
'24':'/todo',
'25':'/todo',
'26':'/todo',
'27':'/todo',
'28':'/todo',
'29':'/todo',
'30':'/todo',
'31':'/todo',
'32':'/todo',
'33':'/todo',
'34':'/todo',
'35':'/todo',
'36':'/todo',
'36534':'/todo',
'37':'/todo',
'38':'/todo',
'39':'/todo',
'40':'/todo',
'41':'/todo',
'42':'/todo',
'43':'/todo',
'44':'/todo',
'45':'/todo',
'46':'/todo',
'47':'/todo',
'48':'/todo',
}

}

# Go through the file and populate result in a list
result = []
for line in open(iplist):
	# parsing country
	if input_countrycode in line:
		if input_protocol != "both":
			if input_protocol in line:
				result.insert(0,line.split('|')[3] + ipvx_subnets[input_protocol][line.split('|')[4]])
		else:
			if 'ipv4' in line:
				result.insert(0,line.split('|')[3] + ipvx_subnets['ipv4'][line.split('|')[4]])
			if 'ipv6' in line:
				result.insert(0,line.split('|')[3] + ipvx_subnets['ipv6'][line.split('|')[4]])

print result

# Output
#finalresult = []
#for key, value in result.items():
#	print key + value
