
'''
1. Make a suite that contains your tests from theme 9 + the tests from
meeting 10 (who have the class). Generate the report
2. Think of a test class from the pages suggested in theme 8
- Write at least 3 test functions in a class (as we did in class)
Use driver instead of driver (what do you want, how many test functions do you want,
freestyle to start thinking of some test scenarios yourself).

'''

import unittest
import HtmlTestRunner


from HOMEWORK.SE_Verifiers import Login
from SE_Alerts import Alerts
from SE_Context_Menu import ContextMenu
from SE_Authentication import Authentication
from SE_Keys import Keyboard


class TestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test Execution Report',
            report_name='Test Results'
        )

        runner.run(smoke_test)

