# Akta List e kicu value ase segulor Jog Fol / Mul Ber korte For Loop Use Na kore Reduce Function Use Kora Jay.....
# Reduce Function Use Korar Jonno Amader Firstly functools Modiul Import Kore Nete Hobe.....
# Reduce Function Same as map() Cause Argument Hisabe Akta Function Soho Itterable objects nete pare.....



import functools


# Example-------------------------------------1
def myFunc(num1,num2):
    return num1 + num2
List1 = [1,2,3,4,5]
Result1 = functools.reduce(myFunc,List1)
print("\nResult1 = ",Result1)






# Example-------------------------------------2
def myFunc1(n1,n2):
    return n1 * n2
Tuple = (1,2,3,4,5)
Result2 = functools.reduce(myFunc1,Tuple)
print("Result2 = ",Result2)
