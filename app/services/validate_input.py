"""
Validate user input from form
"""

from datetime import datetime
import re


def check_phone(phone):
	"""
	Check phone number

	Args:
		phone (str): a string representing a phone number

	Returns:
		is_valid (bool): true if number is valid. false otherwise
	"""

	is_valid = False
	pattren = "^0\d{9}$"

	match = re.pattren(pattren, phone)

	if (match):
		is_valid = True

	return is_valid




def check_age(date_str):
	"""
	Checks personal details.

	Args:
		date_str (str): a string representing a date of birth

	Returns:

		 age(int): an integer representing age 
	"""

	birth_date = datetime.strptime(date_str, "%Y-%m-%d")
	current = datetime.now()
	date_difference = current - birth_date
	age = date_difference.days // 365

	return age

	
