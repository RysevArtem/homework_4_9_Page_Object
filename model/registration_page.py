import os

from selene.support.shared import browser
from selene import be, have, command

import model
from .locators import Locators
from pathlib import Path

import tests

class RegistrationPage():
    def page_open(self):
        browser.open('/automation-practice-form')
    def page_set_up(self):
        browser.execute_script(f'document.querySelector("{Locators.page_set_up_footer}").remove()')
        browser.execute_script(f'document.querySelector("{Locators.page_set_up_fixedban}").remove()')
        browser.execute_script(f'document.querySelector("{Locators.page_set_up_right_side_advertisment}").remove()')

    def type_first_name(self, first_name):
        browser.element(Locators.first_name).should(be.blank).type(first_name)

    def type_last_name(self, last_name):
        browser.element(Locators.last_name).should(be.blank).type(last_name)

    def type_email(self, email):
        browser.element(Locators.user_email).should(be.blank).type(email)

    def choose_gender(self, gender):
        browser.all(Locators.gender).element_by(have.value(gender)).element('..').click()

    def type_phone_number(self, phone_number):
        browser.element(Locators.phone_number).should(be.blank).type(phone_number)

    def input_date_of_birth(self, birth_day, birth_month, birth_year):
        browser.element(Locators.date_of_birth_input).click()
        browser.element(Locators.date_of_birth_month).type(birth_month)
        browser.element(Locators.date_of_birth_year).type(birth_year)
        browser.element(
            f'.react-datepicker__day--0{birth_day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def type_subjects(self, subject):
        browser.element(Locators.subjects_input).should(be.blank).type(subject).press_enter()

    def choose_hobbies(self, hobby):
        browser.all(Locators.hobbies).element_by(have.text(hobby)).click()

    def upload_pictire(self, upload_filename):
        browser.element(Locators.upload_pictire).type(os.getcwd() + f'/tests/resourses/{upload_filename}')

    def type_address(self, address):
        browser.element(Locators.current_address).should(be.blank).type(address)

    def choose_state(self, state):
        browser.element(Locators.choose_state).click()
        browser.all(Locators.choose_state_option).element_by(
            have.exact_text(state)
        ).click()

    def choose_city(self, city):
        browser.element(Locators.choose_city).click()
        browser.all(Locators.choose_city_options).element_by(
            have.exact_text(city)
        ).click()

    def click_submit_button(self):
        browser.element(Locators.submit_button).perform(command.js.click)

    def should_registered_user_with(self, first_name, last_name, email, gender, phone_number, birth_day,
                                    birth_month, birth_year,
                                    subject, hobby, upload_filename,
                                    current_address, state, city):
        full_name = first_name + " " + last_name
        full_birthday = birth_day + " " + birth_month + "," + birth_year
        state_and_city = state + " " + city
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                f'{phone_number}',
                full_birthday,
                subject,
                hobby,
                upload_filename,
                current_address,
                state_and_city
            )
        )
        browser.element(Locators.completed_form_close_button).should((be.visible).and_(be.clickable))
