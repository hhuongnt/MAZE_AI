#!/usr/bin/env python3
from sys import stdin, stdout, stderr


# The communication protocol
def com_protocol():
    for i in range(3):
        if 'HELLO' in stdin.readline():
            stdout.write('I AM A\n\n')
        elif 'YOU ARE' in stdin.readline():
            stdout.write('OK\n\n')


com_protocol()


# Get the maze from VM
def get_maze():
    maze = []
    while True:
        line = stdin.readline()
        if line == '\n':
            break
        maze.append(line)
        stderr.write(line)
    return maze


maze = get_maze()


# find player_coordinate
def player_coordinate():
    player = [0,0]
    for row in range(len(a)):
        for char in range(len(a[row])):
            if a[row][char] == 'A':
                player[0] += row
                player[1] += char
    return player


player = player_coordinate()


# check if a cell is resource or not
def is_it_resources(row,char):
    if a[row][char] == 'o' or a[row][char] == '!':
        return 'resources'
    else:
        return 'not_resources'
