def format_duration(seconds):
    divi = [60, 60, 24, 365]
    format = ["second","minute","hour","day","year"]
    time = []
    if seconds <= 0:
        return "now"
    else:
        for x in divi:
            if seconds == 0:
                time.append(seconds)
            else:
                time.append(seconds%x)
                seconds //= x
                if x == 365:
                    time.append(seconds%x)
        time = [f" {x} "+format[y] if x<2 else f" {x} "+format[y]+"s" for y, x in enumerate(time)]
        time = [x[1:] for x in time if " 0" not in x]
        time.reverse()
        if len(time) == 1:
            return time[0]
        elif len(time) == 2:
            return time[0]+" and "+time[1]
        elif len(time) == 3:
            return time[0]+", "+time[1]+" and "+time[2]
        elif len(time) == 4:
            return time[0]+", "+time[1]+", "+time[2]+" and "+time[3]
        elif len(time) == 5:
            return time[0]+", "+time[1]+", "+time[2]+", "+time[3]+" and "+time[4]
