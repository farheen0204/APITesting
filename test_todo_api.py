from http.client import responses

import requests
import uuid

ENDPOINT = "https://todo.pixegami.io"

# response = requests.get(ENDPOINT)
# print(response)
#
# data = response.json()
# print(data)
#
# status_code = response.status_code
# print(status_code)

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task():

    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()

    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

def test_can_update_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    new_payload = {
        "content": "my updated content",
        "user_id": payload["user_id"],
        "task_id": task_id,
        "is_done": True
    }
    #update the task

    update_task_response = update_task(new_payload)
    assert create_task_response.status_code == 200

    # get and validate the changes
    get_task_response = get_task(task_id)
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["user_id"] == new_payload["user_id"]

def test_can_list_tasks():
    #create N tasks
    n = 3
    payload = new_task_payload()
    for _ in range(3):

        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    user_id = payload["user_id"]
    list_tasks_response = list_task(user_id)
    assert list_tasks_response.status_code == 200
    data = list_tasks_response.json()
    tasks = data["tasks"]
    assert len(tasks) == n
    print(data)

def test_can_delete_task():
    # Create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    # Delete the task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200
    # Get the task and check that its not found
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404


def create_task(payload):
    return requests.put(ENDPOINT +  "/create-task", json=payload)

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    print(f"Creating task for user {user_id} with content{content}")
    return  {
        "content": content,
        "user_id": user_id,
        "is_done": False
    }

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def list_task(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def update_task(payload):
    return requests.put(ENDPOINT +  "/update-task", json=payload)

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")
