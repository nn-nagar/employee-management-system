from django.test import TestCase

# Create your tests here.

from emp_app.models import Department, Employee


class EmployeeTestCase(TestCase):
    def testEmployee(self):
        dept= Department.objects.get(name='AWS Cloud')
        employee = Employee(first_name="Diego", last_name="Blurb", dept=dept)
        self.assertEqual(employee.first_name, "Diego")
        self.assertEqual(employee.last_name, "Blurb")
        self.assertEqual(employee.dept, dept)
