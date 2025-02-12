from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value = 'Continue']"
    yes_radio_button_xpath = "//input[@name = 'newsletter'][@value = 1]"
    duplicate_email_warning_xpath = "//div[@id = 'account-register']//following-sibling::div"
    privacy_policy_warning_xpath = "//div[@id = 'account-register']//following-sibling::div"
    first_name_warning_xpath = "//input[@id = 'input-firstname']//following-sibling::div"
    last_name_warning_xpath = "//input[@id = 'input-lastname']//following-sibling::div"
    email_warning_xpath = "//input[@id = 'input-email']//following-sibling::div"
    telephone_warning_xpath = "//input[@id = 'input-telephone']//following-sibling::div"
    password_warning_xpath = "//input[@id = 'input-password']//following-sibling::div"

    def enter_first_name(self, first_name_text):
        self.type_into_element(first_name_text,"first_name_field_id",self.first_name_field_id)

    def enter_last_name(self, last_name_text):
        self.type_into_element(last_name_text, "last_name_field_id",self.last_name_field_id)

    def enter_email(self, email_text):
        self.type_into_element(email_text,"email_field_id",self.email_field_id)

    def enter_telephone(self, telephone_text):
        self.type_into_element(telephone_text,"telephone_field_id",self.telephone_field_id)

    def enter_password(self, password_text):
        self.type_into_element(password_text,"password_field_id",self.password_field_id)

    def enter_password_confirm(self, password_text_confirm):
        self.type_into_element(password_text_confirm,"confirm_password_field_id",self.confirm_password_field_id)

    def select_agree_checkbox_field(self):
        self.element_click("agree_field_name",self.agree_field_name)

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def select_yes_radio_button(self):
        self.element_click("yes_radio_button_xpath",self.yes_radio_button_xpath)

    def register_an_account(self, first_name_text, last_name_text, email_text, telephone_text, password_text,
                            password_text_confirm, yes_or_no, privacy_policy):
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email(email_text)
        self.enter_telephone(telephone_text)
        self.enter_password(password_text)
        self.enter_password_confirm(password_text_confirm)
        if yes_or_no.__eq__("yes"):
            self.select_yes_radio_button()
        if privacy_policy.__eq__("select"):
            self.select_agree_checkbox_field()
        return self.click_on_continue_button()

    def retrieve_duplicate_email_warning(self):
        self.retrieve_element_text("duplicate_email_warning_xpath",self.duplicate_email_warning_xpath)

    def retrieve_privacy_policy_warning(self):
        self.retrieve_element_text("privacy_policy_warning_xpath",self.privacy_policy_warning_xpath)

    def retrieve_first_name_warning(self):
        self.retrieve_element_text("first_name_warning_xpath",self.first_name_warning_xpath)

    def retrieve_last_name_warning(self):
        self.retrieve_element_text("last_name_warning_xpath",self.last_name_warning_xpath)

    def retrieve_email_warning(self):
        self.retrieve_element_text("email_warning_xpath",self.email_warning_xpath)

    def retrieve_telephone_warning(self):
        self.retrieve_element_text("telephone_warning_xpath",self.telephone_warning_xpath)

    def retrieve_password_warning(self):
        self.retrieve_element_text("password_warning_xpath",self.password_warning_xpath)

    def verify_all_warnings(self, expected_privacy_policy_warning, expected_first_name_warning,
                            expected_last_name_warning, expected_email_warning,
                            expected_telephone_warning, expected_password_warning):
        actual_privacy_policy_warning = self.retrieve_privacy_policy_warning()
        actual_first_name_warning = self.retrieve_first_name_warning()
        actual_last_name_warning = self.retrieve_last_name_warning()
        actual_email_warning = self.retrieve_email_warning()
        actual_telephone_warning = self.retrieve_telephone_warning()
        actual_password_warning = self.retrieve_password_warning()

        status = False

        if expected_privacy_policy_warning.__eq__(actual_privacy_policy_warning):
            if expected_first_name_warning.__eq__(actual_first_name_warning):
                if expected_last_name_warning.__eq__(actual_last_name_warning):
                    if expected_email_warning.__eq__(actual_email_warning):
                        if expected_telephone_warning.__eq__(actual_telephone_warning):
                            if expected_password_warning.__eq__(actual_password_warning):
                                status = True
        return status
