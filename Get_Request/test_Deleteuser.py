import requests
#import jsonpath

Url = "https://reqres.in/api/users/2"

def test_deleteresource():


    response = requests.delete(Url)


    #fetch response code
    print(response.status_code)
    assert response.status_code == 204