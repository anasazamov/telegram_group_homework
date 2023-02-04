from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    ids = []
    for msg in data['messages']:
        if msg['type'] == 'service':
            if msg['actor'] not in ids:
                ids.append(msg['actor'])
        elif msg['type'] == 'message':
            if msg['from'] not in ids:
                ids.append(msg['from'])
    
    return ids
path_file="data/result.json"
data=read_data(path_file)
print(find_all_users_name(data))



