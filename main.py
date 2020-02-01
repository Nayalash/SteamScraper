import requests
import time
import random

curr_index = 1

reduced = open("reduced.txt", "w+")


def exists(name):
    url = f"https://steamcommunity.com/id/{name}"
    print(f"Pinging {url}")
    r = requests.get(url)
    content = str(r.content)
    return not content.__contains__("Sorry!")


with open('list.txt') as f:
    for s_name in f:
        s_name = s_name.strip()
        print(f"{curr_index}: Checking {s_name}...")
        if exists(s_name):
            print(f"{s_name} exists.")
            reduced.write(f"{s_name}\n")
        else:
            print(f"{s_name} does not exist.")

        time.sleep(random.randint(1, 3))
        curr_index += 1

