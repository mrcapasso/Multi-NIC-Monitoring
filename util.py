def elapsedTimeCalculator(startTime:float, endTime:float, decRound:int=2) -> str:
    elapsedTimeSecs = endTime - startTime
    elapsedTimeMins = elapsedTimeSecs/60
    elapsedTimeHours = elapsedTimeMins/60
    elapsedTimeDays = elapsedTimeHours/24
    if elapsedTimeDays >= 1: #Time as unit of days. 
        return str(round(elapsedTimeDays, decRound)) + ' days'
    elif elapsedTimeHours >= 1: #Time as unit of hours.
        return str(round(elapsedTimeHours, decRound)) + ' hours'
    elif elapsedTimeMins >= 1: #Time as unit of minutes.
        return str(round(elapsedTimeMins,decRound)) + ' minutes'
    else: #Time as unit of seconds.
        return str(round(elapsedTimeSecs,decRound)) + ' seconds'

if __name__ == '__main__':
    raise AssertionError('Not start file.')