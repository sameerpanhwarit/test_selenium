from Task1 import SapSuccessFactorLogin

class RatingScaleNavigator:
    def __init__(self):
        self.success_factor_login = SapSuccessFactorLogin()

    def navigate_to_rating_scale(self):
        self.success_factor_login.login()

        current_url = self.success_factor_login.driver.current_url
        scrub_id = current_url.split("?")[1]
        print("Scrub ID:", scrub_id)

        rating_scale_url = f"https://hcm41preview.sapsf.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=form_rating_scale&itrModule=talent&{scrub_id}"
        self.success_factor_login.driver.get(rating_scale_url)

        


if __name__ == "__main__":
    rating_scale_navigator = RatingScaleNavigator()
    rating_scale_navigator.navigate_to_rating_scale()
