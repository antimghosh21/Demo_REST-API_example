import json
import sys
import requests

URL="http://127.0.0.1:8000/api/auth/"

def get_token():
    #get AUTH token
    url="http://127.0.0.1:8000/api/auth/"
    response= requests.post(url, data={'Username': 'antim',
                                       'Password': '12345'}),
    # return response.json()

def get_data():
    url = f"{URL}/api/users_list/"
    # token= get_token()
    header= {'Authorization':F'Token {get_token()}'}
    response = requests.get(url, headers=header)
    Emp_data= response.json()
    for e in Emp_data:
        print(e)
        get_data()

def create_new():
    url=f'{URL}/api/users_list'
    header={'Authorization':f'Token {get_token()}'}
    data= {
        # "employee_id": f"00{count}",
        "employee_id": "007",
        "name": "Apurba Roy",
        "age": 26,
        "ranking": 7.0
    }
    response=requests.post(url, data=data, headers=header)
    print(response.text)
# for e in range(20):
# create_new()

def edit_data(employee_id):
    url = f'{URL}/api/users_list/{employee_id}/'
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "name": "Apurba Roy",
        "age": 26,
        "ranking": 7.0
    }
    response = requests.put(url, data=data, headers=header)
    print(response.text, response.status_code)

# edit_data(2)

def delete_data(employee_id):
    url = f'{URL}/api/users_list/{employee_id}/'
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "name": "Apurba Roy",
        "age": 26,
        "ranking": 7.0
    }
    response = requests.delete(url, headers=header)
    print(response.status_code)

for e in range(10):
    if e > 6:
        delete_data(2)