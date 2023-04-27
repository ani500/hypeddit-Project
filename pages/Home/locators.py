
class Locators():


    _logout_hypeddit = "//ul[@class='dropdown-menu']//input[@name='logout']"

    @property
    def logout_hypeddit(self):
        return self._logout_hypeddit

    _trial_text = "//h2[text()='START YOUR FREE 7-DAY TRIAL']"

    @property
    def trial_text(self):
        return self._trial_text

    _3_dot_menu = "//img[@alt='three-dot-menu']"

    @property
    def trial_text(self):
        return self._trial_text



