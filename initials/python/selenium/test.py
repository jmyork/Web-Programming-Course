import os
import pathlib
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebPageTests(unittest.TestCase):
    def test_title(self):
        driver.get(file_uri("initials\python\selenium\counter.html")) 
        print(file_uri("counter.html"))
        self.assertIn("Counter", driver.title)

    def test_increase(self):
        driver.get(file_uri("initials\python\selenium\counter.html"))
        increase = driver.find_element(By.ID, "increase")
        increase.click()
        self.assertEqual(driver.find_element(By.ID, "h1").text, "1")


    def test_decrease(self):
        driver.get(file_uri("initials\python\selenium\counter.html"))
        decrease = driver.find_element(By.ID, "decrease")
        decrease.click()
        self.assertEqual(driver.find_element(By.ID, "h1").text, "0")

    def test_multiple_increase(self):
        driver.get(file_uri("initials\python\selenium\counter.html"))
        increase = driver.find_element(By.ID, "increase")
        for i in range(100):
            increase.click()
        self.assertEqual(driver.find_element(By.ID, "h1").text, "100")
    def test_multiple_decrease(self):
        driver.get(file_uri("initials\python\selenium\counter.html"))
        decrease = driver.find_element(By.ID, "decrease")
        for i in range(100):
            decrease.click()
        self.assertEqual(driver.find_element(By.ID, "h1").text, "0")
    
    def test_multiple_again(self):
        driver.get(file_uri("initials\python\selenium\counter.html"))
        increase = driver.find_element(By.ID, "increase")
        for i in range(100):
            increase.click()
        self.assertEqual(driver.find_element(By.ID, "h1").text, "100")
        
if __name__ == "__main__":
    unittest.main()