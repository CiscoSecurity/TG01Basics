import requests

api_key = 'a1b2c3d4e5f6g7h8i9j0k1l2m3'

url = 'https://panacea.threatgrid.com/api/v3/configuration/vms?api_key={}'.format(api_key)

r = requests.get(url)

print(r.json())