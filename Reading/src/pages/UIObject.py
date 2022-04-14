# coding=utf-8
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Reading.src.pages.Browser import Browser
from Reading.src.pages.utils import Create_dir


class UiObject:
    def __init__(self, by, locator, **kwargs):
        self.__by = by
        self.__locator = locator
        self.__web_element = kwargs.get("web_element", None)

    @staticmethod
    def from_web_element(web_element):
        """
        If you want to initiate UiObject from a WebElement:
        aka return of driver.find_element(By.SOMETHING, "//something")
        Use this method.
        :param web_element: WebElement object
        :return: UiObject object instance
        """
        return UiObject(by=None, locator=None, web_element=web_element)

    def get_element(self, wait=10):
        """
        Will use WebDriver to locate element in the DOM
        :param wait: INT, If the element is not present on the page at
                          the time of this call, how long you want to wait for it
        :return: WebElement object
        """
        if self.__web_element:
            return self.__web_element
        self.wait_to_appear(wait)
        return Browser.get_driver().find_element(self.by, self.locator)

    def get_elements(self, wait=10):
        """
        Will use WebDriver to locate elements in the DOM
        :param wait: INT, If the element is not present on the page at
                          the time of this call, how long you want to wait for it
        :return: LIST of WebElement objects
        """
        if self.__web_element:
            return [self.__web_element]
        self.wait_to_appear(wait)
        return Browser.get_driver().find_elements(self.by, self.locator)

    @property
    def locator(self):
        """
        :return: STRING, locator this object was initialize with
        """
        return self.__locator

    @property
    def by(self):
        """
        :return: STRING, By ID this object was initialize with aka By.XPATH or By.ID
        """
        return self.__by

    def exists(self, wait=10):
        """
        :param wait: INT, seconds to wait before returning verdict
        :return: BOOLEAN, if object currently exists in the DOM
        """
        try:
            WebDriverWait(Browser.get_driver(), wait).until(
                EC.presence_of_element_located((self.by, self.locator)))
            return True
        except:
            return False

    def visible(self, wait=1):
        """
        :param wait: INT, seconds to wait before returning verdict
        :return: BOOLEAN, if object is currently visible on the page
        """
        try:
            WebDriverWait(Browser.get_driver(), wait).until(
                EC.invisibility_of_element_located((self.by, self.locator)))
            return False
        except:
            return True

    def clickable(self, wait=1):
        """
        :param wait: INT, seconds to wait before returning verdict
        :return: BOOLEAN, if object exists in the DOM
        """
        try:
            WebDriverWait(Browser.get_driver(), wait).until(
                EC.element_to_be_clickable((self.by, self.locator)))
            return True
        except:
            return False

    def wait_to_appear(self, wait=10):
        """
        :param wait: INT, how long you want to wait for the element to appear
        :return: self (UiObject)
        """
        if self.exists(wait):
            return self
        raise AssertionError("Locator did not appear: {} in {} seconds!"
                             .format(self.locator, wait))

    def wait_to_disappear(self, wait=10):
        """
        :param wait: INT, how long you want to wait for the element to disappear
        :return: self (UiObject)
        """
        if not self.visible(wait):
            return self
        raise AssertionError("Locator did not disappear: {} in {} seconds!"
                             .format(self.locator, wait))

    def wait_to_be_clickable(self, wait=10):
        """
        :param wait: INT, how long you want to wait for the element to be click-able
        :return: self (UiObject)
        """
        if self.clickable(wait):
            return self
        if self.exists():
            raise AssertionError("Locator did not become click-able: {} in {} seconds"
                                 .format(self.locator, wait))
        raise AssertionError("Locator does not exist: {}".format(self.locator))

    def get_text(self, encoding=None, wait=10):
        """
        :param encoding: STRING, aka "utf-8", if encoding is provided, the text will be
                                 automatically encoded and returned to the caller
        :param wait: INT, how long you want to wait for the element to appear
        :return: STRING, text value
        """
        text = self.get_element(wait).text
        return text.encode(encoding) if encoding else text

    def set_text(self, value, wait=10):
        """
        :param value: STRING, text value to type on the element
        :param wait: INT, how long you want to wait for the element to appear
        :return: STRING, text value
        """
        self.get_element(wait).send_keys(Keys.CONTROL + "a")
        self.get_element(wait).send_keys(Keys.DELETE)
        self.get_element(wait).send_keys(value)
        return self

    def clear_text(self, wait=10):
        """
        :param value: STRING, text value to type on the element
        :param wait: INT, how long you want to wait for the element to appear
        """
        self.get_element(wait).send_keys(Keys.CONTROL + "a")
        self.get_element(wait).send_keys(Keys.DELETE)
        return self

    def press_key(self, key, use_ac=False, wait=10):
        """
        :param key: STRING, special key code aka Keys.ENTER
        :param use_ac: BOOLEAN, if you want to use ActionChains for this operation
        :param wait: INT, how long you want to wait for the element to appear
        :return: self (UiObject)
        """
        if use_ac:
            ActionChains(Browser.get_driver()).send_keys(key).perform()
        else:
            self.get_element(wait).send_keys(key)
        return self

    def get_property(self, value, wait=10):
        """
        :param value: STRING, aka "class" or "name" etc
        :param wait: INT, how long you want to wait for the element to appear
        :return: STRING, attribute value as text
        """
        return self.get_element(wait).get_property(value)

    def get_attribute(self, value, wait=10):
        """
        :param value: STRING, aka "class" or "name" etc
        :param wait: INT, how long you want to wait for the element to appear
        :return: STRING, attribute value as text
        """
        return self.get_element(wait).get_attribute(value)

    def click(self, use_ac=False, wait=10):
        """
        :param use_ac: BOOLEAN, if you want to use ActionChains for this operation
        :param wait: INT, how long you want to wait for the element to appear
        :return:
        """
        if use_ac:
            ActionChains(Browser.get_driver()).move_to_element(
                self.get_element(wait)).click().perform()
        else:
            self.get_element(wait).click()
        return self

    def ScrShot(self, filename, location=''):
        """
        :param filename: String, name of image that your want to take screen
        :param location: String, the Folder of image file that you want to locate after screen shot
        :return: None
        """
        try:
            dir_img = os.getcwd()
            if location == '':
                path = dir_img +'\\Reading Test Results\\img'
            else:
                path = dir_img +'\\Reading Test Results\\' + location +'\\img'                
            Create_dir(path)
            file = path + '\\' + filename + '.png'
            self.driver.get_screenshot_as_file(file)
        except Exception as e:
            print('Error: ', e)

        
