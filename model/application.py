from selene.support.shared import browser

from model.simplified_registration_page import SimplifiedRegistrationPage


class Application:
    def __init__(self):
        self.simplifield_registration_page = SimplifiedRegistrationPage()

    def open(self):
        browser.open('/')
        return self


app = Application()