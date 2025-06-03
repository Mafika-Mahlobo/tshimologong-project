"""
Survey results
"""
from ..utils.DBconnection import get_DBconnection
import psycopg2
from psycopg2 import Error

def total_surveys():
    conn = get_DBconnection()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM Survey"
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        return data[0][0]
    except Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

def average_age():
    conn = get_DBconnection()
    cursor = conn.cursor()
    query = "SELECT AVG(age) FROM Survey"
    try:
        cursor.execute(query)
        data = cursor.fetchone()
        return data[0] if data[0] is not None else False
    except Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

def oldest():
    conn = get_DBconnection()
    cursor = conn.cursor()
    query = "SELECT fullname, age FROM Survey WHERE age = (SELECT MAX(age) FROM Survey)"
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        return data[0] if cursor.rowcount > 0 else False
    except Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

def youngest():
    conn = get_DBconnection()
    cursor = conn.cursor()
    query = "SELECT fullname, age FROM Survey WHERE age = (SELECT MIN(age) FROM Survey)"
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        return data[0] if cursor.rowcount > 0 else False
    except Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

def pizza():
    conn = get_DBconnection()
    cursor = conn.cursor()
    query = "SELECT (SUM(CASE WHEN pizza = 1 THEN 1 ELSE 0 END)::float / COUNT(*)) * 100 FROM Survey"
    try:
        cursor.execute(query)
        data = cursor.fetchone()
        return data[0] if data[0] is not None else False
    except Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

def pasta():
    conn = get_DBconnection()
    cursor = conn.cursor()
    query = "SELECT (SUM(CASE WHEN pasta = 1 THEN 1 ELSE 0 END)::float / COUNT(*)) * 100 FROM Survey"
    try:
        cursor.execute(query)
        data = cursor.fetchone()
        return data[0] if data[0] is not None else False
    except Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

def pap_wors():
    conn = get_DBconnection()
    cursor = conn.cursor()
    query = "SELECT (SUM(CASE WHEN pap_and_wors = 1 THEN 1 ELSE 0 END)::float / COUNT(*)) * 100 FROM Survey"
    try:
        cursor.execute(query)
        data = cursor.fetchone()
        return data[0] if data[0] is not None else False
    except Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

def movie():
    conn = get_DBconnection()
    cursor = conn.cursor()
    query = "SELECT AVG(6 - movies) FROM Survey"
    try:
        cursor.execute(query)
        data = cursor.fetchone()
        return data[0] if data[0] is not None else False
    except Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

def radio():
    conn = get_DBconnection()
    cursor = conn.cursor()
    query = "SELECT AVG(6 - radio) FROM Survey"
    try:
        cursor.execute(query)
        data = cursor.fetchone()
        return data[0] if data[0] is not None else False
    except Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

def eating_out():
    conn = get_DBconnection()
    cursor = conn.cursor()
    query = "SELECT AVG(6 - eat_out) FROM Survey"
    try:
        cursor.execute(query)
        data = cursor.fetchone()
        return data[0] if data[0] is not None else False
    except Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()

def tv():
    conn = get_DBconnection()
    cursor = conn.cursor()
    query = "SELECT AVG(6 - tv) FROM Survey"
    try:
        cursor.execute(query)
        data = cursor.fetchone()
        return data[0] if data[0] is not None else False
    except Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        conn.close()
