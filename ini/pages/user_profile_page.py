from ini.pages.internal_page import InternalPage
from ini.pages.blocks.add_movie_form import AddMovieForm
from selenium.webdriver.support.select import Select


class UserProfilePage(InternalPage):

    def __init__(self, driver, base_url):
        super(UserProfilePage, self).__init__(driver, base_url)
        self.user_form = AddMovieForm(self.driver, self.base_url)

