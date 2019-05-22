'''
模块：random
大纲：随机数、随机序列、随机多个
随机数：
    random()        #[0,1]
    randint(1,10)   #[1,10]
    randrange(1,10) #[1,10)
随机序列：
    choice([x for x in range(1,10)])
随机多个：
    sample(序列,随机个数)
-------------------------------------------------------------------------------------------
'''
import random
#随机数
# print(random.random())      #[0,1]
# print(random.randint(1,2))  #[1,2]
# print(random.randrange(1,2)) #不包括2
#随机序列
print(random.choice("asddfghjkl"))
#随机多个序列
print(random.sample("asdfghjkl",3)) #return list列表形式