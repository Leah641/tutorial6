# tutorial6

#start
print("# # # f(x) = -x^2 + 3x - 2 from a=1 to b=2 # # #")

#first define the function
def f(x):
    y = -(x**2) + 3*x -2
    return y

#set x
x=1

#print values of function
while x>=1 and x<=2.000001:
    y = f(x)
    print("When x =",x,"=> f(x) =",y)
    x += 0.1

#create first and last
first=f(1)
last=f(2)

#set middle sum
middlesum=0
x = 1.1
while x>1 and x<2:
    middlesum += f(x)
    x += 0.1

#set approximately
approximately= 0.1/2 * (first + last + 2*middlesum)

#set error
error=((1/6 - approximately) / (1/6)) * 100

#print all
print("# # # Example of Trapezium Rule Values # # #")
print("First Height:", first)
print("Last Height:", last)
print("Middle Sum:", middlesum)
print("Integration is approximately",approximately)
print("True value of Integration is 1/6")
print("Therefore the error is",error,"%")

quit()
