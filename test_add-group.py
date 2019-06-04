# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(selfself):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        success = True
        ws = self.wd
        wd.get('http://localhost/addressbook/')
        wd.find_element_by_name('user').click()
        wd.find_element_by_name('user').clear()
        wd.find_element_by_name('user').send_key('admin')
        wd.find_element_by_name('pass').click()
        wd.find_element_by_name('pass').clear()
        wd.find_element_by_name('pass').send_key('secret')
        wd.find_element_by_css_selector('input[type=\"submit\"]').click()
        wd.find_element_by_link_text('groups').click()
        wd.find_element_by_name('new').click()
        wd.find_element_by_name('group_name').click()
        wd.find_element_by_name('group_name').clear()
        wd.find_element_by_name('group_name').send_key('dfgsdf')
        wd.find_element_by_name('group_header').click()
        wd.find_element_by_name('group_header').clear()
        wd.find_element_by_name('group_header').send_key('dfgsdf')
        wd.find_element_by_name('group_footer').click()
        wd.find_element_by_name('group_footer').clear()
        wd.find_element_by_name('group_footer').send_key('dfgsdf')
        wd.find_element_by_name('submit').click()
        wd.find_element_by_link_text('group_page').click()
        wd.find_element_by_link_text('Logout').click()
        self.assertTrue(success)

    def teardown(selfself):
        self.wd.quit()

if __name__ == '__main__':
    # execute only if run as a script
    main()
