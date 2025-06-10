import requests
from faker import Faker
fake=Faker()

my_headers = {"Authorization": "pk_188624974_05RT3BHQDG55DKCKKSJ786V6X5FLKMJG"}

def create_task ():
    random_name = fake.first_name()
    body = {
        "name": random_name
    }
    result = requests.post("https://api.clickup.com/api/v2/list/901511049038/task", headers=my_headers, json=body)
    return result

def get_tasks():
    result = requests.get("https://api.clickup.com/api/v2/list/901511049038/task", headers=my_headers)

def get_task_by_id(task_id):
    result = requests.delete("https://api.clickup.com/api/v2/task/" + task_id, headers=my_headers)

def delete_task(task_id):
    result = requests.delete("https://api.clickup.com/api/v2/task/" + task_id, headers=my_headers)


def update_task(task_id):
    random_name_for_update = fake.first_name()
    body_updated = {
        "name": random_name_for_update
    }
    result = requests.put("https://api.clickup.com/api/v2/task/" + task_id, headers=my_headers, json=body_updated)
    return result

def get_tasks_without_token():
    result = requests.get("https://api.clickup.com/api/v2/list/901511049038/task")
