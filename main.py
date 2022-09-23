import application.salary
from application.db.people import get_employees
import datetime

if __name__ == '__main__':
    print (f' время: {datetime.datetime.today()}, salary:  {application.salary.calculate_salary()}')
    print(f' время: {datetime.datetime.today()}, employees: {get_employees()}')
