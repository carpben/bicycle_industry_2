import support
import support2

class Model(object):
    def __init__(self, name, category, description, colors, sizes):
        self.name = name
        self.category = category
        self.description = description
        self.colors = colors
        self.sizes = sizes

    def __str__(self):

        model = "MODEL NAME: {}\t CATEGORY: {}\t DESCRIPTION: {}".format(self.name, self.category, self.description)

        colors = "COLOR SELECTION:"
        for color in self.colors:
            colors += "\t{}".format(color)

        sizes = ""
        for size, details in self.sizes.iteritems():
            s = "SIZE: {}\t WEIGHT: {} Kg\t COST: {} US$\n"
            sizes += s.format(size, details['weight'], details['price'])
            
        return "{}\n{}\n{}".format(model, colors, sizes)

def make_model(models):
    name = support.text_input("Model name: ")

    print ("Choose a category:   ")
    _, category = support.choose_one_from_list(CATEGORIES)

    description = support.text_input("Description: ")

    print ("Add color options:")
    colors = support.choose_many_from_list(COLORS)

    print ("Add size options:")
    # This includes size selection, and additional info for each size
    size_lst = support.choose_many_from_list(SIZES)
    sizes = {x: {} for x in size_lst}

    for size in size_lst:
        print ("\nMODEL:\t{}\tSIZE:\t{}".format(name, size))
        sizes[size]['weight'] = support.positive_float_input("Enter weight (Kg): ")
        sizes[size]['price'] = support.positive_float_input("Enter cost (US $): ")
    
    print
    models[name]=Model(name, category, description, colors, sizes)

def make_models(models):
    another = True
    while another:
        make_model(models)
        another = support.yes_or_no("Would you like to add another model?")
"""
option2
import support3
def sample_model_library():
    models = support3.sample_model_library()
    print models
"""
def sample_model_library(): # Option3
    models['H1'] = Model(
        'H1',
        'HighWay',
        'Fine, Lights, Stable.',
        ['Blue', 'Red'],
        {
            'Small': {
                'weight': 3.0,
                'price': 1000.0
            },
            'Large': {
                'weight': 3.3,
                'price': 1100.0
            }
        }
    )

    models['Mountain 100'] = Model(
        'Mountain 100',
        'Mountain',
        'Good, Shock absorber.',
        ['Brown', 'Black'],
        {
            'Large': {
                'weight': 4.0,
                'price': 1000.0
            },
            'XXLarge': {
                'weight': 4.4,
                'price': 1100.0
            }
        }
    )

    models['M1'] = Model(
        'M1',
        'Mountain',
        'Fine, Shock absorber.',
        ['Brown', 'Black'],
        {
            'Large': {'weight': 4.0, 'price': 500.0},
            'XXLarge': {'weight': 4.4, 'price': 550.0}
        }
    )

    models['City 100'] = Model(
        'City 100',
        'City',
        'Good, Stable.',
        ['Yellow', 'Green'],
        {
            'XLarge': {'weight': 3.3, 'price': 550.0},
            'Medium': {'weight': 3.0, 'price': 500.0}
        }
    )

    models['C1'] = Model(
        'C1',
        'City',
        'Fine, Stable.',
        ['Yellow', 'Green'],
        {
            'XLarge': {'weight': 3.3, 'price': 275.0},
            'Medium': {'weight': 3.0, 'price': 250.0}
        }
    )

    models['Highway 100'] = Model(
        'Highway 100',
        'HighWay',
        'Good, Lights, Stable.',
        ['Blue', 'Red'],
        {
            'Small': {'weight': 3.0, 'price': 2000.0},
            'Large': {'weight': 3.3, 'price': 2200.0}
        }
    )

def print_bicycle_models ():
    print ("\nPRINTING BICYCLE MODELS\n") 
    for name, model in models.iteritems():
        print (model)
    
class Bicycle(object):
    def __init__ (self, ide, model, color, size):
        self.ide = ide
        self.model = model
        self.color = color
        self.size = size
        company_inventory.append(ide)
    """
    def __str__(self):
        text="bicycles[{}] = Bicycle ({}, '{}', '{}', '{}'), "
        text=text.format(self.ide,self.ide,self.model, self.color, self.size) 
        return text
    """
    def __str__(self):
        s = "ID:{}\tMODEL:{}\t COLOR:{}\t SIZE:{}"
        return s.format(self.ide, self.model, self.color, self.size)

