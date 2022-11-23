import os
import timeit
import datetime

r = '192.168.3.0/24'
for i in range(1,101):
    start = timeit.default_timer()
    # Adjusted to  UDP SCAN
    os.system("sudo nmap -sT -sU {} -oN nmap_udp_logging/nmap_icmp_blocked_run_{}".format(r,i))
    stop = timeit.default_timer()
    total_time = stop - start
    net_class = "C"
    # output running time in a nice format.
    mins, secs = divmod(total_time, 60)
    hours, mins = divmod(mins, 60)
    time_csv = "%d:%d:%d.\n" %(hours, mins, secs)
    dt = datetime.datetime.now().strftime('%Y-%m-%d-%H%M')
    time_log = "{},{},{},{}".format(dt,r,net_class,time_csv)
    with open("nmap_udp_logging/nmap_only_class_C_ICMP_BLOCKED_time.csv","a+") as f:
        print("[*]Writing To Time Log[*]")
        f.write(time_log)
        print("[*]Time Log Updated[*]")