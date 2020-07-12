# 某两个ip之间哪些地址ping的通，哪些ping不通

import time
import threading
import subprocess
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from ipaddress import ip_address  # 处理ip地址的标准库 ipaddress 模块，来处理ip地址的计算
import sys


class ping_ips():

    def get_ip_list(self, threading_num, ips, is_write):
        # 创建一个队列
        IP_QUEUE = Queue()
        ip_used = []
        ip_not_used = []
        ip_list = ips.split('-')
        ip_start = ip_address(ip_list[0])
        ip_end = ip_address(ip_list[1])

        while ip_start <= ip_end:
            IP_QUEUE.put(str(ip_start))
            ip_start += 1

        # 定义一个执行 ping 的函数

        def ping_ip(ip):
            res = subprocess.call('ping -n 2 -w 5 %s' %
                                  ip, stdout=subprocess.PIPE)
            # 打印运行结果
            print(ip, True if res == 0 else False)
            if lock.acquire():
                if res == 0:
                    ip_used.append(ip)
                else:
                    ip_not_used.append(ip)
                lock.release()

        # 创建一个最大任务为【threading_num】的线程池
        pool = ThreadPoolExecutor(max_workers=threading_num)
        lock = threading.Lock()
        start_time = time.time()
        all_task = []
        while not IP_QUEUE.empty():
            all_task.append(pool.submit(ping_ip, IP_QUEUE.get()))

        # 等待所有任务结束
        wait(all_task, return_when=ALL_COMPLETED)
        print('ping耗时：%s' % (time.time() - start_time))

        if is_write:
            with open('result1.txt', 'a', encoding='utf-8') as f:
                f.write("开始ping：\n")
                f.write("已用ip：\n")
                for ip in ip_used:
                    f.write("%s\n" % ip)
                f.write("未用ip：\n")
                for ip in ip_not_used:
                    f.write("%s\n" % ip)

        return ip_used, ip_not_used


if __name__ == '__main__':
    args = sys.argv
    ips = "110.37.231.1-110.37.231.10"
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
    pingips = ping_ips()
    ip_used, ip_not_used = pingips.get_ip_list(thread_num, ips, is_write)

    print(str(len(ip_used))+"已用", "\n", ip_used)
    print(str(len(ip_not_used))+"未用", "\n", ip_not_used)