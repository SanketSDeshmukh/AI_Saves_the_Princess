#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    robot_row = 0
    robot_col = 0
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
        #print('Up \n'*(robot_row-princess_row))
        for i in range(robot_row-princess_row):
            path.append('UP')
        action_cnt = princess_col - robot_col
        bot_actions(action_cnt, path)
        
    if robot_row == princess_row:
        action_cnt = princess_col - robot_col
        bot_actions(action_cnt, path)

    for i in range(len(path)):
        print(path[i])
        
#print all the moves here
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

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
