from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_fill_input():
    with step('Type search query'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('Appium\n')
        result = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output'))
        result.should(have.exact_text('Appium'))


def test_dismiss_alert():
    with step('Type search query'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Alert')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'OK')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'This is a native alert')).should(be.not_.visible)
