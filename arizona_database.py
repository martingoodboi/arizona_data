import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="arizona"
)

#show tables

"""mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for _ in mycursor:
  print(_)
"""
#select * from table
"""mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM arizona_roster")

myresult = mycursor.fetchall()

for _ in myresult:
  print(_)"""

#create table + add columns
"""mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE arizona_roster (id INT unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY, player_name VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL, pos VARCHAR(255) COLLATE utf8_unicode_ci DEFAULT NULL, age INT unsigned NOT NULL, ht DECIMAL(3,2) unsigned NOT NULL, wt INT unsigned NOT NULL, exp INT unsigned NOT NULL, college VARCHAR(255) COLLATE utf8_unicode_ci DEFAULT NULL)")
"""


"""#drop table
mycursor = mydb.cursor()

sql = "DROP TABLE arizona_roster"

mycursor.execute(sql)"""




"""mycursor = mydb.cursor()

sql = "INSERT INTO arizona_roster(id,player_name, pos, age, ht, wt, exp, college) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(player_name, pos, age, ht, wt, exp, college)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")"""
