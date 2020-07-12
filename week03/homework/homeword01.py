'''
    1.使用argprase模块，解决命令行传参数；see: https://zhuanlan.zhihu.com/p/28871131
'''
import argparse

def get_parse():
    parser = argparse.ArgumentParser(description='The Program of Scan Port')
    parser.add_argument('-n', required=True, choices=[1, 2, 3, 4, 5, 6, 7, 8])
    parser.add_argument('-f', required=True, choices=['tcp', 'ping'])
    parser.add_argument('-ip', required=True, )
    parser.add_argument('-w', required=True, )

    return parser

if __name__ =='__maim__':
    parser = get_parse()
    args = parser.parse_args()
    print(args)