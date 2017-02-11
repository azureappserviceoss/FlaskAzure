import ast
import requests

class Directory(object):
  def __init__(self, andrewID):
	request = requests.get('https://apis.scottylabs.org/directory/v1/andrewID/' + andrewID)
	self.person = ast.literal_eval(request.content)
	
  def getName(self):
    return self.person.get("first_name")
	
  def getEmail(self):
    return self.person.get("preferred_email")
  
  
    