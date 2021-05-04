import os, sys, time, pandas, psutil
import pprint #temp
from util import *
#pprint Docs: https://docs.python.org/3/library/pprint.html

###########################(Pandas Resources - Start)###########################
#Pandas Module Resources
#Cheatsheet: https://www.dataquest.io/blog/pandas-cheat-sheet/
#Quickstart Guide: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
#Formal Docs: https://pandas.pydata.org/docs/reference/io.html
############################(Pandas Resources - End)############################


###########################(Psutil Resources - Start)###########################
#General Docs: https://psutil.readthedocs.io/en/latest/#network
# # psutil.net_io_counters(pernic=False, nowrap=True)
# #     system-wide IO stats, allows per nic
# #     https://psutil.readthedocs.io/en/latest/#psutil.net_io_counters

# # psutil.net_connections(kind='inet')
# #     Return System-wide socket connections
# #     https://psutil.readthedocs.io/en/latest/#psutil.net_connections

# # psutil.net_if_addrs()
# #     Return the addresses associated to each NIC
# #     (address family, primary address, netmask, broadcast, point to point)
# #     https://psutil.readthedocs.io/en/latest/#psutil.net_if_addrs

# # psutil.net_if_stats()
# #     Return information about each NIC 
# #     (NIC up or down, duplex comm type, NIC speed, nic max transmission unit)
# #     https://psutil.readthedocs.io/en/latest/#psutil.net_if_stats
############################(Psutil Resources - End)############################

def main(): 
    pass

if __name__ == "__main__":
    os.system('cls')
    main()