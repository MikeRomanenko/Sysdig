from selenium import webdriver
import base_locators as locators
from time import sleep
driver = webdriver.Chrome('/Users/t-1007/chromedriver')


class TestLogin:

    def test_login_page(self):

        print("\n* Visit login page")
        driver.get(locators.loginPage)
        assert locators.loginTitle in driver.title
        sleep(0.5)

        print("* Verify registration url.")
        driver.find_element(*locators.registerLink).click()
        assert driver.current_url == locators.signUpUrl
        driver.back()
        sleep(2)

        print("* Verify unable to login with a 'bad' user.")
        driver.find_element(*locators.UsernameField).send_keys(locators.user)
        driver.find_element(*locators.PasswordField).send_keys(locators.password)
        driver.find_element(*locators.loginButton).click()
        sleep(0.2)
        assert 'Credentials are not valid' in driver.find_element(*locators.invalidLoginMessage).text
        sleep(2)

        print("* Verify login with Google.")
        driver.find_element(*locators.registerGoogle).click()
        assert driver.title == locators.signInGoogleTitle
        driver.back()
        sleep(2)

        print("* Verify login with SAML.")
        driver.find_element(*locators.registerSAML).click()
        assert driver.current_url == locators.signInSamlUrl
        driver.back()
        sleep(2)

        print("* Verify login with Open Id.")
        driver.find_element(*locators.registerOpenID).click()
        assert driver.current_url == locators.signInOpenIdUrl
        driver.quit()