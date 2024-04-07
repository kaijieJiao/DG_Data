import os
import json
import random
SPLIT="llava_gqa_testdev_balanced"

in_file=f'/mnt2/kaijiejiao/LLaVA/playground/data/eval/gqa/{SPLIT}.jsonl'
in_path='/mnt2/kaijiejiao/LLaVA/playground/data/eval/gqa/data/images'
out_path='/mnt2/kaijiejiao/DG_Data/Need_Data/gqa/data/images'
with open(in_file,'r') as fin:
    for i,item in enumerate(fin):
        item=eval(item)
        if i==0:
            print(len(fin))
            print(item)
        # print(f"cp {in_path}/{item['image']} {out_path}/{item['image']}")
        os.system(f"cp {in_path}/{item['image']} {out_path}/{item['image']}")
        # if i>10:
        #     break
