from datetime import datetime
from datetime import timedelta
#from datetime import datetiöe /date/time
simdi =datetime.today()
resuly= datetime.now().year
resuly= datetime.now().month
resuly= datetime.now().minute
resuly=datetime.ctime(simdi)
resuly=datetime.strftime(simdi,"%Y")
resuly=datetime.strftime(simdi,"%Y %B")

print(resuly)

birtday =datetime(1983,5,9,12,30,10)

resuly =datetime.timestamp(birtday)
resuly=datetime.fromtimestamp(resuly)
resuly=simdi+timedelta(days=410)
print(resuly)