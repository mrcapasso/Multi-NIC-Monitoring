import os, sys, pprint, csv
import psutil
import pandas as pd
import net_address_module as netAdd
import net_IO_module as netIO
import net_stat_module as netStat

###ToDo
#Time series of netStatNIC(dict) for each NIC
#Time series of netIOCounter(dict) for each NIC
#Time series of netAddressNIC(dict) for each NIC

def main(): 
    #Configurations
    DATA_FOLDER = r'Data'
    CONSOLE_TEXT_OUTPUT = True

if __name__ == "__main__":
    os.system('cls')
    main()