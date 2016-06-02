from ini.pages.page import Page
from selenium.webdriver.support.select import Select


class AddMovieForm(Page):

    @property
    def movie_title_field(self):
        return self.driver.find_element_by_name("name")

    @property
    def movie_year_field(self):
        return self.driver.find_element_by_name("year")

    @property
    def submit_button(self):
        return self.driver.find_element_by_name("submit")
