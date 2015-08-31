def text_input(question):
    """Like input, but we doesn't allow empty input"""
    value = input(question)
    while value.strip() == "":
        value = input("Value can't be empty")
    return value

def int_input(question):
    while True:
        try:
            value = int(text_input(question))
            return value
        except ValueError:
            print("Please enter an integer")
            
def positive_int_input(question):
    value = int_input(question)
    while value<0:
        value = int_input("Please enter a positive integer")
    return value

def float_input(question):
    while True:
        try:
            value = float(text_input(question))
            return value
        except ValueError:
            print("Please enter a number.\t")
            
def positive_float_input(question):
    value = float_input(question)
    while value<0:
        value = float_input("Please enter a non negative number.\t")
    return value

def int_input_in_range (question, mini, maxi):
    # presents question/string, and returns integer in range. 
    value = int_input(question)
    while value<mini or value>maxi:
        value = int_input("Invalid option. Please enter integer in range.\t")
    return value
    
def int_input_in_lst (question, lst): 
    # Presents question/string, and returns integer in list. 
    value = int_input(question)
    while value not in lst:
        value = int_input("Invalid option. Please try again.\t")
    return value
    
def yes_or_no (question):
    print (question,) 
    value = (text_input("Y(es)/N(o)\t"))
    value=value.lower()
    while value not in ["y", "yes", "n", "no"]:
        value = (text_input("Answer should be one of y, yes, n or no\t"))
        value=value.lower()
    return value in ["y", "yes"]
    
def choose_one_from_list(lst): 
    for index, item in enumerate(lst):
        print ("\t{} - {}".format(index + 1, item))
    index = int_input_in_range("Choose an option by number:\t", 1, len(lst)) - 1
    return index, lst[index]

def choose_many_from_list (lst): 
    lst_to_return = []
    index_lst = [] 
    # For convenience we will build list of indexs, and convert to list of values at the end. 
    # There is a difference between the list indexes which are from 0 and the index for user which is from 1. 
    
    for index, item in enumerate(lst):
        print ("\t{} - {}".format(index + 1, item))
    index = int_input_in_range("Add an option by number:\t", 1, len(lst)) - 1
    index_lst.append(index)
        
    while len(index_lst)<len(lst): # The loop ends when all list items were choosen, or when user enters 0.  
        for index, item in enumerate(lst):
            print ("\t{} - {}".format(index + 1, item), end=" ")
            if index in index_lst:
                print (" (Selected)")
            else: 
                print ()
        allowed_ints = [i for i in range(len(lst)+1) if (i-1) not in index_lst]
        index = int_input_in_lst("Add an option by number, or enter 0 to continue:\t", allowed_ints) - 1
        if index ==-1: 
            break
        index_lst.append(index)
    index_lst.sort()
    lst_to_return=[lst[i] for i in index_lst]
    return lst_to_return