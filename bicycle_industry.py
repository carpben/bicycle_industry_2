from support import text_input, int_input, positive_int_input, float_input 
from support import positive_float_input, int_input_in_range, int_input_in_lst
from support import yes_or_no, choose_one_from_list, choose_many_from_list
from support2 import sample_model_library, Model 
from support3 import sample_bicycle_library, Bicycle

def make_model(models, CATEGORIES, COLORS, SIZES):
    name = text_input("Model name: ")

    print ("Choose a category:   ")
    _, category = choose_one_from_list(CATEGORIES)

    description = text_input("Description: ")

    print ("Add color options:")
    colors = choose_many_from_list(COLORS)

    print ("Add size options:")
    # This includes size selection, and additional info for each size
    size_lst = choose_many_from_list(SIZES)
    sizes = {x: {} for x in size_lst}

    for size in size_lst:
        print ("\nMODEL:\t{}\tSIZE:\t{}".format(name, size))
        sizes[size]['weight'] = positive_float_input("Enter weight (Kg): ")
        sizes[size]['price'] = positive_float_input("Enter cost (US $): ")
    
    print
    models[name]=Model(name, category, description, colors, sizes)

def make_models(models, CATEGORIES, COLORS, SIZES):
    another = True
    while another:
        make_model(models, CATEGORIES, COLORS, SIZES)
        another = yes_or_no("Would you like to add another model?")

def print_bicycle_models (models):
    print ("\nPRINTING BICYCLE MODELS\n") 
    for model in models.values():
        print (model)

count=0
def bicycle_production(bicycles, models, company_inventory):
    print ("Choose a model from list of models: ")
    names = list(map(lambda model: model.name, models.values()))
    _, name = choose_one_from_list(names)

    print ("Choose color from selection of colors for model", name, ":")
    _, color = choose_one_from_list(models[name].colors)
    
    _, size = choose_one_from_list(list(sorted(models[name].sizes.keys())))

    s = "How many Bicycles to manufacture of\t"
    s += "MODEL: \t{} \t COLOR: \t{} \tSIZE: \t{}?"
    print (s.format(name, color, size))

    quantity = positive_int_input("Type Quantity: ")
    global count
    for i in range(quantity):
        ide=count
        bicycles[ide]=Bicycle(ide, name, color, size, company_inventory)
        count+=1

def make_bicycles(bicycles, models, company_inventory):
    another = True
    while another:
        bicycle_production(bicycles, models, company_inventory)
        another = yes_or_no("Would you like to add another order of bicycles?")

def print_bicycles (bicycles):
    print ("PRINTING ALL PRODUCED BICYCLES")
    for ide, bicycle in bicycles.items():
        print (bicycle)
    
company_inventory = []
company_margin=0.25

def bicycle_info_for_shops():
    pass
    
def main(): 
    
    CATEGORIES = ["Mountain", "City", "HighWay"]
    SIZES = ["XSmall", "Small", "Medium", "Large", "XLarge", "XXLarge"]
    COLORS = ["White", "Yellow", "Green", "Blue", "Red", "Brown", "Purple", "Gray", "Black"]
    
    models={}
    bicycles = {}
    company_inventory = []
    
    print ("\nWelcome to Bicycle Industry Model.")
    print ("\nLets start with creating bicycle models.") 

    choice1, _ = choose_one_from_list(
        ["Let's create some models!", "Use sample model library"]
        )
    if choice1 == 1:
        sample_model_library(models) 
    else:
        make_models(models, CATEGORIES, COLORS, SIZES)
    print_bicycle_models(models)

    print ("Lets create some bicycles.")
    shortcut=False
    if choice1==1: 
        choice2, _ = choose_one_from_list(
            ["Let's create some Bicycles!", "Use sample bicycle library"]
            )
        if choice2==1: 
            shortcut=True
    if shortcut:    
        sample_bicycle_library(bicycles, company_inventory)
    else:
        make_bicycles(bicycles, models, company_inventory)
        
    print_bicycles(bicycles)

if __name__ == "__main__":
    main()
