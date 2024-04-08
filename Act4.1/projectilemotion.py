import math

def projectilemotion_solver():
    velocity = int(input("Enter velocity:\n"))
    angle = int(input("Enter angle:\n"))
    
    max_distance = float(((velocity)**2*math.sin(2*angle))/9.8)
    
    max_height = float(((velocity)**2*math.sin(2*angle))/(2*9.8))
    
    print("Max distance is ",max_distance)
    print("Max height is ",max_height)