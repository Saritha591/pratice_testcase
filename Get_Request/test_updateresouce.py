from json import JSONDecoder
import json
import requests
import jsonpath

#ApI users
Url = 'https://reqres.in/api/users/2'

#Read input json file
def test_updatedresources():
    file = open('D:\\saritha_pytest\\pratice_testcase\\Get_Request\\data.json','r')
    json_input = file.read()

    requests_json = json.loads(json_input)
    print(requests_json) 

    #make put using input body
    Response = requests.put(Url,requests_json)
    print(Response.content)

    #validating response
    assert Response.status_code == 200