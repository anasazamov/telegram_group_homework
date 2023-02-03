from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    arr=[]
    d=data
    l=d["messages"]
    for i in l[:32]:
        if "actor" in i.keys():
            arr.append(i["actor"])
        if "from" in i.keys():
            arr.append(i["from"])
    return arr

path_file="data/result.json"
print(find_all_users_name(read_data(path_file)))



