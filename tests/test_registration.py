from model.registration_page import RegistrationPage
from model.user_data import User, Subjects


def test_authorization(browser_options):
    student = User(
        first_name="Артем",
        last_name="Рысев",
        email="test@yandex.ru",
        gender="Male",
        phone_number=1234567890,
        birth_year="2005",
        birth_month="June",
        birth_day="05",
        subject=Subjects.biology.value,
        hobby="Sports",
        upload_filename="child.jpg",
        current_address="Morskaya, 5",
        state='NCR',
        city='Delhi'
    )

    registration_page = RegistrationPage()
    registration_page.page_open()
    registration_page.page_set_up()
    registration_page.type_first_name(student.first_name)
    registration_page.type_last_name(student.last_name)
    registration_page.choose_gender(student.gender)
    registration_page.type_email(student.email)
    registration_page.type_phone_number(student.phone_number)
    registration_page.input_date_of_birth(student.birth_day, student.birth_month, student.birth_year)
    registration_page.type_subjects(student.subject)
    registration_page.choose_hobbies(student.hobby)
    registration_page.upload_pictire(student.upload_filename)
    registration_page.type_address(student.current_address)
    registration_page.choose_state(student.state)
    registration_page.choose_city(student.city)
    registration_page.click_submit_button()
    registration_page.should_registered_user_with(student.first_name, student.last_name, student.email, student.gender,
                                                  student.phone_number,
                                                  student.birth_day, student.birth_month, student.birth_year,
                                                  student.subject, student.hobby,
                                                  student.upload_filename,
                                                  student.current_address, student.state, student.city)
