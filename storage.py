#ShowerBud Team 105
def write_file(filename:str, variable:str):
    with open(filename, 'w') as my_file:
        my_file.write(str(variable))
        
def read_file(filename:str):
    with open(filename) as my_file:
        return my_file.read()        
