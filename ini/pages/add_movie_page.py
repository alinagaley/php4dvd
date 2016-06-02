from ini.pages.internal_page import InternalPage
from ini.pages.blocks.user_form import UserForm
from selenium.webdriver.support.select import Select
from ini.pages.blocks.add_movie_form import AddMovieForm

class AddMoviePage(InternalPage):

    def __init__(self, driver, base_url):
        super(AddMoviePage, self).__init__(driver, base_url)
        self.add_movie_form = AddMovieForm(self.driver, self.base_url)

