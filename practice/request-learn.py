statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
# online_number = 0
# print(statuses.items())
# for value in statuses.values():
#     if value == "online":
#         online_number += 1
# print(online_number)


def online_count(status):

    online_number = 0
    for value in status.values():
        if value == "online":
            online_number += 1
    return online_number

print(online_count(statuses))