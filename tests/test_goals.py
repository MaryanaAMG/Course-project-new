import requests
from faker import Faker
from pytest_steps import test_steps

from modules.goal_methods import create_goal, get_goals, delete_goal, get_goal_by_id, update_goal, \
    get_goals_without_token

fake=Faker()


my_headers = {"Authorization": "pk_188624974_05RT3BHQDG55DKCKKSJ786V6X5FLKMJG"}

@test_steps("Create new goal", "Get all goals", "Delete created goal")
def test_get_goals():
    result = create_goal ()
    assert result.status_code == 200
    goal_data = result.json()["goal"]
    goal_id = goal_data["id"]
    goal_name = goal_data["name"]
    print(f"✅ Goal created: {goal_name} (ID: {goal_id})")
    goal_id = result.json()["goal"]["id"]
    yield
    get_goals()
    assert result.status_code == 200
    yield
    delete_goal(goal_id)
    assert result.status_code == 200
    yield


@test_steps("Create new goal", "Get goal by Id", "Delete created goal")
def test_create_goal():
    result = create_goal()
    assert result.status_code == 200
    goal_id = result.json()["goal"]["id"]
    yield
    get_goal_by_id(goal_id)
    assert result.status_code == 200
    yield
    delete_goal(goal_id)
    assert result.status_code == 200
    yield

@test_steps("Create new goal", "Get goal by Id", "Delete created goal")
def test_get_goal():
    result = create_goal()
    assert result.status_code == 200
    goal_id = result.json()["goal"]["id"]
    yield
    get_goal_by_id(goal_id)
    assert result.status_code == 200
    yield
    delete_goal(goal_id)
    assert result.status_code == 200
    yield

@test_steps("Create new goal", "Update created goal", "Delete created goal")
def test_update_goal():
    result = create_goal()
    assert result.status_code == 200
    goal_id = result.json()["goal"]["id"]
    yield
    update_goal(goal_id)
    assert result.status_code == 200
    yield
    delete_goal(goal_id)
    assert result.status_code == 200
    yield

@test_steps("Create new goal", "Delete created goal")
def test_delete_goal():
    result = create_goal()
    assert result.status_code == 200
    goal_id = result.json()["goal"]["id"]
    yield
    delete_goal(goal_id)
    assert result.status_code == 200
    yield

def test_get_goal_without_token():
    random_name = fake.first_name()
    body = {
        "name": random_name
    }
    result = requests.post("https://api.clickup.com/api/v2/team/90151250102/goal", headers=my_headers, json=body)
    assert result.status_code == 200
    # assert result.json()["name"] == body.get("name")
    goal_id = result.json()["goal"]["id"]

    result = requests.get("https://api.clickup.com/api/v2/team/90151250102/goal")
    assert result.status_code == 400

    result = requests.delete("https://api.clickup.com/api/v2/goal/" + goal_id, headers=my_headers)
    assert result.status_code == 200
