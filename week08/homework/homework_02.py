# 自定义一个python函数，实现map()函数的功能

# def map(func, iter:iter):
#     result = []
#     for n in iter:
#         c = func(n)
#         result.append(c)
#     return result
#
def demo(a):
    return a ** 2

test = [i for i in range(1,11)]

# d = map(demo, test)
# print(d)
d = map(demo,test)
print(list(d))