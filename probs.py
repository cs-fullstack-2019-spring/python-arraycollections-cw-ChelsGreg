def main():
    # prob1()
    #prob2()
    # prob3()
    # prob4()
    prob5()




# Create a function with the variable below.
# After you create the variable do the instructions below that.
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# a) Print the 3rd element of the numberList.
# b) Print the size of the array
# c) Delete the second element.
# d) Print the 3rd element.
#
# #
# def prob1():
#
#     siblings = ["Chelsea", "Keith", "Kyle", "Ryan"]
#
#     print(siblings[2])
#     print(len(siblings))
#     siblings.remove("Keith")
#     print(siblings[2])
#



#Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.


# def prob2():
#
#     birthDay = input("What do you like to do for your birthday?")
#
#     while(birthDay != "q"):
#         birthDay = input("What else do you like to do?")




#Create a function that contains a collection of information for the following.
# After you create the collection do the instructions below that.


# def prob3():
#
#     nickNames = {"Johnathan": "John", "Michael": "Mike", "William": "Bill", "Robert": "Rob"}
#
#
#     print(nickNames)
#     print(nickNames["William"])



#Create an array of 5 numbers.
# Using a loop, print the elements in the array reverse order.
# Do not use a function
#
# def prob4():
#
#     fiveNumbers = [5, 10, 15, 20, 25]
#
#     for nums in range(len(fiveNumbers) -1, -1, -1):
#         print(fiveNumbers[nums])
#
#






#Create a function that will have a hard coded array
# then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher,
# lower, or equal to it.


def prob5():

    highLow = [5, 6, 7, 25]
    askUser = int(input("Enter a number"))

    lower = 0
    greater = 0
    equal = 0

    for eachEl in highLow:
        if(askUser > eachEl):
            lower +=1
            print(lower, "numbers are lower")
        elif(askUser < eachEl):
            greater += 1
            print(greater, "numbers are greater")
        elif(askUser == eachEl):
            equal += 1
            print(equal, "numbers are equal")
        else:
            print("Error")

























if __name__ == '__main__':
    main()
