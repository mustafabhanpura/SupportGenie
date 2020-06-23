import random
all_agents = []
all_issues = []
list_roles = [['sales'],['translator'],['sales','translator']] #This list is used randomly allot roles to agents and issues

#following is the class which generates instances Agents and Issues to be resolved
class Agent():
    def __init__(self,id,time,roles):
        self.id = id
        self.is_available = True
        self.available_since = time
        self.roles = roles

    def __str__(self):
        return str(self.id)

class Issue():
    def __init__(self,id,roles):
        self.id = id
        self.roles = roles
        self.resolved = False

    def __str__(self):
        return str(self.id)

# following two functions make instances of the above defined class i.e. Agent and Issue
def create_agents(id):
    idle_time = random.randint(10,30)
    agent_role = (list_roles[random.randint(0,len(list_roles)-1)])
#     idle_time = input("Enter the idle time for Agent-"+str(id)+":")
    #agent_role = list(input("Enter the roles:").split(','))
    new_agent = Agent(id,idle_time,agent_role)
    all_agents.append(new_agent)

def create_issues(id):
#     role = list(input("Enter the rolels for Issue-"+str(id)+":").split(','))
    role  =  (list_roles[random.randint(0,len(list_roles)-1)])
    new_issue = Issue(id,role)
    all_issues.append(new_issue)


# this is the main function that takes in the list of available agents along with the issue and mode of selection of agents
def generate_agents(all_agents, mode, issue):
    active_agents = []  # list used to store the available agents based on their availability and matching issue roles
    for agent in all_agents:
        if agent.is_available == True:
            for role in issue.roles:
                if role in agent.roles:
                    match = True
                else:
                    match = False
                    break
            if match:
                active_agents.append(agent)
    if active_agents:

        if mode == 1:  # mode=1 is assigned to All-Available mode of selection

            print('Available agents:')
            for agent in active_agents:
                print("Agent-", agent.id)
            select_agent = int(input("Agent Id choosing the issue:"))

            for agents in all_agents:
                if agents.id is select_agent:
                    agents.is_available = False
                    break

            return agents

        if mode == 2:  # mode=2 is assigned to Least Busy mode of selection
            sorted_list = sorted(active_agents, key=lambda x: x.available_since, reverse=True)
            sorted_list[0].is_available = False
            selected_agent = sorted_list[0]

            return selected_agent

        if mode == 3:  # mode = 3 is assigned to Random mode of selection

            selected_agent = active_agents[random.randint(0, len(active_agents) - 1)]
            for agents in all_agents:
                if agents.id is selected_agent.id:
                    agents.is_available = False
                    break

            return selected_agent
    else:
        print("No agents are available at this moment.")


if __name__ == '__main__':
    n = int(input("Enter the number of issues:"))

    for i in range(10):
        create_agents(i)
    for i in range(n):
        create_issues(i)
    print('Agent Id  Available Since\tAgent Role')
    for agent in all_agents:
        print(agent.id, '\t\t', agent.available_since, "\t\t", agent.roles)
    print('Issue Id\tIssue Role ')
    for issue in all_issues:
        print(issue.id, "\t\t", issue.roles)
    print()
    # Loop through all the pending issues
    for issue in all_issues:
        print()
        print("Issue to be resolved ISSUE-", issue.id)
        print()
        selection = int(input("Enter the selection mode:\n"
                              "1:All Available\n"
                              "2:Least Busy\n"
                              "3:Random\n "))

        if selection == 1:
            mode = 1
            active_agents = generate_agents(all_agents, mode, issue)
            if active_agents:
                print('The agent assigned to Issue-' + str(issue.id) + ' is Agent-', active_agents.id)

        if selection == 2:
            mode = 2
            active_agents = generate_agents(all_agents, mode, issue)
            if active_agents:
                print('The agent assigned to Issue-' + str(issue.id) + ' is Agent-', active_agents.id)

        if selection == 3:
            mode = 3
            active_agents = generate_agents(all_agents, mode, issue)
            if active_agents:
                print('The agent assigned to Issue-' + str(issue.id) + ' is Agent-', active_agents.id)
        issue.resolved = True
        print()
        print('Agent Id  Available Since\tAgent Role')
        for agent in all_agents:
            if agent.is_available:
                print(agent.id, '\t\t', agent.available_since, "\t\t", agent.roles)



