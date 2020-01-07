import re
from datetime import datetime as dtti
from datetime import timedelta as td

today = dtti.today()
price = {
        "new":100,
        "old":75
        }


f = open("emails/jonas.email")
data = f.read()
date = re.findall("\d{1,4}[-./]\d{1,2}[-./]\d{2,4}",data)[0]
name = re.findall("[A-Z][a-z]+ [A-Z][a-z]+",data)[0]

delimiter = re.findall("[-./]",date)
if re.search("^\d{4}",date) is not None:
    fmt = "%Y{d[0]}%m{d[1]}%d".format(d=delimiter)
else:
    fmt = "%d{d[0]}%m{d[1]}%Y".format(d=delimiter)

fmtdate = dtti.strptime(date,fmt)
payback_time = today-fmtdate

print(payback_time.days)
years = round(payback_time.days/365)
days = payback_time.days - (years*365)

print(years,days)

price_year =(price["new"]-price["old"])*12

customer_pays=years*price_year
customer_pays+=((price_year/12)/30)*days
we_pay=abs(customer_pays)

text="{} is owed {} and {} recives bill with -{}".format(name,we_pay,name,customer_pays)

email = """
Hi {}!
{}
mvh
Our Name
""".format(name,text)

f2 = open("emails/jonas.response.email","w")
f2.write(email)



