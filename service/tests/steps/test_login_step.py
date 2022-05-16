from pytest_bdd import given, parsers, when, then, scenario
from browsers import driver
from service.Pages.login import loginPage


@given("User Setups the Web Browser")
def userSetupTheWebBrowser():
    print("Passed")


@when(parsers.cfparse('User Navigates to "{urlToLoad}" Url'))
def userNavigateToUrl(urlToLoad):
    webdriver = driver.driver.get_driver()
    webdriver.maximize_window()
    webdriver.get("https://develop.crossfund.app/")
    print("URL loaded successfully", urlToLoad)


@then('User clicks on Login button')
def user_clicks_login_button():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.login_button()


@scenario("C:\\Users\\wajahat.kamal\\PycharmProjects\\CrossFund\\service\\tests\\features\\login.feature",
          'Verify User is '
          'successfully '
          'logged in')
def test_login_module():
    print("Test Successful!!!!!!!")


@scenario("C:\\Users\\wajahat.kamal\\PycharmProjects\\CrossFund\\service\\tests\\features\\login.feature",
          'Verify Internal Invitation sent successfully')
def test_internal_invite():
    print("Test Successful!!!!!!!")


@given('User is on the login page')
def login_page():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.login_page()


@when('User Enters "valid.username" on UserName Field on Login Page')
def user_name():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.login_username()


@then('User Enters "valid.password" on Password Field on Login Page')
def user_passwrd():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.login_password()


@then('User Clicks on Login Button on Login Page')
def user_passwrd():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.submit_button()


@then('User Successfully Logs in to CrossFund platform')
def home_page():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.home_page()


@then('User clicks on the Profile button')
def user_clicks_profile_button():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.user_clicks_profile_button()


@then('User clicks on Invitation from the left menu')
def user_clicks_invitation_button():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.user_clicks_invitation_button()


@then('User Enters the First Name')
def user_enters_first_name():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.user_enters_first_name()


@then('User Enters the Last Name')
def user_enters_last_name():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.user_enters_last_name()


@then('User Enters the Email Address')
def user_enters_invite_email():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.user_enters_invite_email()

@then('User Selects the Campaign from the dropdown Menu')
def user_selects_campaign():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.user_selects_campaign()

@then('User clicks on Send button')
def user_clicks_send_button():
    webdriver = driver.driver.get_driver()
    pglogin = loginPage(webdriver)
    pglogin.user_clicks_send_button()
