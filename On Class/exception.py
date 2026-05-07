# denominator = input("please enter a deniminator: ")
# numerator = None

# try: 
#     denominator = int(denominator)
#     print(numerator/denominator)

# except ZeroDivisionError:
#     print("can't divide by a zero poopy >:(")

# except ValueError:
#     print("can't enter a string doodie T_T")

# except TypeError: 
#     print("learn your inputs, this is why you're hard to love")
#     numerator = int(input("well well well, enter a numerator: "))

# finally: 
#     print(numerator/denominator)


sandwiches = ("BLT", "Italian", "Teriyaki")

sandwich_index = (int(input("what sandwich do you want?")))
try: 
    print(sandwiches[sandwich_index])

except IndexError:
    print("sorry, we don't have that sandwich")