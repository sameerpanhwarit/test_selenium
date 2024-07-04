
import requests

class Request:
    def __init__(self, baseURL):
        self.baseURL = baseURL

    @staticmethod
    def userData():

        email = input("Enter user email: ")
        first = input("Enter user first name: ")
        last = input("Enter user last name: ")

        json = {
            'email': email,
            'first': first,
            'last': last
        }

        return json


    def get(self, params=None):
        response = requests.get(self.baseURL, params=str(params))
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Request failed with status code {response.status_code}")

    def post(self, data=None):
        response = requests.post(self.baseURL, json=data)
        if response.status_code == 201:
            print(f'User created successfully: {response.json()}')
        else:
            print(f"Request failed with status code {response.status_code}")

    def put(self, endpoint, data=None):
        url = f'{self.baseURL}/{endpoint}'
        response = requests.put(url, json=data)
        if response.status_code == 200:
            print(f"User updated successfully: {response.json()}")
        else:
            print(f"Request failed with status code {response.status_code}")

if __name__ == '__main__':
    request = Request('https://reqres.in/api/users')

    requestOption = input('Which Request you want to made? GET, PUT,POST: ').upper()

    while True:
        if requestOption == 'GET':
            request.get(params=1)
            break

        elif requestOption == 'POST':
            json = request.userData()
            request.post(data=json)
            break
        
        elif requestOption == 'PUT':
            userID= input('Enter user ID you want to update: ')
            json = request.userData()
            request.put(endpoint=userID, data=json)
            break

        else:
            print('Invalid Request Option!!!')
