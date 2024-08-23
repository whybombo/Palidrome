s = input("Enter Value to test to see if it is a Palidrome: ")

reverse = s[::-1]

if ( s == reverse ):
    print("The value is a Palidrome!")
else:
    print("The value is not a Palidrome!")
