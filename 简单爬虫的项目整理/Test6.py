'''
通过前三个数相加来生成下一个数据
'''
def tribonacci(signature, n):
    #your code here
    for i in range(n):
        signature.append(sum(signature[-3:]))
    return signature[:n]
    
ret = tribonacci([1, 1, 1], 10)       
print(ret) # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]