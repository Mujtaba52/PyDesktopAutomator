import unittest
import time
import pyautogui
import pywinauto
import os
class TestCalculatorAutomation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Launch Calculator once before the tests
        cls.app = pywinauto.Application(backend="uia").start("calc.exe").connect(title='Calculator', timeout=100)
        # Wait for Calculator to start (adjust the sleep duration as needed)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # Close Calculator after all tests are done
        cls.app.Calculator.close()

    def test_addition(self):
        # Perform addition: 5 + 3
        time.sleep(2)
        pyautogui.click(839, 1199)

        time.sleep(1)
        pyautogui.click(1951, 1193)

        time.sleep(1)
        pyautogui.click(1407, 1192)
        # app.Calculator.child_window(title="Five", control_type="Button").click()

        time.sleep(2)
        pyautogui.click(1957, 1340)

        time.sleep(2)
        result = self.app.Calculator.child_window(auto_id="CalculatorResults", control_type="Text").texts()
        print(result)
        self.assertEqual(result[0], "Display is 5")
        time.sleep(2)

    def test_subtraction(self):
        # Perform subtraction: 2 - 3
        pyautogui.click(839, 1199)

        time.sleep(2)
        pyautogui.click(1957, 1043)

        time.sleep(1)
        pyautogui.click(1407, 1192)
        # app.Calculator.child_window(title="Five", control_type="Button").click()

        time.sleep(1)
        pyautogui.click(1957, 1340)
        result = self.app.Calculator.child_window(auto_id="CalculatorResults", control_type="Text").texts()
        print(result)
        self.assertEqual(result[0], "Display is -1")
        time.sleep(2)

    def test_multiplication(self):
        # x, y = pyautogui.position()
        # print(f"Mouse coordinates: x={x}, y={y}")
        pyautogui.click(839, 1199)

        time.sleep(2)
        pyautogui.click(1957, 897)

        time.sleep(1)
        pyautogui.click(1407, 1192)
        # app.Calculator.child_window(title="Five", control_type="Button").click()

        time.sleep(1)
        pyautogui.click(1957, 1340)
        result = self.app.Calculator.child_window(auto_id="CalculatorResults", control_type="Text").texts()
        print(result)
        self.assertEqual(result[0], "Display is 6")
        time.sleep(2)

    # Add more test methods for other calculator operations here


if __name__ == "__main__":
    unittest.main()
