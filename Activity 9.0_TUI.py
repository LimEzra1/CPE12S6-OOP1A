#TUI Form
import statistics


def main():

 L = []
 num1 = eval(input("Enter the First Grade: "))
 L.append(num1)
 num2 = eval(input("Enter the Second Grade: "))
 L.append(num2)
 num3 = eval(input("Enter the Third Grade: "))
 L.append(num3)
 print("The Average is: ",statistics.fmean(L))
main()

