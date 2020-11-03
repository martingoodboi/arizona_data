import requests
import MySQLdb
from bs4 import BeautifulSoup
import re

#SQL connection data to connect and save the data in
HOST = "localhost"
USERNAME = "root"
PASSWORD = "--------"
DATABASE = "arizona"

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

			
			#print()
			#print(names,pos,age,ht,wt,exp,college)



			#Save event data to database
			# Open database connection
			db = MySQLdb.connect("localhost", "root", "Lisna699", "arizona")
			# prepare a cursor object using cursor() method
			cursor = db.cursor()
			# Prepare SQL query to INSERT a record into the database.
			sql = "INSERT INTO arizona_roster ( player_name, pos, age, ht, wt, exp, college) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(player_name, pos, age, ht, wt, exp, college, 'NOW()')
			try:
				# Execute the SQL comman
				cursor.execute(sql)
				# Commit your changes in the database
				db.commit()
			except:
				# Rollback in case there is any error
				db.rollback()
			# disconnect from server
			db.close()
			

