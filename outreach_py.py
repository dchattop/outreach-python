import os
import configparser
import http.client
import json
from get_access_token import get_access_token
from get_outreach_resource import fetch_outreach_resource


# create global variables
path = os.getcwd()

# create list of all resources for which data needs to be fetched
resources = ['accounts', 'prospects', 'tasks', 'opportunities']


# derive absolute path for the cfg file
config_file_path = os.path.join(path,'config\outreach_constants.cfg')
config_obj = configparser.ConfigParser()
config_obj.read(config_file_path)

"""
get all config data from outreach_constants.cfg

"""
client_id = config_obj.get('outreach', 'client_id')
redirect_url = config_obj.get('outreach', 'redirect_url')
refresh_token= config_obj.get('outreach', 'outreach_refresh_token')
scope = config_obj.get('outreach', 'scope')
client_secret = config_obj.get('outreach', 'client_secret')

"""
get access_token using the refresh_token
"""
access_token = get_access_token(client_id,client_secret,redirect_url,refresh_token,'refresh_token')
print("access token generated successfully")

if __name__ == "__main__":

    """
    Args:
    
    fetch data for all resources mentioned in the list `resources`
    """
    for resource in resources:
        fetch_outreach_resource(resource,access_token)
        print(f"outreach_{resource}.json file fetched successfully!!")











