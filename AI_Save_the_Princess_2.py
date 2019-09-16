
def nextMove(n,r,c,grid):
    robot_row = r
    robot_col = c
    princess_row = 0
    princess_col = 0
    path = []
    for i, elem in enumerate(grid):
        for m in range(0, len(elem)):
            #if elem[m] == "m":
            #    robot_row = i
            #    robot_col = m
            if elem[m] == "p":
                princess_row = i
                princess_col = m
    if robot_row < princess_row:
        for i in range(princess_row-robot_row):
            path.append('DOWN')
        action_cnt = princess_col - robot_col
        bot_actions(action_cnt, path)
        
    if robot_row > princess_row:
        for i in range(robot_row-princess_row):
            path.append('UP')
        action_cnt = princess_col - robot_col
        bot_actions(action_cnt, path)
        
    if robot_row == princess_row:
        action_cnt = princess_col - robot_col
        bot_actions(action_cnt, path)

    #for i in range(len(path)):
    print(path[0])
    return ""

def bot_actions(act,path):
    if act < 0:
        for i in range(act*-1):
            path.append('LEFT')
        #print('Left \n'*(act * -1))
    elif act > 0:
        for i in range(act):
            path.append('RIGHT')
        #print('Right \n'*act)
    elif act == 0:
        pass
    
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid)) 
