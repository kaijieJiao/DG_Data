import os
import json
import random
SPLIT="llava_gqa_testdev_balanced"
image_path='vqav2/test2015'
in_file=f'/mnt2/kaijiejiao/LLaVA/playground/data/eval/vqav2/llava_vqav2_mscoco_test-dev2015.jsonl'
in_path=f'/mnt2/kaijiejiao/LLaVA/playground/data/eval/{image_path}'
out_path=f'/mnt2/kaijiejiao/DG_Data/Need_Data/{image_path}'
with open(in_file,'r') as fin:
    # all_data=json.load(fin)
    for i,item in enumerate(fin):
        item=eval(item)
        if i==0:
            print(item)
        if 'image' in item:

            directory = os.path.dirname(f"{out_path}/{item['image']}")
            if not os.path.exists(directory):
                os.makedirs(directory)

        # print(f"cp {in_path}/{item['image']} {out_path}/{item['image']}")
            os.system(f"cp {in_path}/{item['image']} {out_path}/{item['image']}")
        # if i>10:
        #     break
