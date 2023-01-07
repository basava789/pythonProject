import helpnop
import test_datenop

def test_login():
    helpnop.load_browcer()
    helpnop.load_website(test_datenop.url)
    helpnop.login_verfiy()
    helpnop.close_browcer()
