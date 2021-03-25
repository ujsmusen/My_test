# -----------------------随机生成5个微信原始ID-----------------------开始
import random

for j in range(5):
    id_str = 'wxid_'
    for i in range(14):
        temp = random.choice('0123456789abcdefghijklmnopqrstuvwxyz')
        id_str = id_str + temp
    print(id_str)
# -----------------------随机生成5个微信原始ID-----------------------结束
