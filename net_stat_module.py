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

# # psutil.net_if_stats()
# #     Return information about each NIC 
# #     (NIC up or down, duplex comm type, NIC speed, nic max transmission unit)
# #     https://psutil.readthedocs.io/en/latest/#psutil.net_if_stats

def activeNICDict() -> dict: 
    '''psutil.net_if_stats(), but for active NICs'''
    dictOfNICs = psutil.net_if_stats()
    dictOfActiveNICs = {}
    for i in dictOfNICs:
        individualNic = dictOfNICs.get(i)
        isUpStatus = individualNic[0]
        if isUpStatus == True:
            ithKeyValue = dictOfNICs.get(i)
            dictOfActiveNICs.update({i:ithKeyValue})
    return dictOfActiveNICs


if __name__ == '__main__':
    pprint.pprint(activeNICDict())