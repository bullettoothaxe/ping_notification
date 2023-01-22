import json

FILE_NAME = 'users.json'

User = int | str


def read() -> list[User]:
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
        return data


def update(next_users: list[User]):
    uniq_next_users = uniq(next_users)
    with open(FILE_NAME, "w") as file:
        json.dump(uniq_next_users, file)


def add_user(user_id):
    next_users = read().copy()
    next_users.append(user_id)
    update(next_users)


def remove_user(user_id):
    next_users = read().copy()
    next_users.remove(user_id)
    update(next_users)


def uniq(items):
    return list(set(items))
