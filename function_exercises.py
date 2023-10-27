#is_two defines x as only parameter
def is_two(x):
    #checks to see if x is equal to int 2 or str 2
    if x == 2 or x == '2':
        #If true returns true
        return True
    #Otherwise, any other answer returns false
    else:
        return False
#-------------------
#variable 'vowels' sets up the list of vowels to be used for checking

#is_vowel defines string as the only parameter
def is_vowel(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    #if condition checks if string is found in vowels
    if string in vowels:
        #if found in vowels it returns True
        return True
    #if not found in vowels it returns False
    else:
        return False

#-------------------
#variable 'vowels' sets up the list of vowels to be used for checking
#is_consonant defines string as the only parameter
def is_consonant(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    #checks if string is not included in vowels
    if string not in vowels:
        #if not then it returns True
        return True
    #otherwise, the function returns False
    else:
        return False
    
print(is_consonant('b'))
#-------------------
#variable 'vowels' sets up the list of vowels to be used for checking

#capitalize defines string as the only parameter
def capitalize(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    #finds if first letter of string is not in vowels
    if string[0] not in vowels:
        #the cap variable takes the first letter and capitalizes it
        #then it combines it with the rest of the string
        cap = string[0].upper() + string[1:]
        #returns cap variable back
        return cap

#-------------------
#calculate_tip defines percentage and bill_total as the parameters
def calculate_tip(percentage, bill_total):
    #calculates the amount of the tip base on percentage
    tip_amount = bill_total * percentage
    #returns the bill and percent amount to give the total amount of the bill with tip
    return (bill_total + tip_amount)


#-------------------
#apply_discount defines original and discount_percent as the parameters
def apply_discount(original, discount_percent):
    #after_discount is the amount that is going to be taken off original
    after_discount = original * discount_percent
    #returns the original amount with the discount applied
    return (original - after_discount)


#-------------------
#handle_commas defines str_num as the parameter
#handle_commas defines str_num as the parameter
def handle_commas(str_num):
    #starts a blank string
    new_str = ''
    #for loop to get each part of the string
    for i in str_num:
        #looks to see if that part is a comma
        if i == ',':
            #continue skips to the next i without adding to new_str
            continue
        if i == '$':
            continue
        else:
            #adds to new_str if part of string is not a comma
            new_str += i
    if '.' in new_str:
        return float(new_str)
    else:
    #returns the value of new_str as an integer
        return int(new_str)


#-------------------
#get_letter_grade defines num as the parameter
def get_letter_grade(num):
    #checks if greater or equal to 90
    if num >= 90:
        return 'A'
    #checks if greater or equal to 80
    elif num >= 80:
        return 'B'
    #checks if greater or equal to 70
    elif num >= 70:
        return 'C'
    #checks if greater or equal to 60
    elif num >= 60:
        return 'D'
    #if not any of the others then returns 'F'
    else:
        return 'F'

#-------------------
#variable 'vowels' sets up the list of vowels to be used for checking
#remove_vowels defines string_with_vowels as the parameter
def remove_vowels(string_with_vowels):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    #sets no_vowel_string as blank to be added to later
    no_vowel_string = ""
    #loops through every index of the parameter
    for i in string_with_vowels:
        #checks if i is in vowels, if it is it skips over
        if i in vowels:
            continue
        #if not in vowels then it adds to no_vowel_string
        else:
            no_vowel_string += i
    return no_vowel_string
            

#-------------------
#normalize_name defines identifier as the parameter
def normalize_name(identifier):
    #sets python_identifier as a blank string
    python_identifier = ""
    #loops through every char of the parameter
    for i in identifier:
        #checks for a space
        if i == ' ':
            #sets the space as an underscore
            python_identifier += '_'
        #checks for a percentage
        elif i == '%':
            #skips over it
            continue
        #adds all other characters to python_identifier
        else:
            python_identifier += i
    #checks if the first character is an underscore
    if python_identifier[0] == '_':
        #checks if last character is an underscore
        if python_identifier[-1] == '_':
            #if so, returns the string without them
            return python_identifier.lower()[1:-1]
        #returns the string with the first character gone
        else:
            return python_identifier.lower()[1:]
    #returns the string with the last character gone
    else:
        return python_identifier.lower()[:-1]
    #returns the string if there were no underscores in the beginning or end
    return python_identifier.lower()

#-------------------
#cumulative_sum defines list_num as the parameter
def cumulative_sum(list_num):
    #final_list is a blank list that will contain the final output
    final_list = []
    #for statement with range of len of list_num to give it a defined number to search through
    for i in range(len(list_num)):
        #finds the first value
        if i == 0:
            final_list.append(list_num[i])
        #runs all the other numbers of the list
        else:
            #finds the value of the previous number plus the one it is currently looking at
            value = final_list[i-1] + list_num[i]
            final_list.append(value)
    #returns the final answer
    return final_list

