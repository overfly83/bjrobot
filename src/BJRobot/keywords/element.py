from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from keywordgroup import KeywordGroup
from BJRobot.utilities import System


# class Element(KeywordGroup):
class Element(KeywordGroup):

    def __init__(self):
        pass

    def find_element(self, by=By.ID, value=None):
        return self._current_browser().find_element(by, value)

    def find_element_by_class(self, class_name):
        return self._current_browser().find_element_by_class_name(class_name)

    def find_element_by_name(self, name):
        return self._current_browser().find_element_by_name(name)

    def find_element_by_id(self, id_):
        return self._current_browser().find_element_by_id(id_)

    def find_element_by_link_text(self, link_text):
        return self._current_browser().find_element_by_link_text(link_text)

    def find_element_by_partial_link_text(self, partial_link_text):
        return self._current_browser().find_element_by_partial_link_text(partial_link_text)

    def find_element_by_css_selector(self, css_selector):
        return self._current_browser().find_element_by_css_selector(css_selector)

    def find_element_by_xpath(self, xpath):
        return self._current_browser().find_element_by_xpath(xpath)

    def find_element_by_tag_name(self, tag_name):
        return self._current_browser().find_element_by_tag_name(tag_name)

    def find_elements(self, by=By.ID, value=None):
        return self._current_browser().find_elements(by, value)

    def find_elements_by_class(self, class_name):
        return self._current_browser().find_elements_by_class_name(class_name)

    def find_elements_by_name(self, name):
        return self._current_browser().find_elements_by_name(name)

    def find_elements_by_id(self, id_):
        return self._current_browser().find_elements_by_id(id_)

    def find_elements_by_link_text(self, link_text):
        return self._current_browser().find_elements_by_link_text(link_text)

    def find_elements_by_partial_link_text(self, partial_link_text):
        return self._current_browser().find_elements_by_partial_link_text(partial_link_text)

    def find_elements_by_css_selector(self, css_selector):
        return self._current_browser().find_elements_by_css_selector(css_selector)

    def find_elements_by_xpath(self, xpath):
        return self._current_browser().find_elements_by_xpath(xpath)

    def find_elements_by_tag_name(self, tag_name):
        return self._current_browser().find_elements_by_tag_name(tag_name)

    def element_should_contain_text(self, by=By.ID, value=None, expected=None):
        actual = self._get_text(by, value)
        if not expected in actual:
            message = "Element '%s' should have contained text '%s' but " \
                      "its text was '%s'." % ((by, value), expected, actual)
            raise AssertionError(message)

    def element_should_not_contain_text(self, by=By.ID, value=None, expected=None):
        actual = self._get_text(by, value)
        if expected in actual:
            message = "Element '%s' should not have contained text '%s' but " \
                      "its text was '%s'." % ((by, value), expected, actual)
            raise AssertionError(message)

    def element_should_contain_value(self, by=By.ID, value=None, expected=None):
        actual = self._get_value(by, value)
        if not expected in actual:
            message = "Element '%s' should have contained text '%s' but " \
                      "its text was '%s'." % ((by, value), expected, actual)
            raise AssertionError(message)

    def element_should_not_contain_value(self, by=By.ID, value=None, expected=None):
        actual = self._get_value(by, value)
        if expected in actual:
            message = "Element '%s' should not have contained text '%s' but " \
                      "its text was '%s'." % ((by, value), expected, actual)
            raise AssertionError(message)

    def element_should_be_enabled(self, by=By.ID, value=None):
        if not self.is_element_enabled(by, value):
            message = "Element '%s' is not enabled currently." % (by,value).__str__()
            raise AssertionError(message)

    def element_should_not_be_enabled(self, by=By.ID, value=None):
        if self.is_element_enabled(by, value):
            message = "Element '%s' is enabled currently." % (by,value).__str__()
            raise AssertionError(message)

    def click_element_by_id(self, id_):
        self.find_element_by_id(id_).click()

    def click_element_by_name(self, name):
        self.find_element_by_name(name).click()

    def click_element_by_xpath(self, xpath):
        self.find_element_by_xpath(xpath).click()

    def click_element(self, by=By.ID, value=None):
        self.find_element(by, value).click()

    def double_click_element_by_id(self, id_):
        element = self.find_element_by_id(id_)
        ActionChains(self._current_browser()).double_click(element).perform()

    def double_click_element_by_name(self, name):
        element = self.find_element_by_name(name)
        ActionChains(self._current_browser()).double_click(element).perform()

    def double_click_element_by_xpath(self, xpath):
        element = self.find_element_by_xpath(xpath)
        ActionChains(self._current_browser()).double_click(element).perform()

    def double_click_element(self, by=By.ID, value=None):
        element = self.find_element(by, value)
        ActionChains(self._current_browser()).double_click(element).perform()

    def click_element_at_coordinates_by_id(self, id_, xoffset=0, yoffset=0):
        element = self.find_element_by_id(id_)
        ActionChains(self._current_browser()).move_to_element(element).move_by_offset(xoffset, yoffset).click().perform()

    def click_element_at_coordinates_by_name(self, name, xoffset=0, yoffset=0):
        element = self.find_element_by_name(name)
        ActionChains(self._current_browser()).move_to_element(element).move_by_offset(xoffset, yoffset).click().perform()

    def click_element_at_coordinates_by_xpath(self, xpath, xoffset=0, yoffset=0):
        element = self.find_element_by_xpath(xpath)
        ActionChains(self._current_browser()).move_to_element(element).move_by_offset(xoffset, yoffset).click().perform()

    def click_element_at_coordinates(self, by=By.ID, value=None, xoffset=0, yoffset=0):
        element = self.find_element(by, value)
        ActionChains(self._current_browser()).move_to_element(element).move_by_offset(xoffset, yoffset).click().perform()

    def drag_and_drop(self, source_by=By.ID, source_value=None, target_by=By.ID, target_value=None):
        src_elem = self.find_element(source_by, source_value)
        trg_elem = self.find_element(target_by, target_value)
        ActionChains(self._current_browser()).drag_and_drop(src_elem, trg_elem).perform()

    def drag_and_drop_by_xpath(self, source_xpath, target_xpath):
        src_elem = self.find_element_by_xpath(source_xpath)
        trg_elem = self.find_element_by_xpath(target_xpath)
        ActionChains(self._current_browser()).drag_and_drop(src_elem, trg_elem).perform()

    def drag_and_drop_by_offset(self, source_by=By.ID, source_value=None, xoffset=0, yoffset=0):
        src_elem = self.find_element(source_by, source_value)
        ActionChains(self._current_browser()).drag_and_drop_by_offset(src_elem, xoffset, yoffset).perform()

    def drag_and_drop_by_offset_by_xpath(self, source_xpath, xoffset, yoffset):
        src_elem = self.find_element_by_xpath(source_xpath)
        ActionChains(self._current_browser()).drag_and_drop_by_offset(src_elem, xoffset, yoffset).perform()

    def mouse_down(self, by=By.ID, value=None):
        element = self.find_element(by, value)
        if element is None:
            raise AssertionError("ERROR: Element %s not found." % (by, value).__str__())
        ActionChains(self._current_browser()).click_and_hold(element).perform()

    def mouse_down_by_xpath(self, xpath):
        element = self.find_element_by_xpath(xpath)
        if element is None:
            raise AssertionError("ERROR: Element %s not found." % xpath)
        ActionChains(self._current_browser()).click_and_hold(element).perform()

    def mouse_down_by_id(self, id_):
        element = self.find_element_by_id(id_)
        if element is None:
            raise AssertionError("ERROR: Element %s not found." % id_)
        ActionChains(self._current_browser()).click_and_hold(element).perform()

    def mouse_down_by_name(self, name):
        element = self.find_element_by_name(name)
        if element is None:
            raise AssertionError("ERROR: Element %s not found." % name)
        ActionChains(self._current_browser()).click_and_hold(element).perform()

    def set_value(self, by=By.ID, value=None, key=None):
        if key.startswith('\\') and len(key) > 1:
            key = System.map_ascii_key_code_to_key(int(key[1:]))
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(key)

    def set_value_by_id(self, id_, key=None):
        if key.startswith('\\') and len(key) > 1:
            key = System.map_ascii_key_code_to_key(int(key[1:]))
        element = self.find_element_by_id(id_)
        element.clear()
        element.send_keys(key)

    def set_value_by_name(self, name, key=None):
        if key.startswith('\\') and len(key) > 1:
            key = System.map_ascii_key_code_to_key(int(key[1:]))
        element = self.find_element_by_name(name)
        element.clear()
        element.send_keys(key)

    def set_value_by_xpath(self, xpath, key=None):
        if key.startswith('\\') and len(key) > 1:
            key = System.map_ascii_key_code_to_key(int(key[1:]))
        element = self.find_element_by_xpath(xpath)
        element.clear()
        element.send_keys(key)

    def is_element_enabled_by_id(self, id_):
        element = self.find_element_by_id(id_)
        if not element.is_enabled():
            return False
        read_only = element.get_attribute('readonly')
        if read_only == 'readonly' or read_only == 'true':
            return False
        return True

    def is_element_enabled_by_name(self, name):
        element = self.find_element_by_name(name)
        if not element.is_enabled():
            return False
        read_only = element.get_attribute('readonly')
        if read_only == 'readonly' or read_only == 'true':
            return False
        return True

    def is_element_enabled_by_xpath(self, xpath):
        element = self.find_element_by_xpath(xpath)
        if not element.is_enabled():
            return False
        read_only = element.get_attribute('readonly')
        if read_only == 'readonly' or read_only == 'true':
            return False
        return True

    def is_element_enabled(self, by=By.ID, value=None):
        element = self.find_element(by, value)
        if not element.is_enabled():
            return False
        read_only = element.get_attribute('readonly')
        if read_only == 'readonly' or read_only == 'true':
            return False
        return True

    def is_element_visible_by_id(self, id_):
        element = self.find_element_by_id(id_)
        if element is not None:
            return element.is_displayed()
        return None

    def is_element_visible_by_name(self, name):
        element = self.find_element_by_name(name)
        if element is not None:
            return element.is_displayed()
        return None

    def is_element_visible_by_xpath(self, xpath):
        element = self.find_element_by_xpath(xpath)
        if element is not None:
            return element.is_displayed()
        return None

    def is_element_visible(self, by=By.ID, value=None):
        element = self.find_element(by, value)
        if element is not None:
            return element.is_displayed()
        return None

    def is_element_present_by_id(self, id_):
        return (self.find_element_by_id(id_) is not None)

    def is_element_present_by_name(self, name):
        return (self.find_element_by_id(name) is not None)

    def is_element_present_by_xpath(self, xpath):
        return (self.find_element_by_xpath(xpath) is not None)

    def is_element_present(self, by=By.ID, value=None):
        return (self.find_element(by, value) is not None)

    def _get_text_by_id(self, id_):
        element = self.find_element_by_id(id_)
        if element is not None:
            return element.text
        return None

    def _get_text_by_name(self, name):
        element = self.find_element_by_name(name)
        if element is not None:
            return element.text
        return None

    def _get_text_by_xpath(self, xpath):
        element = self.find_element_by_xpath(xpath)
        if element is not None:
            return element.text
        return None

    def _get_text(self, by=By.ID, value=None):
        element = self.find_element(by, value)
        if element is not None:
            return element.text
        return None

    def _get_value_by_id(self, id_):
        element = self.find_element_by_id(id_)
        return element.get_attribute('value') if element is not None else None

    def _get_value_by_name(self, name):
        element = self.find_element_by_name(name)
        return element.get_attribute('value') if element is not None else None

    def _get_value_by_xpath(self, xpath):
        element = self.find_element_by_xpath(xpath)
        return element.get_attribute('value') if element is not None else None

    def _get_value(self, by=By.ID, value=None):
        element = self.find_element(by, value)
        return element.get_attribute('value') if element is not None else None

    def _map_ascii_key_code_to_key(self, key_code):
        map = {
            0: Keys.NULL,
            8: Keys.BACK_SPACE,
            9: Keys.TAB,
            10: Keys.RETURN,
            13: Keys.ENTER,
            24: Keys.CANCEL,
            27: Keys.ESCAPE,
            32: Keys.SPACE,
            42: Keys.MULTIPLY,
            43: Keys.ADD,
            44: Keys.SEPARATOR,
            45: Keys.SUBTRACT,
            56: Keys.DECIMAL,
            57: Keys.DIVIDE,
            59: Keys.SEMICOLON,
            61: Keys.EQUALS,
            127: Keys.DELETE
        }
        key = map.get(key_code)
        if key is None:
            key = chr(key_code)
        return key
