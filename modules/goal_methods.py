import requests
from faker import Faker
fake=Faker()

my_headers = {"Authorization": "pk_188624974_05RT3BHQDG55DKCKKSJ786V6X5FLKMJG"}

def create_goal ():
    random_name = fake.first_name()
    body = {
        "name": random_name
    }
    result = requests.post("https://api.clickup.com/api/v2/team/90151249020/goal", headers=my_headers, json=body)
    return result

def get_goals():
    result = requests.get("https://api.clickup.com/api/v2/team/90151249020/goal", headers=my_headers)

def get_goal_by_id(goal_id):
    result = requests.delete("https://api.clickup.com/api/v2/goal/" + goal_id, headers=my_headers)

def delete_goal(goal_id):
    result = requests.delete("https://api.clickup.com/api/v2/goal/" + goal_id, headers=my_headers)

def update_goal(goal_id):
    random_name_for_update = fake.first_name()
    body_updated = {
        "name": random_name_for_update
    }
    result = requests.put("https://api.clickup.com/api/v2/goal/" + goal_id, headers=my_headers, json=body_updated)
    return result
