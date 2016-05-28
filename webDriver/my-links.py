# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class ALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_a_links(self):
        link_title = {
            "Library West Computer Lab":"De Anza College :: Library :: Library West Computer Lab", 
            "Orientation":"De Anza College :: Counseling and Advising Center :: Orientation",
            "Outreach & Relations with Schools": "De Anza College :: Office of Outreach & Relations with Schools :: Welcome Future Students and Parents",
            "PIN-Personal Identification Number":"De Anza College :: Registration :: Personal Identification Number (PIN)",
            "Paralegal Studies":"De Anza College :: Paralegal Studies :: Home",
            "Parents":"De Anza College :: Office of Outreach & Relations with Schools :: Welcome Future Students and Parents",
            "Parking":"De Anza College :: Parking and Transportation :: Home",
            "Partners in Learning":"De Anza College :: Partners in Learning Conference :: Partners in Learning Conference",
            }
        
        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try: self.assertEqual(title, driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

