import time 

a=time.ctime()

print(a)


from datetime import datetime

# Get current date and time
now = datetime.now()
print("Current time:", now)

# Format the datetime
print("Formatted:", now.strftime("%d/%m/%Y %H:%M:%S"))
