from datetime import datetime

import allure
import allure_commons
import pytest
import selene
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selene import browser

import config
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    common_options = {
        'platformName': 'ios',
        # Set URL of the application under test
        'app': config.BSTACK_APP_NAME,
        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': 'Automation project',
            'buildName': f'browserstack-build-{datetime.now()}',
            'sessionName': request.node.name,

            # Set your access credentials
            'userName': config.BSTACK_USER_NAME,
            'accessKey': config.BSTACK_ACCESS_KEY
        }
    }

    options = XCUITestOptions().load_capabilities(common_options)
    options.set_capability(name='platformVersion', value=config.IOS_PLATFORM_VERSION)
    options.set_capability(name='deviceName', value=config.IOS_DEVICE_NAME)

    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(
            config.DRIVER_REMOTE_URL,
            options=options
        )

    browser.config.timeout = float(config.DRIVER_TIMEOUT)
    browser.config._wait_decorator = selene.support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield driver

    attach.add_screenshot()
    attach.add_page_source()

    session_id = browser.driver.session_id

    with allure.step('Tear down app session'):
        browser.quit()

    attach.add_bstack_video(session_id)
