import json
import requests
URL = "https://fastapi-abd.herokuapp.com/users"
  
# location given here
import requests


email=input("enter email: ")
pas=input("enter password : ")
pload = {"email":email,"password":pas}
# r = requests.post(URL,data = pload)


  
headers = {'accept': 'application/json','Content-Type':'application/json'}

r = requests.post(URL, headers=headers,json=pload)
print(r.text)