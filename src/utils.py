import pandas as pd
import sys,os
import yaml
import pickle

def read_yaml(file_path:str):
    ''' 
    read yaml file 
    '''
    try:
        with open(file_path,'r') as y:
            data=yaml.safe_load(y)

        return data
    except Exception as e:
        print(str(e))


def save_obj(file_path,obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as f:
            pickle.dump(f,obj)

            print(f'model save to {file_path}')
    except Exception as e:
        print(e)
