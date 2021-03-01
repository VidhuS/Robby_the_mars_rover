import argparse as ap

import re

import platform

import numpy as np
import pandas as pd



# First we define list of functions we use for our algorithm
# To split the array
# Make robbie move up
def moveup(x, y):
    x = x - 1
    cost = 2
    return x, y, cost


# Make robbie move down
def movedown(x, y):
    x = x + 1
    cost = 2
    return x, y, cost


# Make robbie move left
def moveleft(x, y):
    y = y - 1
    cost = 2
    return x, y, cost


# Make robbie move right
def moveright(x, y):
    y = y + 1
    cost = 2
    return x, y, cost


# Make robbie move upleft
def moveUpleft(x, y):
    x = x - 1
    y = y - 1
    cost = 1
    return x, y, cost


# Make robbie move downleft
def moveDownleft(x, y):
    x = x + 1
    y = y - 1
    cost = 1
    return x, y, cost


# Make robbie move upright
def moveUpright(x, y):
    x = x - 1
    y = y + 1
    cost = 1
    return x, y, cost


# Make robbie move Downright
def moveDownright(x, y):
    x = x + 1
    y = y + 1
    cost = 1
    return x, y, cost


#Using Eucledian distance to calculate value of g and H

def g_value(x,y,sx,sy):
    gvalue=abs(x-sx)+abs(y-sy)
    return gvalue

def h_value(x,y,gx,gy):
    hvalue=abs(x-gx)+abs(y-gy)
    return hvalue

def f_value(cx,cy,sx,sy,gx,gy):
    g=g_value(cx,cy,gx,gy)
    h=h_value(sx,sy,gx,gy)
    f=g+h
    return f,g,h

def addValue(move, x, y, flag, cost, trav):
    trav = trav
    data = {'Move': move, 'cord_X': x, 'cord_Y': y, 'validity': flag, 'cost': cost}
    trav = trav.append(data, ignore_index=True).reset_index().drop(['index'], axis=1)
    return trav


def split(word):
    return [char for char in word]


