from selene.support.shared import browser

from model.application import app


def test_reg(browser_options):
    browser.open('/text-box')
    app.simplifield_registration_page.register()
    app.simplifield_registration_page.should_have_registered()
