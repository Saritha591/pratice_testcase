import requests
import json
import jsonpath

#API users 
Url = 'https://reqres.in/api/users?page=2'

def test_getdata():

    #sent get request 
    requests.get(Url)

    Response= requests.get(Url)
    print(Response)

    #we want to display response content
    print(Response.content)

    #we can fetch the body and header of respose
    print(Response.headers)

    #parse response to json format
    json_Response = json.loads(Response.text)
    print(json_Response)

    #HOW WE CAN FETCH JSONPATH
    #fetch value using json path
    pages = jsonpath.jsonpath(json_Response,'total_pages')
    print(pages[0])
    assert pages[0] == 2