# To assign coordinates
def strip(x):
    xCord = x[0][len(start) // 2:]
    y_c = xCord[len(xCord) // 2:]
    x_c = xCord[:len(xCord) // 2]
    return x_c, y_c


# Checking if the move is valid
def isValid(c1, c2, n):
    trav = pd.DataFrame(columns=['Move', 'cord_X', 'cord_Y', 'validity', 'cost'])
    x = 0
    y = 0
    n = n
    cost = 0
    x, y, cost = moveright(c1, c2)
    flag = 1
    r = 1
    l = 1
    d = 1
    u = 1
    try:
        if (x in range(n) and y in range(n)):
            if (grid[x, y] == "X"):
                flag = 0
                r = 0
                move = 'R'
                trav = addValue(move, x, y, flag, cost, trav)
                move = 'R D'
                x, y, cost = moveDownright(c1, c2)
                trav = addValue(move, x, y, flag, cost, trav)
                move = 'R U'
                x, y, cost = moveUpright(c1, c2)
                trav = addValue(move, x, y, flag, cost, trav)
            else:
                move = 'R'
                trav = addValue(move, x, y, flag, cost, trav)
        else:
            print('\n move out of bound : Right')

        x, y, cost = moveleft(c1, c2)
        flag = 1
        if (x in range(n) and y in range(n)):
            if (grid[x, y] == "X"):
                flag = 0
                l = 0
                move = 'L'
                trav = addValue(move, x, y, flag, cost, trav)
                move = 'L D'
                x, y, cost = moveDownleft(c1, c2)
                trav = addValue(move, x, y, flag, cost, trav)
                move = 'L U'
                x, y, cost = moveUpleft(c1, c2)
                trav = addValue(move, x, y, flag, cost, trav)
            else:
                move = 'L'
                trav = addValue(move, x, y, flag, cost, trav)
        else:
            print('\n move out of bound : Left')

        x, y, cost = moveup(c1, c2)
        flag = 1
        if (x in range(n) and y in range(n)):
            if (grid[x, y] == "X"):
                flag = 0
                u = 0
                move = 'U'
                trav = addValue(move, x, y, flag, cost, trav)
                move = 'R U'
                x, y, cost = moveUpright(c1, c2)
                trav = addValue(move, x, y, flag, cost, trav)
                move = 'L U'
                x, y, cost = moveUpleft(c1, c2)
                trav = addValue(move, x, y, flag, cost, trav)
            else:
                move = 'U'
                trav = addValue(move, x, y, flag, cost, trav)
        else:
            print('\n move out of bound: Up')

        x, y, cost = movedown(c1, c2)
        flag = 1
        if (x in range(n) and y in range(n)):
            if (grid[x, y] == "X"):
                d = 0
                flag = 0
                move = 'D'
                trav = addValue(move, x, y, flag, cost, trav)
                move = 'L D'
                x, y, cost = moveDownleft(c1, c2)
                trav = addValue(move, x, y, flag, cost, trav)
                move = 'R D'
                x, y, cost = moveDownright(c1, c2)
                trav = addValue(move, x, y, flag, cost, trav)
            else:
                move = 'D'
                trav = addValue(move, x, y, flag, cost, trav)
        else:
            print('\n move out of bound : Down')

        if l == 1 and d == 1:
            x, y, cost = moveDownleft(c1, c2)
            flag = 1
            if (x in range(n) and y in range(n)):
                if (grid[x, y] == "X"):
                    flag = 0
                    move = 'L D'
                    trav = addValue(move, x, y, flag, cost, trav)
                else:
                    move = 'L D'
                    trav = addValue(move, x, y, flag, cost, trav)
            else:
                print('\n move out of bound : Down Left')
        else:
            print('\n direction containing diagonal Down-Left is mountain.')

        if l == 1 and u == 1:
            x, y, cost = moveUpleft(c1, c2)
            flag = 1
            if (x in range(n) and y in range(n)):
                if (grid[x, y] == "X"):
                    flag = 0
                    move = 'L U'
                    trav = addValue(move, x, y, flag, cost, trav)
                else:
                    move = 'L U'
                    trav = addValue(move, x, y, flag, cost, trav)
            else:
                print('\n move out of bound : Up-Left')
        else:
            print('\n direction containing diagonal Up-Left is mountain.')

        if u == 1 and r == 1:
            x, y, cost = moveUpright(c1, c2)
            flag = 1
            if (x in range(n) and y in range(n)):
                if (grid[x, y] == "X"):
                    flag = 0
                    move = 'R U'
                    trav = addValue(move, x, y, flag, cost, trav)
                else:
                    move = 'R U'
                    trav = addValue(move, x, y, flag, cost, trav)
            else:
                print('\n move out of bound : Up-Right.')
        else:
            print('\n direction containing diagonal Up-Right is mountain.')

        if r == 1 and d == 1:
            x, y, cost = moveDownright(c1, c2)
            flag = 1
            if (x in range(n) and y in range(n)):
                if (grid[x, y] == "X"):
                    flag = 0
                    move = 'R D'
                    trav = addValue(move, x, y, flag, cost, trav)
                else:
                    move = 'R D'
                    trav = addValue(move, x, y, flag, cost, trav)
            else:
                print('\n move out of bound Down-right.')
        else:
            print('\n direction containing diagonal Down-Right is mountain.')
        return trav
    except IndexError:
        print("Sorry Robie is unable to reach the solutions")
        file_o.write("Sorry Robie is unable to reach the solutions")
        exit()






if __name__ == "__main__":
    # Reading the file and storeing values in respective variable
    list1 = ['input1.txt', 'input2.txt','input3.txt','input4.txt']
    list2 = ['output1.txt', 'output2.txt','output3.txt','output4.txt']
    i=0
    def main2(i):
        while i <= len(list1):
            file_i = open(list1[i])
            file_o = open(list2[i], "w+")
            tuple = file_i.read().split()
            for i in range(0, len(tuple)): tuple[i] = tuple[i].split(',')
            Array = np.array(tuple, dtype=np.str)
            n = int(Array[0])
            A = np.delete(Array, 0)

            list = []
            for i in range(len(A)):
                a = str(A[i])
                a = split(a)

                list.append(a)
            grid = np.array([np.array(xi) for xi in list])

            start = np.argwhere(grid == "S")
            s1, s2 = strip(start)
            file_o.write(str('Start : ' + str(start)))
            goal = np.argwhere(grid == "G")
            g1, g2 = strip(goal)
            n = 5
            ind = 0
            t_cost = 0
            total_cost = []
            c1 = s1
            c2 = s2
            checked = pd.DataFrame(columns=['Move', 'cord_X', 'cord_Y', 'validity', 'cost'])
            frontier = pd.DataFrame()
            visited = pd.DataFrame({'node_index': [ind], 'Move': ['S'], 'cord_X': [c1], 'cord_Y': [c2], 'cost': [0]})
            while ~(c1 == g1 and c2 == g2):
                node = []
                node = pd.DataFrame(columns=['node_index', 'Move', 'cord_X', 'cord_Y', 'cost'])
                tmp = []
                tmp = isValid(c1, c2, n).reset_index(drop=True)
                checkList = []
                tmpList = []
                checkList = visited[['cord_X', 'cord_Y']].reset_index(drop=True)
                tmpList = tmp[['Move', 'cord_X', 'cord_Y']].reset_index(drop=True)
                moveNa = []
                t = -1
                for i in checkList.index:
                    for j in tmpList.index:
                        if (checkList.cord_X.values[i] == tmpList.cord_X.values[j]) and (
                                checkList.cord_Y.values[i] == tmpList.cord_Y.values[j]):
                            t = t + 1
                            moveNa.insert(t, tmpList.Move.values[j])
                file_o.write('move not allowed: ' + str(moveNa))
                for m in moveNa:
                    delete_row = tmp[tmp['Move'] == m].index
                    tmp = tmp.drop(delete_row)
                tmp.reset_index(drop=True)
                checked = checked.append(tmp)
                frontier = []
                frontier = tmp[tmp.validity == 1].reset_index(drop=True)

                # Frontier for each choice

                x = frontier.cord_X
                y = frontier.cord_Y
                F_value = []
                G_value = []
                H_value = []
                heu_Data = []
                F_value, G_value, H_value = f_value(x, y, s1, s2, g1, g2)
                Heuristic_Data = pd.DataFrame(
                    {'f_value': [F_value][0], 'g_value': [G_value][0], 'h_value': [H_value][0]})

                frontier = pd.concat([frontier, Heuristic_Data], axis=1).sort_values(by=['h_value'])
                node_count = frontier.f_value.count()
                for i in range(node_count):
                    ind = ind + i + 1
                    node_ind = 'N' + str(ind)
                    frontier['node_index'] = node_ind
                file_o.write('OPEN : \n' + str(frontier))

                c1 = frontier.cord_X.values[0]
                c2 = frontier.cord_Y.values[0]
                move = frontier.Move.values[0]
                cost = frontier.cost.values[0]

                node = node.append({'node_index': node_ind, 'Move': move, 'cord_X': c1, 'cord_Y': c2, 'cost': cost},
                                   ignore_index=True)
                visited = visited.append(node).reset_index(drop=True)

                if (c1 == g1 and c2 == g2):
                    visited.iloc[-1]['Move'] = 'G'
                    for m in visited.cost:
                        t_cost = t_cost + m
                        total_cost.append(t_cost)
                    visited['total_cost'] = total_cost
                    file_o.write('\n Congrats! Robbie is home.')
                    file_o.write('CLOSED :\n' + str(visited))
                    solution = ''
                    for m in visited.Move:
                        solution = solution + str(m) + '-'
                    solution = solution + str(visited.total_cost.values[-1])
                    file_o.write(solution)
                file_o.write('CLOSED :\n' + str(visited))
            file_i.close()
            file_o.close()
            i=i+1



