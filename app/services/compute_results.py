"""
Survey results
"""
from ..utils.DBconnection import get_DBconnection
import mysql.connector

def total_surveys():

	"""
	returns number of surveys.

	Args:
		None

	Returns:
		total (int): integer representing number of rows
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT COUNT(*) FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchall()

		total = data[0]

		return total[0]

	except mysql.connector.Error as err:
		cursor.close()
		conn.close()
		return f"Error: {err}"


def average_age():

	"""
	Returns the average of participants

	Args:
		None

	Returns:
		average_age (int): Integer representing an averange of age
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT AVG(age) AS Average_age FROM Survey"

	try:

		cursor.execute(query)

		data = cursor.fetchone()

		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False

	except mysql.connector.Error as err:
		return f"Error: {err}"

def oldest():

	"""
	Returns the oldest person
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT fullname, age FROM Survey WHERE age = (SELECT MAX(age) FROM Survey)"

	try:
		cursor.execute(query)

		data = cursor.fetchall()
		if (cursor.rowcount > 0):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def youngest():

	"""
	Returns youngest person
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT fullname, age FROM Survey WHERE age = (SELECT 	MIN(age) FROM Survey)"

	try:
		cursor.execute(query)

		data = cursor.fetchall()
		if (cursor.rowcount > 0):
			return data[0]
		return False
	except mysql.connector.Error as err:
		return f"Error: {err}"
	

def pizza():

	"""
	Returns percentage of people who like pizza 
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT (SUM(pizza = 1) / COUNT(*)) * 100 FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def pasta():
	"""
	Returns percentage of people who like pasta 
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT (SUM(pasta = 1) / COUNT(*)) * 100 FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def pap_wors():
	"""
	Returns percentage of people who like Pap and  Wors
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT (SUM(pap_and_wors = 1) / COUNT(*)) * 100 FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
	
def movie():
	"""
	Returns the average rating for people who like movies
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT AVG(6 - movies) FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def radio():
	"""
	Returns the average rating for people who like radio
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT AVG(6 - radio) FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def eating_out():
	"""
	Returns the average rating for people who like eating out
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT AVG(6 - eat_out) FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def tv():
	"""
	Returns the average rating for people who like tv
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT AVG(6 - tv) FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0) and data[0] is not None:
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"