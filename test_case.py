import helpshop
import test_data1
def test_login():
    helpshop.load_broweser()
    helpshop.load_website(test_data1.url)
    helpshop.login_verify()
    helpshop.close_browser()