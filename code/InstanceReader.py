import pandas as pd
import numpy as np

def read_instance(path):
    df = pd.read_excel(path)
    instance_dict = {}
    attraction_num = np.squeeze(df.loc[0].values)[0]
    visitor_num = np.squeeze(df.loc[2].values)[0]
    
    visitor_info = pd.DataFrame({'visitor_index': [x for x in range(visitor_num)],
                                 'time_limit': df.loc[4].values[0:10]})
    attraction_info = pd.DataFrame({'attraction_index': ['e']+[x for x in range(attraction_num)]+['h'], 
                                   'attraction_reward': df.loc[6].values[:attraction_num+2],
                                    'serve_time': df.loc[8].values[:attraction_num+2]})
    
    attraction_distance_map = pd.DataFrame(df.loc[10: 10+attraction_num+2].dropna(axis=1).values, 
                                           columns=['e']+[x for x in range(attraction_num)]+['h'], 
                                           index=['e']+[x for x in range(attraction_num)]+['h'])    
    return {'visitor_info': visitor_info, 'attraction_info': attraction_info, 'attraction_distance_map': attraction_distance_map}