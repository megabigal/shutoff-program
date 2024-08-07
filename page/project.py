import requests
import json
import base64 
import datetime

#url to server
url = "https://eu-w1-s19-0qg1zvyxhm.cloud.cambiumnetworks.com/api/v2/"
#the url used to get access token
tokenUrl = "https://eu-w1-s19-0qg1zvyxhm.cloud.cambiumnetworks.com/api/v2/access/token"
#client credentials
clientID = "KI6hbp3GSjiODJCO"
clientSecret = "kMp7ECRbO05HPmbq1DBMmqEjCBdoFb"

#format for authentication
credentials = f'{clientID}:{clientSecret}'
encodedCredentials = base64.b64encode(credentials.encode()).decode()

header = {
    'Authorization':f'Basic {encodedCredentials}',
    'Content-Type':'application/x-www-form-urlencoded'
}
data = {
    'grant_type': 'client_credentials'
}

response = requests.post(tokenUrl, headers=header, data=data)

def getToken():
    tokenUrl = "https://eu-w1-s19-0qg1zvyxhm.cloud.cambiumnetworks.com/api/v2/access/token"
    
    #client credentials
    clientID = "KI6hbp3GSjiODJCO"
    clientSecret = "kMp7ECRbO05HPmbq1DBMmqEjCBdoFb"

    #format for authentication
    credentials = f'{clientID}:{clientSecret}'
    encodedCredentials = base64.b64encode(credentials.encode()).decode()

    header = {
        'Authorization':f'Basic {encodedCredentials}',
        'Content-Type':'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(tokenUrl, headers=header, data=data)
    return response.json()["access_token"]


token = response.json()["access_token"]


logfile = open("log.txt","a")
logfile.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")))
logfile.write(f'user {clientID} logged in \n')

def getWLANData(wlanName,token):
    
    wlanUrl = f'https://eu-w1-s19-0qg1zvyxhm.cloud.cambiumnetworks.com/api/v2/wifi_enterprise/wlans/{wlanName}'
    
    
    header = {
    'Authorization':f'Bearer {token}',
    'Content-Type':'application/x-www-form-urlencoded'
    } 

    wlan = requests.get(wlanUrl, headers=header)
    
   
    
    #print(wlan.json()['data'][0]['basic']

  #  print("*****")
    
    return wlan 
def getSsid(wlanName,token):
    wlanUrl = f'https://eu-w1-s19-0qg1zvyxhm.cloud.cambiumnetworks.com/api/v2/wifi_enterprise/wlans/{wlanName}'
    header = {
    'Authorization':f'Bearer {token}',
    'Content-Type':'application/x-www-form-urlencoded'
    } 
    wlan = requests.get(wlanUrl, headers=header)
    
    return wlan.json()['data'][0]['basic']['ssid']

def updateWLANData(wlanName,token):
    wlanUrl = f'https://eu-w1-s19-0qg1zvyxhm.cloud.cambiumnetworks.com/api/v2/wifi_enterprise/wlans/{wlanName}'
    
   
    header = {
    'Authorization':f'Bearer {token}',
    'Content-Type':'application/json'
    } 
    #obtains the shutdown variable and flips it
    shutdownVar = not getWLANData(wlanName,token).json()['data'][0]['basic']['shutdown']

    w = getWLANData(wlanName,token).json()
    #print(w)
   
    
    
    data = {
        
        "basic": {
        "shutdown": shutdownVar,
        
        },
        "managed_account": "Strathclyde Partnership for Transport"

    }
   # data = getWLANData(wlanName,token).json()
    #data['data'][0]['basic']['shutdown'] = shutdownVar

    
    

    
    
    
    
    r =requests.put(url=wlanUrl, headers=header, data=json.dumps(data))
    #r = requests.put(url=wlanUrl, headers=header, json=data)
    
    
    


    
   



print(getWLANData("Greenock_Bus_Open",token).json()['data'][0]['basic']['shutdown'])
print(getWLANData("Greenock_Bus_OWE",token).json()['data'][0]['basic']['shutdown'])
#updateWLANData("Bus_Test_A",token)

logfile.close()


