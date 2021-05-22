
import json
import requests
import Data


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

  
def Authenticate(user):
  return user in Data.Admins

def Login(author,username,password):
  if author.id == 247589689035325442: #Power
    if username == 'password':
      Data.Admins.append(author)
      return True
  elif author.id == 232316383495454721: #Nic
      if username == 'password':
        Data.Admins.append(author)
        return True
  elif username == 'blacktop':
    if password == 'garage':
      Data.Admins.append(author)
      return True
    else:
      return False