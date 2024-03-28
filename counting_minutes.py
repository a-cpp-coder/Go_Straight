# separate the input into small pieces for much easier processing

def convert_time(time):
    if "pm" in time:
        # time.replace("pm", "")
        time = time.replace("pm", "")
        hours, minutes = time.split(":")
        print(hours, minutes)
        return int(hours)*60 + int(minutes) + 12 * 60
    else:
        time = time.replace("am", "")
        hours, minutes = time.split(":")
        return int(hours)*60 + int(minutes)
    
def counting_minutes(time_string):
    begin, end = time_string.split("-")
    print(begin, end)
    begin = convert_time(begin)
    end = convert_time(end)

    return end - begin if begin < end else 24 * 60 - (begin - end)

print(counting_minutes("12:30pm-12:00am"))