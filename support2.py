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
        for size, details in self.sizes.items():
            s = "SIZE: {}\t WEIGHT: {} Kg\t COST: {} US$\n"
            sizes += s.format(size, details['weight'], details['price'])
            
        return "{}\n{}\n{}".format(model, colors, sizes)

def sample_model_library (models):
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
