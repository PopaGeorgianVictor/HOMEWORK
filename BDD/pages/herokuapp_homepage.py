from BDD.pages.base_page import Base_page


class Home_page(Base_page):

    def navigate_to_homepage(self):
        self.driver.get()