import requests
URL = "http://localhost:8000/login"
  
# location given here
import requests
pload = {'username':'abd2@gmail.com','password':'123'}
r = requests.post(URL,data = pload)
print(r.text)

  
