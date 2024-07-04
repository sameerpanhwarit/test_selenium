from HelperMethods import Helper
from time import sleep

class SapSuccessFactorLogin:
    def __init__(self):
        self.helper = Helper()
        self.company_id = 'codebotforT1'
        self.username = "sfadmin"
        self.password = "Part@dc68"

    def login(self):
        # self.helper.driver.get("https://pmsalesdemo8.successfactors.com")
        self.helper.driver.get('https://hcm41preview.sapsf.com/sf/start/#/companyEntry')
        self.helper.driver.implicitly_wait(10)

        company_id = self.helper.waitforElementtobevisible('//*[@id="__input0-inner"]', "xpath")

        if company_id is True:
            company_id_input = self.helper.getElement('//*[@id="__input0-inner"]', "xpath")
            company_id_input.send_keys(self.company_id)
            self.helper.clickElement('//*[@id="continueToLoginBtn-BDI-content"]', 'xpath')
        else:
            print("Company id is not visible.")
        username_input = self.helper.getElement('//*[@id="__input1-inner"]', "xpath")
        password_input = self.helper.getElement('//*[@id="__input2-inner"]', "xpath")
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        self.helper.clickElement('//*[@id="__button0-content"]', 'xpath')
        self.driver = self.helper.driver
        sleep(4)

# if __name__ == "__main__":
#     success_factor_login = SapSuccessFactorLogin()
#     success_factor_login.login()
