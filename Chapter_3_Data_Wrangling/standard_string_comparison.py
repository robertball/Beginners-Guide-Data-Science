example = 'Queen of England'
if 'Queen' in example:  # Preferred method
    print('contains example 1')  

if example.__contains__('Queen'):  # Using the __ functions is frowned upon.
    print('contains example 2')

