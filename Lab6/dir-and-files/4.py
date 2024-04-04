import os

pathie = "C:/Users/Aidar/Desktop/pp"

def fun(pathie):
    with open(pathie, 'r') as file:
        print("Number of lines:", len(file.readlines()))
