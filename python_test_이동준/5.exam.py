from datetime import date, datetime

cur_dt = datetime.now()

print(cur_dt.strftime('%Y\%m-%d %H*%M'+'%'+'%S')) # date.today() 와 동일하지만 String 타입임
