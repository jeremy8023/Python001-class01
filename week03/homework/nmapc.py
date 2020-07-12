# 多线程+socket写一个端口扫描器

import socket
import threading
import time
import sys
from queue import Queue
import json


class ScannerPort():
    # 参照老师的demo，创建一个继承threading.Thread的扫描端口类
    class ScanPorts (threading.Thread):
        def __init__(self, ip, portlist, timeout, result_dic):
            threading.Thread.__init__(self)
            self.ip = ip
            self.portlist = portlist
            self.timeout = timeout
            self.result_dic = result_dic

        def run(self):

            while True:
                if self.portlist.empty():
                    break
                ip = self.ip
                port = self.portlist.get()
                timeout = self.timeout

                try:
                    ''' 
                        有两种类型的套接字：基于文件的:AF_UNIX和面向网络的:AF_INET
                        1、面向连接的套接字
                            TCP套接字的名字SOCK_STREAM。
                            特点：可靠，开销大
                        2、无连接的套接字
                            UDP套接字的名字SOCK_DGRAM
                            特点：不可靠（局网内还是比较可靠的），开销小
                    '''
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.settimeout(timeout)
                    result = s.connect_ex((ip, port))
                    # print(result)
                    if result == 0:
                        self.result_dic[port] = '[OPEN]'
                        print("%s [OPEN]" % port)
                    else:
                        self.result_dic[port] = '[CLOSE]'
                        print("%s [CLOSE]" % port)
                except:
                    self.result_dic[port] = '[CLOSE]'
                finally:
                    s.close()

            return self.result_dic

    def main(self, thread_num, ip, ports, is_write):
        start_time = time.time()
        threads = []
        port_queue = Queue()
        timeout = 2
        port_scanner = ScannerPort()
        result_dic = {}  # 扫描端口结果

        for i in ports:
            port_queue.put(i)

        for i in range(thread_num):
            threads.append(port_scanner.ScanPorts(
                ip, port_queue, timeout, result_dic))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        if is_write:
            with open('result2.txt', 'a', encoding='utf-8') as f:
                f.write("扫描ip%s端口：\n" % ip)
                # 遍历字典列表
                for key, values in result_dic.items():
                    f.write("%s : %s\n" % (key, values))

        print("耗时：", time.time() - start_time, "s")


if __name__ == "__main__":
    args = sys.argv
    ip = "110.37.231.1"
    ports = list(range(1, 1024))  # 65535 控制端口范围，也可以做成参数
    thread_num = 10
    is_write = False

    if("-ip" in args):
        ip = args[args.index("-ip") + 1]
        print("扫描的IP的地址为：", ip)

    if("-n" in args):
        thread_num = int(args[args.index("-n") + 1])
        print("扫描的线程数为：", thread_num)
    if("-w" in args):
        is_write = True
        print("是否把结果保存文件：", is_write)
    scannerPort = ScannerPort()
    scannerPort.main(thread_num, ip, ports, is_write)