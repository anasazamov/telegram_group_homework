from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    arr = []
    for i in data['messages']:
        if i['type'] == 'service':
            
                arr.append(i['actor'])
        elif i['type'] == 'message':
            
                arr.append(i['from'])
    
    return list( set( arr ))

path_file="data/result.json"
data=read_data(path_file)
print(find_all_users_name(data))



