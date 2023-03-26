import os

from selene.support.shared import browser
from selene import be, have, command

from .locators import Locators

class SimplifiedRegistrationPage():
    def register(self):
        browser.element('#userName').type("Anna")
        browser.element('#userEmail').type("Anna@yandex.ru")
        browser.element('#currentAddress').type("Невский 129")
        browser.element('#permanentAddress').type("Невский 12")
        browser.element('#submit').perform(command.js.click)

    def should_have_registered(self):
        browser.element('#name').should(have.text("Name:Anna"))
        browser.element('#email').should(have.text("Email:Anna@yandex.ru"))
        #browser.element('#currentAddress').should(have.text("Current Address:Невский 129"))
        #browser.element('#permanentAddress').should(have.text("Permananet Address:Невский 12"))

