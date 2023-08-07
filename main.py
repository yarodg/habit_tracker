import requests
from datetime import datetime

# Your username for pixe.la
USER_NAME = ""

# Your token for pixe.la
PIXELA_TOKEN = ""

# Graph name.
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

## Making a new user/account.
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

## Making a new graph.
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
## Date for backlog pixel recording
# today = datetime.now(year=2023, month=8, day=7)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes have you spent learning programming today? ")
}

# # Making a pixel log.
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity": input("How many minutes did you actually program? ")
}

# # Updating a pixel log.
# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# # Deleting a pixel log.
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

