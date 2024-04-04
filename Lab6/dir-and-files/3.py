import os

pathie = "C:/Users/Aidar/Desktop/pp2"

if os.path.exists(pathie):
    print("Path exists.")
    print("Directory:", os.path.dirname(pathie))
    print("Filename:", os.path.basename(pathie))
else:
    print("Path does not exist.")