count=0
def bicycle_production():
    print ("Choose a model from list of models: ")
    names = map(lambda model: model.name, models.itervalues())
    _, name = support.choose_one_from_list(names)

    print ("Choose color from selection of colors for model", name, ":")
    _, color = support.choose_one_from_list(models[name].colors)

    _, size = support.choose_one_from_list(models[name].sizes.keys())

    s = "How many Bicycles to manufacture of\t"
    s += "MODEL: \t{} \t COLOR: \t{} \tSIZE: \t{}?"
    print (s.format(name, color, size))

    quantity = support.positive_int_input("Type Quantity: ")
    global count
    for i in range(quantity):
        ide=count
        bicycles[ide]=Bicycle(ide, name, color, size)
        count+=1

def make_bicycles():
    another = True
    while another:
        bicycle_production()
        another = support.yes_or_no("Would you like to add another order of bicycles?")

def sample_bicycle_library():
    bicycles[0] = Bicycle (0, 'M1', 'Brown', 'Large') 
    bicycles[1] = Bicycle (1, 'M1', 'Brown', 'Large') 
    bicycles[2] = Bicycle (2, 'M1', 'Brown', 'Large') 
    bicycles[3] = Bicycle (3, 'M1', 'Brown', 'Large') 
    bicycles[4] = Bicycle (4, 'M1', 'Brown', 'Large') 
    bicycles[5] = Bicycle (5, 'M1', 'Brown', 'Large') 
    bicycles[6] = Bicycle (6, 'M1', 'Brown', 'Large') 
    bicycles[7] = Bicycle (7, 'M1', 'Brown', 'Large') 
    bicycles[8] = Bicycle (8, 'M1', 'Brown', 'Large') 
    bicycles[9] = Bicycle (9, 'M1', 'Brown', 'Large') 
    bicycles[10] = Bicycle (10, 'M1', 'Black', 'Large') 
    bicycles[11] = Bicycle (11, 'M1', 'Black', 'Large') 
    bicycles[12] = Bicycle (12, 'M1', 'Black', 'Large') 
    bicycles[13] = Bicycle (13, 'M1', 'Black', 'Large') 
    bicycles[14] = Bicycle (14, 'M1', 'Black', 'Large') 
    bicycles[15] = Bicycle (15, 'M1', 'Black', 'Large') 
    bicycles[16] = Bicycle (16, 'M1', 'Black', 'Large') 
    bicycles[17] = Bicycle (17, 'M1', 'Black', 'Large') 
    bicycles[18] = Bicycle (18, 'M1', 'Black', 'Large') 
    bicycles[19] = Bicycle (19, 'M1', 'Black', 'Large') 
    bicycles[20] = Bicycle (20, 'M1', 'Black', 'XXLarge') 
    bicycles[21] = Bicycle (21, 'M1', 'Black', 'XXLarge') 
    bicycles[22] = Bicycle (22, 'M1', 'Black', 'XXLarge') 
    bicycles[23] = Bicycle (23, 'M1', 'Black', 'XXLarge') 
    bicycles[24] = Bicycle (24, 'M1', 'Black', 'XXLarge') 
    bicycles[25] = Bicycle (25, 'M1', 'Black', 'XXLarge') 
    bicycles[26] = Bicycle (26, 'M1', 'Black', 'XXLarge') 
    bicycles[27] = Bicycle (27, 'M1', 'Black', 'XXLarge') 
    bicycles[28] = Bicycle (28, 'Mountain 100', 'Brown', 'Large') 
    bicycles[29] = Bicycle (29, 'Mountain 100', 'Brown', 'Large') 
    bicycles[30] = Bicycle (30, 'Mountain 100', 'Brown', 'Large') 
    bicycles[31] = Bicycle (31, 'Mountain 100', 'Brown', 'Large') 
    bicycles[32] = Bicycle (32, 'Mountain 100', 'Brown', 'Large') 
    bicycles[33] = Bicycle (33, 'Mountain 100', 'Black', 'Large') 
    bicycles[34] = Bicycle (34, 'Mountain 100', 'Black', 'Large') 
    bicycles[35] = Bicycle (35, 'Mountain 100', 'Black', 'Large') 
    bicycles[36] = Bicycle (36, 'Mountain 100', 'Black', 'Large') 
    bicycles[37] = Bicycle (37, 'Mountain 100', 'Black', 'Large') 
    bicycles[38] = Bicycle (38, 'Mountain 100', 'Black', 'XXLarge') 
    bicycles[39] = Bicycle (39, 'Mountain 100', 'Black', 'XXLarge') 
    bicycles[40] = Bicycle (40, 'Mountain 100', 'Black', 'XXLarge') 
    bicycles[41] = Bicycle (41, 'C1', 'Yellow', 'Medium') 
    bicycles[42] = Bicycle (42, 'C1', 'Yellow', 'Medium') 
    bicycles[43] = Bicycle (43, 'C1', 'Yellow', 'Medium') 
    bicycles[44] = Bicycle (44, 'C1', 'Yellow', 'Medium') 
    bicycles[45] = Bicycle (45, 'C1', 'Yellow', 'Medium') 
    bicycles[46] = Bicycle (46, 'C1', 'Yellow', 'Medium') 
    bicycles[47] = Bicycle (47, 'C1', 'Yellow', 'Medium') 
    bicycles[48] = Bicycle (48, 'C1', 'Yellow', 'Medium') 
    bicycles[49] = Bicycle (49, 'C1', 'Yellow', 'Medium') 
    bicycles[50] = Bicycle (50, 'C1', 'Yellow', 'Medium') 
    bicycles[51] = Bicycle (51, 'C1', 'Green', 'Medium') 
    bicycles[52] = Bicycle (52, 'C1', 'Green', 'Medium') 
    bicycles[53] = Bicycle (53, 'C1', 'Green', 'Medium') 
    bicycles[54] = Bicycle (54, 'C1', 'Green', 'Medium') 
    bicycles[55] = Bicycle (55, 'C1', 'Green', 'Medium') 
    bicycles[56] = Bicycle (56, 'C1', 'Green', 'Medium') 
    bicycles[57] = Bicycle (57, 'C1', 'Green', 'Medium') 
    bicycles[58] = Bicycle (58, 'C1', 'Green', 'Medium') 
    bicycles[59] = Bicycle (59, 'C1', 'Green', 'Medium') 
    bicycles[60] = Bicycle (60, 'C1', 'Green', 'Medium') 
    bicycles[61] = Bicycle (61, 'C1', 'Green', 'XLarge') 
    bicycles[62] = Bicycle (62, 'C1', 'Green', 'XLarge') 
    bicycles[63] = Bicycle (63, 'C1', 'Green', 'XLarge') 
    bicycles[64] = Bicycle (64, 'C1', 'Green', 'XLarge') 
    bicycles[65] = Bicycle (65, 'C1', 'Green', 'XLarge') 
    bicycles[66] = Bicycle (66, 'City 100', 'Yellow', 'Medium') 
    bicycles[67] = Bicycle (67, 'City 100', 'Yellow', 'Medium') 
    bicycles[68] = Bicycle (68, 'City 100', 'Yellow', 'Medium') 
    bicycles[69] = Bicycle (69, 'City 100', 'Yellow', 'Medium') 
    bicycles[70] = Bicycle (70, 'City 100', 'Yellow', 'Medium') 
    bicycles[71] = Bicycle (71, 'City 100', 'Green', 'Medium') 
    bicycles[72] = Bicycle (72, 'City 100', 'Green', 'Medium') 
    bicycles[73] = Bicycle (73, 'City 100', 'Green', 'Medium') 
    bicycles[74] = Bicycle (74, 'City 100', 'Green', 'Medium') 
    bicycles[75] = Bicycle (75, 'City 100', 'Green', 'Medium') 
    bicycles[76] = Bicycle (76, 'City 100', 'Green', 'XLarge') 
    bicycles[77] = Bicycle (77, 'City 100', 'Green', 'XLarge') 
    bicycles[78] = Bicycle (78, 'City 100', 'Green', 'XLarge') 
    bicycles[79] = Bicycle (79, 'H1', 'Blue', 'Small') 
    bicycles[80] = Bicycle (80, 'H1', 'Blue', 'Small') 
    bicycles[81] = Bicycle (81, 'H1', 'Blue', 'Small') 
    bicycles[82] = Bicycle (82, 'H1', 'Blue', 'Small') 
    bicycles[83] = Bicycle (83, 'H1', 'Blue', 'Small') 
    bicycles[84] = Bicycle (84, 'H1', 'Red', 'Small') 
    bicycles[85] = Bicycle (85, 'H1', 'Red', 'Small') 
    bicycles[86] = Bicycle (86, 'H1', 'Red', 'Small') 
    bicycles[87] = Bicycle (87, 'H1', 'Red', 'Small') 
    bicycles[88] = Bicycle (88, 'H1', 'Red', 'Small') 
    bicycles[89] = Bicycle (89, 'H1', 'Blue', 'Large') 
    bicycles[90] = Bicycle (90, 'H1', 'Blue', 'Large') 
    bicycles[91] = Bicycle (91, 'H1', 'Blue', 'Large') 
    bicycles[92] = Bicycle (92, 'H1', 'Blue', 'Large') 
    bicycles[93] = Bicycle (93, 'H1', 'Blue', 'Large') 
    bicycles[94] = Bicycle (94, 'H1', 'Red', 'Large') 
    bicycles[95] = Bicycle (95, 'H1', 'Red', 'Large') 
    bicycles[96] = Bicycle (96, 'H1', 'Red', 'Large') 
    bicycles[97] = Bicycle (97, 'H1', 'Red', 'Large') 
    bicycles[98] = Bicycle (98, 'H1', 'Red', 'Large') 
    bicycles[99] = Bicycle (99, 'Highway 100', 'Blue', 'Small') 
    bicycles[100] = Bicycle (100, 'Highway 100', 'Blue', 'Small') 
    bicycles[101] = Bicycle (101, 'Highway 100', 'Red', 'Small') 
    bicycles[102] = Bicycle (102, 'Highway 100', 'Red', 'Small') 
    bicycles[103] = Bicycle (103, 'Highway 100', 'Blue', 'Large') 
    bicycles[104] = Bicycle (104, 'Highway 100', 'Blue', 'Large') 
    bicycles[105] = Bicycle (105, 'Highway 100', 'Red', 'Large') 
    bicycles[106] = Bicycle (106, 'Highway 100', 'Red', 'Large')

