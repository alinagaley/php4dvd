# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from ini.model.movie import Movie
from ini.model.user import User



def test_add_movie(app):
    new_movie = Movie.random()
    app.ensure_login_as(User.Admin())
    app.add_movie(new_movie)

        #driver.find_element_by_link_text("Add movie").click()
        #driver.find_element_by_name("name").clear()
        #driver.find_element_by_name("name").send_keys("New movie")
        #driver.find_element_by_id("submit").click()
        #driver.find_element_by_name("year").clear()
        #driver.find_element_by_name("year").send_keys("2016")
        #driver.find_element_by_id("submit").click()
        #driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        #self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")


