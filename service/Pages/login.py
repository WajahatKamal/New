import time
from seleniumpagefactory.Pagefactory import PageFactory
from service.testDataReader import userData


class loginPage(PageFactory):

    def __init__(self, driver):
        # It is necessary to initialise driver as page class member to implement Page Factory
        super().__init__()
        self.driver = driver

    # define locators dictionary where key name will become WebElement using PageFactory
    locators = {
        "userNameField": ('XPATH', "//input[@name='email']"),
        "passwordField": ('XPATH', "//input[@name='password']"),
        "loginButton": ('XPATH', "//button[@class='ant-btn ant-btn-primary']"),
        "submitButton": ('XPATH', "//button[@type='submit']"),
        "profilebutton": ('XPATH', "//span[@class='ant-avatar ant-avatar-circle ant-avatar-image']//img"),
        "invitebutton": ('XPATH', "//span[contains(text(),'Invites')]"),
        "firstname": ('XPATH', "//input[@name='first_name']"),
        "lastname": ('XPATH', "//input[@name='last_name']"),
        "emailinvite": ('XPATH', "//input[@name='email']"),
        "sendbutton": ('XPATH', "//button[@type='submit']"),
        "campaignselectdropdown": ('XPATH', "//span[@title='Select Deal']"),
        "campaignselect": ('XPATH', "//div[contains(text(),'Motus Operandi')]"),
    }

    def login_username(self):
        self.userNameField.set_text(userData.userName)  # edtUserName become class variable using PageFactory

    def login_password(self):
        self.passwordField.set_text(userData.password)

    def login_button(self):
        self.loginButton.click_button()

    def submit_button(self):
        self.submitButton.click_button()
        time.sleep(5)

    def login_page(self):
        pass

    def home_page(self):
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@class='ant-typography']").text
        assert "Welcome back" in element

    def user_clicks_profile_button(self):
        time.sleep(5)
        self.profilebutton.click_button()

    def user_clicks_invitation_button(self):
        time.sleep(2)
        self.invitebutton.click_button()

    def user_enters_first_name(self):
        time.sleep(2)
        self.firstname.set_text(userData.firstname)

    def user_enters_last_name(self):
        time.sleep(2)
        self.lastname.set_text(userData.lastname)

    def user_enters_invite_email(self):
        time.sleep(2)
        self.emailinvite.set_text(userData.emailinvite)

    def user_selects_campaign(self):
        time.sleep(2)
        self.campaignselectdropdown.click_button()
        time.sleep(2)
        self.campaignselect.click_button()

    def user_clicks_send_button(self):
        time.sleep(2)
        self.sendbutton.click_button()

