from datetime import datetime
def salary(month,year):
    s=datetime(year,month=month,day=10)
    n=datetime.now()
    return (s-n).days

print(salary(11,2023))


print(datetime(2023,11,1))



