import re
import pandas as pd
import os

for i in range(50,200, 20):
    for j in range(1,200,20):
        os.system("python3 slot4.py %s %s" %(i,j))

with open('depthfeatures_nonintel.txt') as fd:
    data = fd.read()

val_to_pattern = {
    'Depth': r'Depth = (\d+)',
    'Test size': r'Test size = (\-?\d+\.\d+)',
    'Max Features' : r'Max Features = (\-?\d+\.\d+)',
    'Samples' : r'Samples = (\d+)',
    'Accuracy': r'Accuracy = (\-?\d+\.\d+)',
    'Dataset Time': r'Dataset Time = (\-?\d+\.\d+)',
    'Training Time': r'Training Time = (\-?\d+\.\d+)',
    'Total Time': r'Total Time = (\-?\d+\.\d+)',
}
    
   

val_dict = {}
for key, patt in val_to_pattern.items():
    val_dict[key] = re.findall(patt, data)

df = pd.DataFrame.from_dict(val_dict)
print(df)