"""
Saves survey to database
"""

from ..utils.DBconnection import get_DBconnection
import psycopg2


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

	query = """
	INSERT INTO Survey (
		fullname, email, age, contact_number,
		pizza, pasta, pap_and_wors, other,
		movies, radio, eat_out, tv
	) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
	"""

	try:
		cursor.execute(query, survey)
		conn.commit()
		if cursor.rowcount > 0:
			return True
		return False

	except psycopg2.Error as err:
		return f"Error {err}"

	finally:
		cursor.close()
		conn.close()
