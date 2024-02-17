import math

case = int(input())

def main():

    for j in range(case):
        line = float(input())

        if line // 25:
            return line
        print(line)