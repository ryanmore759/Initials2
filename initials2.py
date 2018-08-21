def get_initials(full_name):
    complete_name = full_name.title()
    list_of_names = complete_name.split()
    two_name = list_of_names
    number_of_names = len(list_of_names)
    
    if(number_of_names == 2):
        first_names = list_of_names[:0]
        initials = ''.join(name[0] for name in first_names)
        initials2 = ''.join(name[0] for name in two_name)
        return initials + initials2    
    
    else:
        initials = ''.join(name[0] for name in two_name)
        return initials        

def main():
   full_name = input('Please enter your full name:\n')
   print("The initials of input name are",(get_initials(full_name)))

if __name__ == '__main__':
    main()