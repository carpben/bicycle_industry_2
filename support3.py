import bicycle_industry

def sample_model_library ():
    models={}
    models['H1'] = bicycle_industry.Model(
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

    models['Mountain 100'] = bicycle_industry.Model(
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

    models['M1'] = bicycle_industry.Model(
        'M1',
        'Mountain',
        'Fine, Shock absorber.',
        ['Brown', 'Black'],
        {
            'Large': {'weight': 4.0, 'price': 500.0},
            'XXLarge': {'weight': 4.4, 'price': 550.0}
        }
    )

    models['City 100'] = bicycle_industry.Model(
        'City 100',
        'City',
        'Good, Stable.',
        ['Yellow', 'Green'],
        {
            'XLarge': {'weight': 3.3, 'price': 550.0},
            'Medium': {'weight': 3.0, 'price': 500.0}
        }
    )

    models['C1'] = bicycle_industry.Model(
        'C1',
        'City',
        'Fine, Stable.',
        ['Yellow', 'Green'],
        {
            'XLarge': {'weight': 3.3, 'price': 275.0},
            'Medium': {'weight': 3.0, 'price': 250.0}
        }
    )

    models['Highway 100'] = bicycle_industry.Model(
        'Highway 100',
        'HighWay',
        'Good, Lights, Stable.',
        ['Blue', 'Red'],
        {
            'Small': {'weight': 3.0, 'price': 2000.0},
            'Large': {'weight': 3.3, 'price': 2200.0}
        }
    )
    print models
    return models
