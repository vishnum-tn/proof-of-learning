x=float(input ("Enter the first number: "))
y=float(input ("Enter the second number: "))

#round the sum of x and y to the nearest integer
z=round(x+y)

print (f"{z: ,}")
#f is the format  string, the : is the format specifier, and the , is the thousands separator.