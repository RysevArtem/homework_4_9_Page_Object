
from model.registration_page import RegistrationPage
from model.user_data import User, Subjects


def test_authorization(browser_options):
    student = User(
        first_name="Света",
        last_name="Солонина",
        email="test@yandex.ru",
        gender="Female",
        phone_number=1234567890,
        birth_year="1986",
        birth_month="April",
        birth_day="20",
        subject=Subjects.maths.value,
        hobby="Music",
        upload_filename="child.jpg",
        current_address="Morskaya, 10",
        state='Haryana',
        city='Karnal'
    )

    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
