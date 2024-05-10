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

	quesry = "SELECT COUNT(*) FORM Survey"

	try:
		cursor.execute(quesry)

		data = cursor.fetchall()

		if(cursor.rowcount > 0):
			return data
		return False

	except mysql.connector.Error as err:
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

		cursor.execute(quesry)

		data = cursor.fetchall()

		if (cursor.rowcount > 0):
			return data
		return False

	except mysql.connector.Error as err:
		return f"Error: {err}"
