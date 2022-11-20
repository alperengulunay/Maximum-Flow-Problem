# Maximum flow problem
import math

original_arr = [[-1, 20, 30, 10, -1],
                [0, -1, 40, -1, 30],
                [0, 0, -1, 10, 20],
                [0, -1, 5, -1, 20],
                [-1, 0, 0, 0, -1] ]

arr = [ [-1, 20, 30, 10, -1],
        [0, -1, 40, -1, 30],
        [0, 0, -1, 10, 20],
        [0, -1, 5, -1, 20],
        [-1, 0, 0, 0, -1] ]

desired_node = 4 # + 1
loop = True



def don(curr_node, previous_node):
    for i in range(len(arr[curr_node])):
        if (arr[curr_node][i] != 0):
            if (arr[curr_node][i] != -1):
                if (i not in previous_node):
                    return True
        # if (arr[curr_node][i] != 0 or arr[curr_node][i] != -1 or i not in previous_node ): return True
    return False

while(loop):

    banned_node = -1
    curr_node = 0
    greatest_road = -1
    network = []
    previous_node = []
    last_curr_node = 0

    previous_node.append(curr_node)
    
    for i in range(len(arr[curr_node])):
        yol = arr[curr_node][i]
        if (greatest_road < yol):
            greatest_road = yol
            new_curr_node = i
    curr_node = new_curr_node
    network.append(arr[last_curr_node][curr_node])


    while (curr_node != desired_node):
        greatest_road = -1
        if (don(curr_node, previous_node)):
            last_curr_node = curr_node
            for i in range(len(arr[curr_node])):
                if (i not in previous_node):
                    if (i != banned_node):
                        yol = arr[curr_node][i]
                        if (greatest_road < yol):
                            greatest_road = yol
                            new_curr_node = i
            previous_node.append(curr_node)
            curr_node = new_curr_node
            network.append(arr[last_curr_node][curr_node])
        else:
            banned_node = curr_node
            curr_node = last_curr_node

    previous_node.append(4)

    min_road = 999999

    for yol in network:
        if(yol < min_road): 
            min_road = yol

    for i in range(0, len(previous_node) - 1):
        arr[previous_node[i]][previous_node[i+1]] = arr[previous_node[i]][previous_node[i+1]] - min_road
        arr[previous_node[i+1]][previous_node[i]] = arr[previous_node[i+1]][previous_node[i]] + min_road

    loop = False

    for i in arr[0]:
        if (i == 0):
            loop = False
        elif (i == -1):
            loop = False
        else:
            loop = True
            break

print("\n The original state of the network \n")

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in original_arr]))

print("\n Current state of the network \n")

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in arr]))

print("\n FLOW \t   Flow differences\tFlow rates \tDirections \t")


for i in range(5):
    for j in range(5):
        if (arr[i][j] != original_arr[i][j] and original_arr[i][j]-arr[i][j]>0):
            print('(' + (str)(i+1) , ',' , (str)(j+1) + ')      ', '(' + (str)(original_arr[i][j]-arr[i][j]) , ',' ,
             (str)(arr[i][j]-original_arr[i][j]) + ') \t   ', '(' + (str)(original_arr[i][j]-arr[i][j])  + ')\t     ' , i+1 , '->', j+1)
