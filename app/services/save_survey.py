"""
Saves survey to database
"""

from ..utils.Dbconnection import get_DBconnection
import mysql.connector

def add(survey):

	"""
	function to save user details to database

	Args:
		survey (tuple): a tuple containing survey information

	Returns:
		flag (bool): True if operation was successful, False otherwise
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "INSERT INTO Survey (`fullname`, `email`, `age`, `contact_number`, `pizza`, `pasta`, `pap_and_wors`, `other`, `movies`, `radio`, `eat_out`, `tv`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s)"


	try:

		response = cursor.execute(query, survey)

		conn.commit()
		if (cursor.rowcount > 0):
			return True
		return False
		
	except mysql.connector.Error as err:
		return f"Error {err}"