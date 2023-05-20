acronyms={}

def return_acronym(key):
    return acronyms.get(key)
    

file_path="C:/Users/seana/Desktop/Programming/Python/Pluralsight Files/python-3-fundamentals/08/demos/demos"


with open(file_path+"/software_acronyms.txt") as acronym_file:
    
    for line in acronym_file:
        parsed_line=line.rsplit(sep=' - ')
        acro_key=parsed_line[0]
        acro_def=parsed_line[1]
        acronyms[acro_key]=acro_def.removesuffix('\n')
        
print(acronyms)
find_acronym = input("What acronym do you need the defintion for? (type 'EXIT' to quit)\n")

while find_acronym !='EXIT':
    search_result = return_acronym(find_acronym)
    
    if search_result==None:
        print("\n",find_acronym, "was not found")
    else:
        print("\nThe acronym",find_acronym,"means",search_result)
    
    find_acronym = input("\nWhat acronym do you need the defintion for? (type 'EXIT' to quit)\n")