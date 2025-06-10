import requests
from faker import Faker
from pytest_steps import test_steps

from modules.task_methods import create_task, get_tasks, delete_task, get_task_by_id, update_task

fake=Faker()


my_headers = {"Authorization": "pk_188624974_05RT3BHQDG55DKCKKSJ786V6X5FLKMJG"}

@test_steps("Create new task", "Get all task", "Delete created task")
def test_get_tasks():
    result = create_task ()
    assert result.status_code == 200
    task_data = result.json()
    task_id = task_data["id"]
    task_name = task_data["name"]
    print(f"✅ Task created: {task_name} (ID: {task_id})")
    yield
    get_tasks()
    assert result.status_code == 200
    yield
    delete_task (task_id)
    assert result.status_code == 200
    yield


@test_steps("Create new task", "Get task by Id", "Delete created task")
def test_create_task():
    result = create_task()
    assert result.status_code == 200
    task_id = result.json()["id"]
    yield
    get_task_by_id(task_id)
    assert result.status_code == 200
    yield
    delete_task(task_id)
    assert result.status_code == 200
    yield

@test_steps("Create new task", "Get task by Id", "Delete created task")
def test_get_task():
    result = create_task()
    assert result.status_code == 200
    task_id = result.json()["id"]
    yield
    get_task_by_id(task_id)
    assert result.status_code == 200
    yield
    delete_task(task_id)
    assert result.status_code == 200
    yield

@test_steps("Create new task", "Update created task", "Delete created task")
def test_update_task():
    result = create_task()
    assert result.status_code == 200
    task_id = result.json()["id"]
    yield
    update_task(task_id)
    assert result.status_code == 200
    yield
    delete_task(task_id)
    assert result.status_code == 200
    yield

@test_steps("Create new task", "Delete created task")
def test_delete_task():
    result = create_task()
    assert result.status_code == 200
    task_id = result.json()["id"]
    yield
    delete_task(task_id)
    assert result.status_code == 200
    yield

def test_get_task_without_token():
    random_name = fake.first_name()
    body = {
        "name": random_name
    }
    result = requests.post("https://api.clickup.com/api/v2/list/901511049038/task", headers=my_headers, json=body)
    assert result.status_code == 200
    # assert result.json()["name"] == body.get("name")
    task_id = result.json()["id"]

    result = requests.get("https://api.clickup.com/api/v2/list/901511049038/task")
    assert result.status_code == 400

    result = requests.delete("https://api.clickup.com/api/v2/task/" + task_id, headers=my_headers)
    assert result.status_code == 204
