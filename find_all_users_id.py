from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """

    arr=[]
    d=data
    l=d["messages"]
    for i in l:
        if "actor_id" in i.keys():
            arr.append(i["actor_id"])
        if "from_id" in i.keys():
            arr.append(i["from_id"])  
    s=set(arr)  
    l=list(s)
    return l

path_file="data/result.json"
print(find_all_users_id(read_data(path_file)))

