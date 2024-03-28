def time_convert(num: int) -> str:
    hours = num // 60
    minutes = num % 60

    return str(hours) + ":" + str(minutes)

print(time_convert(63))