# Test Canvas API
# This code uses Python 3.4.3

import urllib.request

print('Start\n')

# TODO change hardcoded variables to command line args
url = 'https://utah.test.instructure.com/api/v1/users/self'
token = 'Bearer 2~UnZJdsRaLUx10KRzNFgWzr3zS7hNLcJYke7WpL1OidGI3Nvt77tOUuaNa5D6pJa1'
header = {'Authorization' : token}

# https://docs.python.org/3/library/urllib.request.html
req = urllib.request.Request(url, None, header) # no additional data needed so None passed for data arg
with urllib.request.urlopen(req) as response:
	responseStatus = response.getcode()
	messageBytes = response.read()

print('Response Status: ' + str(responseStatus))

htmlOutput = open('output.html','w') # w = write mode

output = "<!DOCTYPE html><html><head><title>Server response</title></head>"
output += "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">"
output += "<body><h1>Jeff's Coding Test 5/13/2015</h1>"
output += "<h2>Server Response: " + str(responseStatus) + "</h2><p>"

if responseStatus == 200:
	print('\nOutputting HTML')
	try:
		# message comes in as bytes
		message = messageBytes.decode("utf-8") # must convert to string to parse
		message = message[1:-1] # trim { from beginning and } from end
	except:
		print("Response invalid. Ending Program.") # no {} found or message containted invalid chars
		quit()	

	lines = message.split(',') # TODO convert to Python JSON parser

	for s in lines:
		output += s + '<br>'

output += '</p></body></html>'

htmlOutput.write(output)
htmlOutput.close()

print('\nDone')
