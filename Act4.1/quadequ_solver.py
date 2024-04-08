import cmath

def quadequation_solver():
    a = int(input("Enter the value of a:\n"))
    b = int(input("Enter the value of b:\n"))
    c = int(input("Enter the value of c:\n"))
    
    d = (b**2) - (4*a*c)
    
    solution1 = (-b-cmath.sqrt(d)/(2*a))
    solution2 = (-b+cmath.sqrt(d)/(2*a))
    
    print("Possible solutions are",solution1,"and",solution2)