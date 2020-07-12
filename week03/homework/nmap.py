# 一个主执行文件，引用nmapb和nmapc文件，执行不同的功能
import sys
from nmapb import ping_ips
from nmapc import ScannerPort

if __name__ == '__main__':
    args = sys.argv
    oper = "ping"  # 默认执行nmapb文件
    is_write = True
    thread_num = 10

    if("-f" in args):
        # print("tcp")
        oper = args[args.index("-f") + 1]

    if("-w" in args):
        is_write = True
        print("是否把结果保存文件：", is_write)

    if("-n" in args):
        thread_num = int(args[args.index("-n") + 1])
        print("扫描的线程数为：", thread_num)

    if oper == "ping":
        ips = "110.37.231.1-110.37.231.10"

        if("-ip" in args):
            ips = args[args.index("-ip") + 1]
            print("扫描的IP的地址为：", ips)

        pingips = ping_ips()
        ip_used, ip_not_used = pingips.get_ip_list(thread_num, ips, is_write)

    if oper == "tcp":
        ip = "110.37.231.1"
        ports = list(range(1, 65535))  # 65535

        if("-ip" in args):
            ip = args[args.index("-ip") + 1]
            print("扫描的IP的地址为：", ip)

        scannerPort = ScannerPort()
        scannerPort.main(thread_num, ip, ports, is_write)