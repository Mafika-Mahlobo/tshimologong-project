"""
Validate user input from form
"""

import psycopg2
from ..utils.DBconnection import get_DBconnection

def check_email(email):
	""" 
	Checks if email exists in the database.

	Args:
		email (str): String representing email address to be checked.

	Returns:
		(bool): True if email exists, false if it does not.
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT * FROM Survey WHERE email = %s"

	try:
		cursor.execute(query, (email,))
		response = cursor.fetchall()

		if len(response) > 0:
			return True
		return False

	except psycopg2.Error as err:
		return f"Error {err}"

	finally:
		cursor.close()
		conn.close()


# def check_age(date_str):
# 	"""
# 	Checks personal details.

# 	Args:
# 		date_str (str): a string representing a date of birth

# 	Returns:
# 		 age(int): an integer representing age 
# 	"""

# 	birth_date = datetime.strptime(date_str, "%Y-%m-%d")
# 	current = datetime.now()
# 	date_difference = current - birth_date
# 	age = date_difference.days // 365

# 	return age