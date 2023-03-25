import os

from selene.support.shared import browser
from selene import be, have, command

from .locators import Locators


class RegistrationPage():
    def open(self):
        browser.open('/automation-practice-form')

    def register(self, student):
        browser.execute_script(f'document.querySelector("{Locators.page_set_up_footer}").remove()')
        browser.execute_script(f'document.querySelector("{Locators.page_set_up_fixedban}").remove()')
        browser.execute_script(f'document.querySelector("{Locators.page_set_up_right_side_advertisment}").remove()')

        browser.element(Locators.first_name).should(be.blank).type(student.first_name)

        browser.element(Locators.last_name).should(be.blank).type(student.last_name)

        browser.element(Locators.user_email).should(be.blank).type(student.email)

        browser.all(Locators.gender).element_by(have.value(student.gender)).element('..').click()

        browser.element(Locators.phone_number).should(be.blank).type(student.phone_number)

        browser.element(Locators.date_of_birth_input).click()
        browser.element(Locators.date_of_birth_month).type(student.birth_month)
        browser.element(Locators.date_of_birth_year).type(student.birth_year)
        browser.element(
            f'.react-datepicker__day--0{student.birth_day}:not(.react-datepicker__day--outside-month)'
        ).click()

        browser.element(Locators.subjects_input).should(be.blank).type(student.subject).press_enter()

        browser.all(Locators.hobbies).element_by(have.text(student.hobby)).click()

        browser.element(Locators.upload_pictire).type(os.getcwd() + f'/tests/resourses/{student.upload_filename}')

        browser.element(Locators.current_address).should(be.blank).type(student.current_address)

        browser.element(Locators.choose_state).click()
        browser.all(Locators.choose_state_option).element_by(
            have.exact_text(student.state)
        ).click()

        browser.element(Locators.choose_city).click()
        browser.all(Locators.choose_city_options).element_by(
            have.exact_text(student.city)
        ).click()

        browser.element(Locators.submit_button).perform(command.js.click)

    def should_have_registered(self, student):
        full_name = student.first_name + " " + student.last_name
        full_birthday = student.birth_day + " " + student.birth_month + "," + student.birth_year
        state_and_city = student.state + " " + student.city
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                student.email,
                student.gender,
                f'{student.phone_number}',
                full_birthday,
                student.subject,
                student.hobby,
                student.upload_filename,
                student.current_address,
                state_and_city
            )
        )
        browser.element(Locators.completed_form_close_button).should((be.visible).and_(be.clickable))
