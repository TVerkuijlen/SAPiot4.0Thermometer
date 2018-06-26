 #!/usr/bin/python3
import requests # http://docs.python-requests.org/en/master/
import time, sys, platform
import random
import decimal
#from w1thermsensor import W1ThermSensor  
#sensor = W1ThermSensor()

hostiot4 = 'capgemini-service.eu10.cp.iot.sap'
deviceAltId = 'dab8d5543dd3b1bd' 
restEndPoint=  'https://%s/iot/gateway/rest/measures/%s'
capabilityAltID= 'da5be72b76224b48'
sensorAlternateId= '8e0776501ea5330c'

def readsensors():
	global gTemp
	gTemp = sensor.get_temperature()
	return
	
def postiotcf ():
	#global gTemp
	#sTemp = str(gTemp)
	sTemp = str(decimal.Decimal(random.randrange(755, 1789))/100)
	
	print("\nValues to post: ", sTemp)
	payload = "{ \"capabilityAlternateId\": \""+capabilityAltID+"\",\"sensorAlternateId\": \""+sensorAlternateId+"\", \"measures\": [\""+sTemp+"\"] }"
	headers = {
			'content-type': "application/json",
			'cache-control': "no-cache"
			}
	url = restEndPoint % (hostiot4, deviceAltId)
	print("Payload to post: ", payload)
	print("URL: ", url)
	print(sTemp)    
	response = requests.request("POST", url, data=payload, headers=headers,cert=('./credentials.crt', './credentials.key'))

	print(response.status_code, response.text)

	return

try:
	while(True):
		#readsensors()
		postiotcf()
		time.sleep(5)
except KeyboardInterrupt:
	print("Stopped by the user!")
	



