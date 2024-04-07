import os
import json
import random
SPLIT="llava_gqa_testdev_balanced"

in_file=f'/mnt2/kaijiejiao/LLaVA/playground/data/eval/MME/llava_mme.jsonl'
in_path='/mnt2/kaijiejiao/LLaVA/playground/data/eval/MME/MME_Benchmark_release_version'
out_path='/mnt2/kaijiejiao/DG_Data/Need_Data/MME/MME_Benchmark_release_version'
with open(in_file,'r') as fin:
    for i,item in enumerate(fin):
        item=eval(item)
        if i==0:
            print(item)
        directory = os.path.dirname(f"{out_path}/{item['image']}")
        if not os.path.exists(directory):
            os.makedirs(directory)


        # print(f"cp {in_path}/{item['image']} {out_path}/{item['image']}")
        os.system(f"cp {in_path}/{item['image']} {out_path}/{item['image']}")
        # if i>10:
        #     break
