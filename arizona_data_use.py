import requests
import MySQLdb
from bs4 import BeautifulSoup
import re
import mysql.connector

"""#SQL connection data to connect and save the data in
HOST = "localhost"
USERNAME = "root"
PASSWORD = ""
DATABASE = "arizona"""

source = requests.get('https://www.espn.com/nfl/team/roster/_/name/ari').text
 
soup = BeautifulSoup(source, 'html.parser')
"""
#get the name of table
site_name = soup.find('h1', class_ = 'headline headline__h1 dib').text
table_name = soup.find('div',class_ = 'Table__Title').text
print(site_name)
print()
print(table_name)
print()
"""
#####################################################################

#td table 
"""#Get all data associated with this class
basic_data_table = soup.find("table");
#Get all cells in the base data table
basic_data_cells = basic_data_table.findAll('td')"""

######################################################################

#tr table

#Get the tables where the dates are written.
data_tables = soup.find_all("table")


#Iterate through the tables
for table in data_tables:
	#Iterate through the rows inside the table
	for row in table.select("tr"):
		#Get all cells inside the row
		cells = row.find_all("td")
		#check if there is at least one td cell inside this row
		if(len(cells) > 0):
		#get all the different data from the table's tds
		#Split this cell into two different parts seperated by 'to' in order to have a start_date and an end_date.
			player_name = cells[1].text.split()
			pos = cells[2].text.split()
			age = cells[3].text.split()
			ht = cells[4].text.split()
			wt = cells[5].text.split()
			exp = cells[6].text.split()
			college = cells[7].text.split()

			#print(player_name,pos,age,ht,wt,exp,college)
			#print()
			

			#remove nonnumeric char
			player_name = ''.join(filter(str.isalnum, player_name))
			pos = ''.join(filter(str.isalnum, pos))
			age = ''.join(filter(str.isalnum, age))
			wt = ''.join(filter(str.isalnum, wt))
			exp = ''.join(filter(str.isalnum, exp))
			college = ''.join(filter(str.isalnum, college))
			#print(player_name,pos,age,ht,wt,exp,college)


			# Function to  convert   
			def __str__(ht):  
				    
				# initialize an empty string 
				str1 = ""  
				    
				# traverse in the string   
				for ele in ht:  
				    str1 += ele   
				    
				# return string   
				return str(str1)  
			        
			        
			# Driver code     
			#print(__str__(ht))
			str_ht = __str__(ht)
			x = (str_ht.replace('"',''))
			ht_str = (x.replace("'",'.'))
			#print(ht_str)

			wt_int = (wt.replace("lbs", ""))
			#print(wt_int)
			exp_int = exp.replace("R","0")
			#print(exp_int)

			mydb = mysql.connector.connect(
  			host="localhost",
  			user="root",
  			password="",
  			database="arizona"
			)			



			mycursor = mydb.cursor()

			sql = "INSERT INTO arizona_roster(player_name, pos, age, ht, wt, exp, college) VALUES (%s, %s, %s,%s,%s,%s,%s)"
			val = (player_name,pos,age,ht_str,wt_int,exp_int,college)
			mycursor.execute(sql, val)

			mydb.commit()

			mycursor.close()
			mydb.close()
			

