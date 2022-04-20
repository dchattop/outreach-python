import os
import pandas as pd
import json


path = os.getcwd()
op_file_path = os.path.join(path, 'output')
json_file_path = os.path.join(op_file_path,'outreach_prospects.json')
# print(json_file_path)
data_ = json.load(open(json_file_path))

print(pd.json_normalize(data_, record_path='data'))
