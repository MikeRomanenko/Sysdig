from selenium.webdriver.common.by import By

user = 'test@gmail.com'
password = 'password'

loginButton = (By.ID, 'ember1652')
forgotPass = (By.XPATH, '//*[@id="ember1720"]')
invalidLoginMessage = (By.CLASS_NAME, 'login__error-display')
UsernameField = (By.ID, 'ember1642')
PasswordField = (By.ID, 'ember1643')

homePage = 'https://app.sysdigcloud.com/'
loginPage = homePage + '#/login'
loginTitle = 'Sysdig Monitor'

registerLink = (By.XPATH, '//*[@id="ember1635"]/div[3]/a')
registerGoogle = (By.XPATH, '//*[@id="ember1635"]/div[2]/a[1]')
registerSAML = (By.XPATH, '//*[@id="ember1670"]')
registerOpenID = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/a[3]')

signInGoogleTitle = 'Sign in - Google Accounts'
signInSamlUrl = "https://app.sysdigcloud.com/#/samlAuthentication"
signInOpenIdUrl = "https://app.sysdigcloud.com/#/openIdAuthentication"
signUpUrl = "https://sysdig.com/company/start-free/"
forgotPassUrl = "https://app.sysdigcloud.com/#/forgotPassword"
