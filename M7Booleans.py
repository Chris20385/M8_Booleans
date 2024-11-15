# Cristian Garcia
# 11/12/24

# The first program takes two imputs from the user and tells you if they are equal or not. The second program takes the sum of two numbers and tells you if the are grater than, less than or equal to 10.The third program takes a list and tells you if the value 5 is in that list. The fourth program takes a year and tells you if its a leap year or not. The fifth program gives you the items and weaknesses of characters. And the sixth program checks if a character has the itmes needed to perform certain tasks.


def compare_inputs():
    input1 = input("Enter a first input: ")
    input2 = input("Enter second input: ")

    if input1 == input2:
        print("These inputs are equal")
    else:
        print("These inputs are not equal")

compare_inputs()



def compare_sum():
    input1 = int(input("Enter the first number: "))
    input2 = int(input("Enter the second number: "))

    total = input1 + input2

    if total > 10:
        print(f"The sum of {input1} and {input2} is grater than 10")

    elif total == 10:
        print(f"The sum of {input1} and {input2} is equal to 10")

    else:
        print(f"The sum of {input1} and {input2} is less than 10")

compare_sum()



def num_check( numbers):
    if 5 in numbers:
        print("The value 5 is in this list")
    else:
        print("The value 5 is not in this list")

num_check([1, 7, 4, 3, 5])



def year_check(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
print(year_check(2000))
print(year_check(1800))  
print(year_check(2024))  
print(year_check(2018)) 











import resources

def check_items(num):
    print(f"{resources.player2.nickname}'s profile:")
    print(f"Weapons: {resources.player2.weapons}")
    
    if num == 1:
        required_items = ['rope', 'coat', 'first aid kit']
        
        missing_items = []
        for item in required_items:
            if item not in resources.player2.weapons:
                missing_items.append(item)

        if len(missing_items) > 0:
            print(f"You don't have these items to climb a mountain: ")
            for item in missing_items:
                print(f"- {item}")
            return False
        else:
            print("You have everything you need to climb the mountain!")
            return True

    elif num == 2:
        required_items = ['pan', 'groceries']
        
        missing_items = []
        for item in required_items:
            if item not in resources.player2.weapons:
                missing_items.append(item)

        if len(missing_items) > 0:
            print(f"You don't have these items to cook: ")
            for item in missing_items:
                print(f"- {item}")
            return False
        else:
            print("You have everything you need to cook!")
            return True
    
    elif num == 3:
        required_items = ['pen', 'paper', 'idea']

        missing_items = []
        for item in required_items:
            if item not in resources.player2.weapons:
                missing_items.append(item)
    
        if len(missing_items) > 0:
            print(f"You don't have these items to write a book:")
            for item in missing_items:
                print(f"- {item}") 
            return False
        else:
            print("You have everything you need to write a book!")
            return True

check_items(1)