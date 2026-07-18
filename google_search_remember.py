from selene import browser, be, have


def test_google_search():
    browser.open("https://www.google.com")
    browser.element('[name="q"]').should(be.blank).double_click()