def print_bicycles ():
    print ("PRINTING ALL PRODUCED BICYCLES")
    for ide, bicycle in bicycles.iteritems():
        print (bicycle)
    
company_inventory = []
company_margin=0.25

"""
def price_to_shop (model_name, size): 
    return models[model_name]['sizes'][size]['cost']*(1+company_margin)
"""
def bicycle_info_for_shops():
    pass
    
def main(): 
    CATEGORIES = ["Mountain", "City", "HighWay"]
    SIZES = ["XSmall", "Small", "Medium", "Large", "XLarge", "XXLarge"]
    COLORS = ["White", "Yellow", "Green", "Blue", "Red", "Brown", "Purple", "Gray", "Black"]
    
    models={}
    bicycles = {}
    
    print ("\nWelcome to Bicycle Industry Model.")
    print ("\nLets start with creating bicycle models.") 

    choice1, _ = support.choose_one_from_list(["Let's create some models!",
                                               "Use sample model library"])
    if choice1 == 1:
        #option1 
        support2.sample_model_library(models) 
        """
        option2
        sample_model_library()
        sample_model_library()  option3
        """
    else:
        make_models(models)

    print_bicycle_models()

    print ("Lets create some bicycles.")
    shortcut=False
    if choice1==1: 
        choice2, _ = support.choose_one_from_list(["Let's create some Bicycles!",
                                                  "Use sample bicycle library"])
        if choice2==1: 
            shortcut=True
    if shortcut:    
        sample_bicycle_library()
    else:
        make_bicycles()
        
    print_bicycles()

    print ("\nLets open some shops") 

if __name__ == "__main__":
    main()
