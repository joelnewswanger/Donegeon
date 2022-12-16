from random import randint


def randomAdj():
    with open("AdjBank.txt", 'r') as file:
        adjective_str = file.read()
    adjective_list = adjective_str.split(" ")
    adjcount = len(adjective_list)
    return(adjective_list[randint(0, adjcount-1)].strip("\n"))

