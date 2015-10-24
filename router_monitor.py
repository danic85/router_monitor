import schedule, time, os, sys, urllib2, base64
from datetime import datetime
def check_connection():
	sys.stdout.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Connection")
	hostname = "google.com"
	response = os.system("ping -c 1 " + hostname + " > /dev/null")
	if response == 0:
		print " is up"
	else:
		print " is down!"
def restart_router():
	
	request = urllib2.Request("http://192.18.0.1/sky_rebootCPE.html")
	base = base64.encodestring("%s:%s" % ("admin", "sky")).replace("\n","")
	request.add_header("Authorization", "Basic %s" % base)
	result = urllib2.urlopen(request)

print sys.version
print "starting"
check_connection()
schedule.every(1).minutes.do(check_connection)

while 1:
	schedule.run_pending()
	time.sleep(1)
