# file for queryzzzzz.......
from datetime import date, datetime, timedelta
import random


TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

TABLES['departments'] = (
    "CREATE TABLE `departments` ("
    "  `dept_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `dept_name` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`dept_no`)"
    ") ENGINE=InnoDB")

TABLES['salaries'] = (
    "CREATE TABLE `salaries` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `salary` int(11) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")


def genQueryValue(tabName, tmrw, index):
    if tabName == 'salaries':
        return {
            'salary': 50+index,
            'from_date': tmrw,
            'to_date': date(random.randint(1900, 2000), 1, 1),
        }
    elif (tabName == 'employees'):
        return {
            'birth_date': date(random.randint(1900, 2000), 1, 1),
            'first_name': 'bhaskar',
            'last_name': 'HC',
            'gender': 'M',
            'hire_date': date(random.randint(1900, 2000), 1, 1),
        }
    elif (tabName == 'departments'):
        return {
            'dept_name': 'NoWords...'
        }


def genInsertQuery(tabName):
    if tabName == 'salaries':
        query = ("INSERT INTO salaries "
                 "(salary, from_date, to_date) "
                 "VALUES ( %(salary)s, %(from_date)s, %(to_date)s)")
        return query
    elif tabName == 'employees':
        query = ("INSERT INTO employees "
                 "(birth_date, first_name, last_name, gender, hire_date) "
                 "VALUES (%(birth_date)s,%(first_name)s,%(last_name)s,%(gender)s,%(hire_date)s)")
        return query
    elif tabName == 'deplartment':
        query = ("INSERT INTO department (dept_name) "
                 "VALUES ( %(dept_name)s )")
        return query


# def getSizeOfDB(cursor):
#     query = "SELECT table_schema AS 'Database',  ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Size (MB)'  FROM information_schema.TABLES  GROUP BY table_schema"
#     execQuery = cursor.execute(query)
#     print("Sized {}".format(execQuery));