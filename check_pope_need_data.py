import os
import json
import random
SPLIT="llava_gqa_testdev_balanced"

in_file=f'/mnt2/kaijiejiao/LLaVA/playground/data/eval/pope/llava_pope_test.jsonl'
in_path='/mnt2/kaijiejiao/LLaVA/playground/data/eval/pope/val2014'
out_path='/mnt2/kaijiejiao/DG_Data/Need_Data/pope/val2014'
with open(in_file,'r') as fin:
    for i,item in enumerate(fin):
        item=eval(item)
        if i==0:
            print(item)

            # break
        # print(f"cp {in_path}/{item['image']} {out_path}/{item['image']}")
        os.system(f"cp {in_path}/{item['image']} {out_path}/{item['image']}")
        # if i>10:
        #     break
