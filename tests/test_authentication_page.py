from credentials import Credentials
from pages.authentication_page import AuthenticationPage
from urls import Urls


class TestAuthenticationPage:

    def test_authentication_pg_01_login_invalid_credentials(self, driver):
        authentication_pg = AuthenticationPage(driver)
        authentication_pg.navigate(Urls.authentication_pg_url)
        authentication_pg.fill_email(Credentials.login_invalid_email)
        authentication_pg.fill_password(Credentials.login_invalid_password)
        authentication_pg.sign_in_invalid()
        assert 'Authentication failed' in authentication_pg.get_alert_message_text()

    def test_authentication_pg_02_login_valid_credentials(self, driver):
        authentication_pg = AuthenticationPage(driver)
        authentication_pg.navigate(Urls.authentication_pg_url)
        authentication_pg.fill_email(Credentials.login_valid_email)
        authentication_pg.fill_password(Credentials.login_valid_password)
        account_pg = authentication_pg.sign_in_valid()
        assert account_pg.get_url() == Urls.account_url
