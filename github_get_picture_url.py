import os
import json
import
in_file='/mnt2/kaijiejiao/DG_Data/Need_Data/gqa/llava_gqa_testdev_balanced.jsonl'
picture_path='/mnt2/kaijiejiao/DG_Data/Need_Data'
with open(in_file,'r') as fin:
    for i,item in enumerate(fin):
        item=eval(item)
        if i==0:
            print(item)
        os.system(f"git add {picture_path}/{item['image']}")
        