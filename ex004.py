import time

print("The present time is:",time.strftime('%H:%M:%S'))

# hour=int(time.strftime('%H'))
hour=19
match(hour):
    case _ if hour>=0 and hour<12:
        print('This is Morning')
    case _ if hour>=12 and hour<=17:
        print('This noon')
    case _:
        print('This is night')