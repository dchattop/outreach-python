import json
import os
import http.client

path = os.getcwd()
conn_ = http.client.HTTPSConnection("api.outreach.io")
op_file_path = os.path.join(path, 'output')

def fetch_outreach_resource(resource, token):
    op_json_file_path = os.path.join(op_file_path, f"outreach_{resource}.json")
    auth_header = {"Authorization": f"Bearer {token}"}
    conn_.request('GET', f"/api/v2/{resource}","", auth_header)
    res_ = conn_.getresponse()
    if res_.status==200:
        data_ = res_.read()
        data_json_ = json.loads(data_)
        with open(op_json_file_path, "w") as fp:
            json.dump(data_json_, fp)
        # return data_json_