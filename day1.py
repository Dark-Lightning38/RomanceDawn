name = "Alex"
name2 = "Simon"
times = 10
variable1=0

for i in range(3):
    print("Hello", name)

for a in range(times):
    print("Hello Mr", name)

for b in range(1,11):
    print("Hello", name)

for i in range(1,12):
    variable1 += 1
    print("Hello Sr", name, variable1)

for i in range(1,12):
    variable2 = 0
    variable2 += 1
    print("Hello Sr", name, variable2)


variable3=0
for i in range(1,11):

    variable3 +=1
    print(f"Hello Sr {name}, numero {variable3}")
 

agents1 = [
    {"name":"Alex","FTE":0.7,"days-worked":[1,2,3]},
    {"name":"Simon","FTE":1,"days-worked":[0,1,2,3,4]},
    {"name":"Carmen","FTE":1,"days-worked":[0,1,2,4,5]},
    {"name":"Annelise","FTE":0.7,"days-worked":[0,5,6]}
]

for agent in agents1:
    print (f"Agent {agent['name']} works on days: {agent['days-worked']} for a total FTE of {agent['FTE']}")

def add_agent1(agents_list, name, FTE, days_worked):
    agents_list.append({"name": name, "FTE": FTE, "days-worked":days_worked})

def add_agent2(agents_list, name, FTE, days_worked, hours_worked):
    agents_list.append({"name": name, "FTE": FTE, "days-worked":days_worked,"Hours-worked":hours_worked})

add_agent1(agents1, "Matthieu", 1, [0,1,2,3,4])
add_agent2(agents1, "Agathe",0.5, [0,1,2,3,4], (8,18))

print(agents1)

def add_dimmension_to_agents(agents_lists,key,value):
    for agent in agents_lists:
        agent[key]=value

agents2 = [
    {"name":"Alex","FTE":0.7,"days-worked":[1,2,3]},
    {"name":"Simon","FTE":1,"days-worked":[0,1,2,3,4]},
    {"name":"Matt","FTE":1,"days-worked":[0,1,2,4,5]},
    {"name":"Annelise","FTE":0.7,"days-worked":[0,5,6]}
]

add_dimmension_to_agents(agents2, "Hours-worked", (8,18))

print(agents2)


def update_agent1(agents_list,name,FTE,days_worked):
    for agent in agents_list:
        if agent["name"] == name:
            agent["FTE"] = FTE
            agent["days-worked"] = days_worked

update_agent1(agents1,"Simon", 1, [1,2,3,4,5])
print(agents1)

print(agents1)

def update_agent2(agents_list,name,FTE,days_worked,Hours_worked):
    for agent in agents_list:
        if agent["name"] == name:
            agent["FTE"] = FTE
            agent["days-worked"] = days_worked
            agent["Hours-worked"] = Hours_worked
    print(next((agent for agent in agents_list if agent.get("name") == name), None))

update_agent2(agents1,"Simon", 1, [0,1,2,3,4,5],(9,18))


def update_agent3(agents_list,name,FTE,days_worked,Hours_worked):
    for agent in agents_list:
        if agent["name"] == name:
            agent["FTE"] = FTE
            agent["days-worked"] = days_worked
            agent["Hours-worked"] = Hours_worked
    print(next((agent for agent in agents_list if agent.get("name") == name), None))

update_agent3(agents1,"Simon", 1, [0,1,2,3,4,5],(7,16))


def self_add_agent():
    new_self_add_agent = {}
    name_input = input("Hello, Please start by giving me your name: ")
    print(f"Hello {name_input}, thank you for joining us!")
    FTE_input = float(input("Please enter your FTE: "))
    days_worked_input = input("Please enter the days you worked: ")
    hours_worked_input = input("Please enter the range of hours you work each day: ")
    agents1.append({"name": name_input, "FTE": FTE_input, "days-worked": days_worked_input, "Hours-worked": hours_worked_input})
    print(f"Agent added: {name_input}")
    print(agents1)

#self_add_agent()
def self_add_agent2():
#    new_self_add_agent = {} #WHY did I create this ? to add into a dic and then add this into list ... instead I did ti manually on line 121
    name_input = str(input("Hello, Please start by giving me your name: "))
    print(f"Hello {name_input}, thank you for joining us!")
    FTE_input = float(input("Please enter your FTE: "))
    days_worked_input = list(input("Please enter the days you worked (monday being 0 and sunday 6 - no space or comma): "))
    hours_worked_input = tuple(map(int, input("Please enter the range of hours you work each day (e.g., 8,18): ").split(","))) #WHY the split/map/tuple?
    agents1.append({"name": name_input, "FTE": FTE_input, "days-worked": days_worked_input, "Hours-worked": hours_worked_input})
    print(f"Agent added: {name_input}")
    print(agents1)

#self_add_agent2()

# try:
#     Number=int(input("please enter a number: "))
#     print(f'The number you entred in correct: {Number}')
# except:
#     print("An error occurred, please enter a valid number")

# try:
#     Number=int(input("please enter a number: "))
#     print(f'The number you entred in correct: {Number}')
# except ValueError:
#     print("An error occurred, please enter a valid number")


def self_add_agent3():
    try:
#        new_self_add_agent = {} #WHY did I create this ? to add into a dic and then add this into list ... instead I did ti manually on line 148
        name_input = str(input("Hello, Please start by giving me your name: "))
        if len(name_input) < 2:
            print("Invalid input for Name, must be at least 2 characters long")
            return
        else:
            print(f"Hello {name_input}, thank you for joining us!")
        FTE_input = float(input("Please enter your FTE: "))
        days_worked_input = list(input("Please enter the days you worked (monday being 0 and sunday 6 - no space or comma): "))
        hours_worked_input = tuple(map(int, input("Please enter the range of hours you work each day (e.g., 8,18): ").split(",")))
        agents1.append({"name": name_input, "FTE": FTE_input, "days-worked": days_worked_input, "Hours-worked": hours_worked_input})
        print(f"Agent added: {name_input}")
        print(agents1)
    except ValueError:
        print("An error occurred while adding the agent. Please make sure to enter valid inputs.")

if __name__ == "__main__":
    self_add_agent3()



