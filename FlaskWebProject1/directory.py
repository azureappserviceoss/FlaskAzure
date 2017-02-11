import ast
import requests

class Directory(object):
  def __init__(self, andrewID):
	request = requests.get('https://apis.scottylabs.org/directory/v1/andrewID/' + andrewID)
	self.person = ast.literal_eval(request.content)
	
  #returns a dictionary with the given fields
  def getInfo(self, fields=[]):
    return {k:self.person.get(k) for k in fields}
	
  
  
    