def lab2Question1(word):
    # if the input is not a string, return none
    if type(word) != str:
        print(f"{word} is not a string.")
        return None
    word = word.lower()
    if str(word) == str(word)[::-1]:
        return True
    else:
        return False
#Testing 
test1 = lab2Question1("madam")
print(test1)
test2 = lab2Question1("Madam")
print(test2)
test3 = lab2Question1("I")
print(test3)
test4 = lab2Question1("Hello")
print(test4)
test5 = lab2Question1(3)
print(test5)
test6 = lab2Question1("3")
print(test6)

    

def lab2Question2(number_val):
    num1 = 0
    num2 = 1
    FibonacciList = []
    count = 0
    while count < number_val:
        FibonacciList.append(num1)
        num1, num2 = num2, num1+num2
        count += 1
    print(FibonacciList)
#Testing
lab2Question2(10)
lab2Question2(20)
lab2Question2(7) 
lab2Question2(-2)
 


def lab2Question3(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    count = 0
    start= 0
    
    while start < len(str1):
        i = str1.find(str2, start)
        if i != -1:
            start = i + 1
            count += 1
        else: 
            break
    return count
#Testing

print(lab2Question3("renea", "re"))
print(lab2Question3("Coding is cool", "co"))
print(lab2Question3("What's up", "what"))
print(lab2Question3("aaa", "aa"))
    

def lab2Question4(list1, list2):
    if len(list1) != len(list2):
        return []
    
    sum_list = []
    x = len(list1)
    for i in range(x):
        elements_list1 = list1[i]
        elements_list2 = list2[i]
        sum = elements_list1 + elements_list2
        sum_list.append(sum)
    return sum_list
#Testing
print(lab2Question4([2,2],[2,3,4]))
print(lab2Question4([1,2,3],[1,2,3]))
print(lab2Question4([2,-2],[3,1]))

  

def lab2Question5():
    password = None
    while True: 
        password = input("Enter password: ")
        if isValidPassword(password):
            return password
        else: 
            print ("Invalid password, requirements not met. Please try again.")

def isValidPassword(password):
    if len(password) >= 8:
        has_upper = False
        has_lower = False
        has_digit = False
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
        if has_upper and has_lower and has_digit:
            return True
    return False
#Testing
print(isValidPassword("nouppercase123"))
print(isValidPassword("Renea123"))
print(isValidPassword("123"))
print(isValidPassword("renea"))
    

