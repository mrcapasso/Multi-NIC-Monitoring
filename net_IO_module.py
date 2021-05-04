import psutil
import pandas as pd

def networkIOTable() -> pd.DataFrame:
    '''Returns Pandas dataframe with current NICs' I/O information'''
    netIOCounter = psutil.net_io_counters(pernic=True)
    netIOCounterDataFrame = pd.DataFrame.from_dict(netIOCounter, orient='Index')
    return netIOCounterDataFrame

if __name__ == '__main__':
    pass