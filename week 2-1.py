#print("hello world")
print("What is your first name?")
#
#print("Hello," + first_name)
#print("Hello," + first_name.upper())
#print("Hello, %s!" %first_name.capitalize(), last_name.capitalize() ) )
#print("Hello, {} {}!" %(first_name, last_name))
#print(f"Hello, {first_name} {last_name}!")



"""

-b +/- sqrt(b^2 - 4ac)
--------------------
2a
"""
a = int(input())
b = int(input())
c = int(input())

result = -b + (b**2 - 4*a*c)**(1/2))/(2*a)
print(result)