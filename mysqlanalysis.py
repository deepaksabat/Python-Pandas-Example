import pandas as pd
import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",db="lcrm")##Connection to MYSQL DB
c=conn.cursor()
c.execute("SELECT id,meeting_subject,starting_date,ending_date,longitude,latitude from meetings")
data=c.fetchall()
return [val for sublist in data for val in sublist]
idd = column_to_list("id")
meet = column_to_list("meeting_subject")
strtdt = column_to_list("starting_date")
longitude = column_to_list("longitude")
latitude = column_to_list("latitude")
df = pd.DataFrame({'idd': idd,'meet': meet,'strtdt': strtdt,'longitude': longitude,'latitude': latitude})
print (df[["idd","strtdt","latitude",]].describe(percentiles=(.75,.90,.99)))

conn.close();

   