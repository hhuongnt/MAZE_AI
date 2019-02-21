#!/usr/bin/env python3
from sys import stdin, stdout, stderr

#The communication protocol
def com_protocol():
    for i in range(3):
        if 'HELLO' in stdin.readline():
            stdout.write('I AM A\n\n')
        elif 'YOU ARE' in stdin.readline():
            stdout.write('OK\n\n')


com_protocol()


def get_maze():
    maze = []
    while True:
        line = stdin.readline()
        if line == '\n':
            break
        maze.append(line)
        stderr.write(line)
    return maze
get_maze()
