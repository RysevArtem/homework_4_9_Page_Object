from selene.support.shared import browser
from selene import be, have, command
import os


def test_authorization(browser_options):
    # Steps
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("footer").remove()')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.execute_script('document.querySelector("#RightSide_Advertisement").remove()')
    browser.element('#firstName').should(be.blank).type("Артем")
    browser.element('#lastName').should(be.blank).type("Рысев")
    browser.element('#userEmail').should(be.blank).type("test@yandex.ru")
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type("1234567890")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value = "1986"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value = "7"]').click()
    browser.element('[aria-label = "Choose Tuesday, August 5th, 1986"]').click()
    browser.element('#subjectsInput').should(be.blank).type("Maths").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').type(os.getcwd() + '/child.jpg')
    browser.element('#currentAddress').should(be.blank).type("Something2")
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').perform(command.js.click)
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    # Assertions
    browser.element('.table tr:nth-child(1) > th:nth-child(1)').should(have.exact_text('Label'))
    browser.element('.table tr:nth-child(1) > th:nth-child(2)').should(have.exact_text('Values'))
    browser.element('.table tr:nth-child(1)>td:nth-child(1)').should(have.exact_text('Student Name'))
    browser.element('.table tr:nth-child(1)>td:nth-child(2)').should(have.exact_text('Артем Рысев'))
    browser.element('.table tr:nth-child(2)>td:nth-child(1)').should(have.exact_text('Student Email'))
    browser.element('.table tr:nth-child(2)>td:nth-child(2)').should(have.exact_text('test@yandex.ru'))
    browser.element('.table tr:nth-child(3)>td:nth-child(1)').should(have.exact_text('Gender'))
    browser.element('.table tr:nth-child(3)>td:nth-child(2)').should(have.exact_text('Male'))
    browser.element('.table tr:nth-child(4)>td:nth-child(1)').should(have.exact_text('Mobile'))
    browser.element('.table tr:nth-child(4)>td:nth-child(2)').should(have.exact_text('1234567890'))
    browser.element('.table tr:nth-child(5)>td:nth-child(1)').should(have.exact_text('Date of Birth'))
    browser.element('.table tr:nth-child(5)>td:nth-child(2)').should(have.exact_text('05 August,1986'))
    browser.element('.table tr:nth-child(6)>td:nth-child(1)').should(have.exact_text('Subjects'))
    browser.element('.table tr:nth-child(6)>td:nth-child(2)').should(have.exact_text('Maths'))
    browser.element('.table tr:nth-child(7)>td:nth-child(1)').should(have.exact_text('Hobbies'))
    browser.element('.table tr:nth-child(7)>td:nth-child(2)').should(have.exact_text('Sports'))
    browser.element('.table tr:nth-child(8)>td:nth-child(1)').should(have.exact_text('Picture'))
    browser.element('.table tr:nth-child(8)>td:nth-child(2)').should(have.exact_text('child.jpg'))
    browser.element('.table tr:nth-child(9)>td:nth-child(1)').should(have.exact_text('Address'))
    browser.element('.table tr:nth-child(9)>td:nth-child(2)').should(have.exact_text('Something2'))
    browser.element('.table tr:nth-child(10)>td:nth-child(1)').should(have.exact_text('State and City'))
    browser.element('.table tr:nth-child(10)>td:nth-child(2)').should(have.exact_text('Uttar Pradesh Lucknow'))
    browser.element('#closeLargeModal').should((be.visible).and_(be.clickable))
