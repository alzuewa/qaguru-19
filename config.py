import os
from dotenv import load_dotenv

load_dotenv()

BSTACK_USER_NAME = os.getenv('BSTACK_USER_NAME')
BSTACK_ACCESS_KEY = os.getenv('BSTACK_ACCESS_KEY')
BSTACK_APP_NAME = os.getenv('BSTACK_APP_NAME', 'bs://sample.app')
BSTACK_SESSION_URL = os.getenv('BSTACK_SESSION_URL', 'https://api.browserstack.com/app-automate/sessions/')

DRIVER_TIMEOUT = os.getenv('DRIVER_TIMEOUT', '10.0')
DRIVER_REMOTE_URL = os.getenv('DRIVER_REMOTE_URL', 'http://hub.browserstack.com/wd/hub')

ANDROID_PLATFORM_VERSION = os.getenv('ANDROID_PLATFORM_VERSION', '9.0')
ANDROID_DEVICE_NAME = os.getenv('ANDROID_PLATFORM_VERSION', 'Google Pixel 3')

IOS_PLATFORM_VERSION = os.getenv('IOS_PLATFORM_VERSION', '16')
IOS_DEVICE_NAME = os.getenv('IOS_DEVICE_NAME', 'iPhone 13')
