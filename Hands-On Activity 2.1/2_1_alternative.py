# -*- coding: utf-8 -*-
"""2-1-alternative.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/pjquillan/2d9b2fe90de20bfc3e515b222df7c925/2-1-alternative.ipynb
"""

def Grades():
  #Global?
  global PG
  global MG
  global FG
  #Prelim
  print("PRELIM")
  PHOA=input("Write HOA grade here: ")
  PQ=input("Quiz grade: ")
  PA=input("Assignment grade: ")
  PEx=input("Prelim Exam grade: ")
  #Midterm
  print("MIDTERM")
  MHOA=input("Write HOA grade: ")
  MQ=input("Write quiz: ")
  MA=input("Write Assignment: ")
  MEx=input("Write Exam Here: ")
  #Final
  print("Final")
  FHOA=input("Write HOA grade here: ")
  FQ=input("Quiz grade: ")
  FA=input("Assignment grade: ")
  FEx=input("Prelim Exam grade: ")
  #Percent formula
  Per50=50/100
  Per30=30/100
  Per10=10/100
  #Calculating
  PCS=(Per50*float(PHOA))+(Per30*float(PQ))+(Per10*float(PA))
  PG=((Per50*float(PEx))+(Per50*float(PCS)))
  MCS=(Per50*float(MHOA))+(Per30*float(MQ))+(Per10*float(MA))
  MG=((1/3)*float(PG))+((2/3)*((Per50*float(MEx))+(Per50*float(MCS))))
  FCS=(Per50*float(FHOA))+(Per30*float(FQ))+(Per10*float(FA))
  FG=((1/3)*float(MG))+((2/3)*((Per50*float(FEx))))+(Per50*float(FCS))
def N():
  print("Prelim grade: ", PG)
  print("Midterm grade: ", MG)
  print("Final grade: ", FG)
#Numerical Grade
def Num_Grades():
  if FG>=94 and FG<=100:
    print(1.00)
  if FG>=88.5 and FG<=93.99:
    print(1.25)
  if FG>=83 and FG<=88.49:
    print(1.50)
  if FG>=77.5 and FG<=82.99:
    print(1.75)
  if FG>=72 and FG<=77.49:
    print(2.00)
  if FG>=65.5 and FG<=71.99:
    print(2.25)
  if FG>=61 and FG<=65.49:
    print(2.50)
  if FG>=55.5 and FG<=60.99:
    print(2.75)
  if FG>=50 and FG<=55.49:
    print(3.00)
  if FG>=0 and FG<=49.99:
    print(5.00)
St1=input("Enter student's name: ")
Grades()
print("Name: ", St1)
N()
Num_Grades()
St2=input("Enter student's name: ")
Grades()
print("Name: ", St2)
N()
Num_Grades()
St3=input("Enter student's name: ")
Grades()
print("Name: ", St3)
N()
Num_Grades()



"""MIDTERM GRADE = 1/3 of PRELIM GRADE + 2/3 of (50% Midterm Exam + 50% Midterm Class Standing (CS))

FINAL GRADE = 1/3 of MIDTERM GRADE + 2/3 of (50% Final Exam + 50% Final Class Standing (CS))
"""

def Num_Grades():
  if FG>=94 and FG<=100:
    print(1.00)
  if FG>=88.5 and FG<=93.99:
    print(1.25)
  if FG>=83 and FG<=88.49:
    print(1.50)
  if FG>=77.5 and FG<=82.99:
    print(1.75)
  if FG>=72 and FG<=77.49:
    print(2.00)
  if FG>=65.5 and FG<=71.99:
    print(2.25)
  if FG>=61 and FG<=65.49:
    print(2.50)
  if FG>=55.5 and FG<=60.99:
    print(2.75)
  if FG>=50 and FG<=55.49:
    print(3.00)
  if FG>=0 and FG<=49.99:
    print(5.00)

FG=74
Num_Grades()

def A():
  return a
def B():
    print(a)

a=A()
B()