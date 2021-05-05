import os, sys, pprint, csv
import psutil
import pandas as pd
import net_address_module as netAdd
import net_IO_module as netIO
import net_stat_module as netStat

###########################(Pandas Resources - Start)###########################
#Pandas Module Resources
#Cheatsheet: https://www.dataquest.io/blog/pandas-cheat-sheet/
#Quickstart Guide: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
#Formal Docs: https://pandas.pydata.org/docs/reference/io.html
############################(Pandas Resources - End)############################


#General Docs: https://psutil.readthedocs.io/en/latest/#network
# # psutil.net_io_counters(pernic=False, nowrap=True)
# #     system-wide IO stats, allows per nic
# #     https://psutil.readthedocs.io/en/latest/#psutil.net_io_counters

def networkIOTable() -> pd.DataFrame:
    '''Returns Pandas dataframe with current NICs' I/O information'''
    netIOCounter = psutil.net_io_counters(pernic=True)
    netIOCounterDataFrame = pd.DataFrame.from_dict(netIOCounter, orient='Index')
    return netIOCounterDataFrame
    

#Time series of netIOCounter(dict) for each NIC


if __name__ == '__main__':
    print(networkIOTable())

