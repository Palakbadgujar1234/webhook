import datetime

def get_greeting():
    now = datetime.datetime.now()
    hour = now.hour
    if 12 <= hour < 18:
        return "Good noon"
    elif 18 <= hour < 22:
        return "Good evening"
    else:
        return "Good night"

names = []
for i in range(10):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

for name in names:
    print(f"{get_greeting()}, {name}!")
