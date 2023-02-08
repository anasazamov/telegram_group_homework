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
    for i in data["messages"]:
        if "actor_id" in i.keys() or "from_id" in i.keys():
            if (i["type"]=="service" or i["type"]=="message") :
                if "actor_id" in i.keys():
                    if  not(i["actor_id"].startswith("channel")) :
                        arr.append(i["actor_id"])
                if "from_id" in i.keys():
                    if  not(i["from_id"].startswith("channel")) :    
                        arr.append(i["from_id"])  
    s=set(arr)  
    l=list(s)
    return l

path_file="data/result.json"
print(find_all_users_id(read_data(path_file)))

