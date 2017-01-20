from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from keywordgroup import KeywordGroup
from BJRobot.utilities import System
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class Element(KeywordGroup):

    def __init__(self):
        self.__default_implicit_wait_in_secs = self._default_implicit_wait_in_secs

    def wait_until_page_contains_element(self, locator, timeout=30):
        """
        Let the script wait until the page contain the expected element.
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | wait until page contains element | id=kw | 30 |
        """
        (prefix, criteria) = self._parse_locator(locator)
        self._safe_find(by=prefix, value=criteria, timeout=timeout)

    def wait_until_page_not_contains_element(self, locator, timeout=30):
        """
        Let the script wait until the page not contain the expected element.
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | wait until page not contains element | id=kw | 30 |
        """
        WebDriverWait(self._get_current_browser(), timeout, poll_frequency=0.1) \
            .until(ec.invisibility_of_element_located(locator=locator))

    def find_element(self, locator, timeout=30):
        """
        Find single element from current page and return it back.
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | find element | id=kw | 30 |
        """
        (prefix, criteria) = self._parse_locator(locator)
        return self._safe_find(by=prefix, value=criteria, timeout=timeout)

    def find_element_by_class(self, class_name, timeout=30):
        """
        Find element by class name
        Example:
        | find element by class | classname | 30 |
        """
        return self._safe_find(by=By.CLASS_NAME, value=class_name, timeout=timeout)

    def find_element_by_name(self, name, timeout=30):
        """
        Find element by class name
        Example:
        | find element by class | name | 30 |
        """
        return self._safe_find(by=By.NAME, value=name, timeout=timeout)

    def find_element_by_id(self, id_, timeout=30):
        """
        Find element by class id
        Example:
        | find element by id | id | 30 |
        """
        return self._safe_find(by=By.ID, value=id_, timeout=timeout)

    def find_element_by_link_text(self, link_text, timeout=30):
        """
        Find element by class link text
        Example:
        | find element by link text | linktext | 30 |
        """
        return self._safe_find(by=By.LINK_TEXT, value=link_text, timeout=timeout)

    def find_element_by_partial_link_text(self, partial_link_text, timeout=30):
        """
        Find element by partial link text
        Example:
        | find element by partial link text | partiallinktext | 30 |
        """
        return self._safe_find(by=By.PARTIAL_LINK_TEXT, value=partial_link_text, timeout=timeout)

    def find_element_by_css_selector(self, css_selector, timeout=30):
        """
        Find element by css selector
        Example:
        | find element by css selector | cssselector | 30 |
        """
        return self._safe_find(by=By.CSS_SELECTOR, value=css_selector, timeout=timeout)

    def find_element_by_xpath(self, xpath, timeout=30):
        """
        Find element by xpath
        Example:
        | find element by xpath | xpath | 10 |
        """
        return self._safe_find(by=By.XPATH, value=xpath, timeout=timeout)

    def find_element_by_tag_name(self, tag_name, timeout=30):
        """
        Find element by tag name
        Example:
        | find element by tag name | tagname | 30 |
        """
        return self._safe_find(by=By.TAG_NAME, value=tag_name, timeout=timeout)

    def find_elements(self, locator, timeout=30):
        """
        Find multiple elements from the current page, return the element list.
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | find elements | xpath=//div | 30 |
        """
        (prefix, criteria) = self._parse_locator(locator)
        return self._safe_finds(by=prefix, value=criteria, timeout=timeout)

    def find_elements_by_class(self, class_name, timeout=30):
        """
        Find elements by class name
        Example:
        | find elements by class | class_name | 20 |
        """
        return self._safe_finds(by=By.CLASS_NAME, value=class_name, timeout=timeout)

    def find_elements_by_name(self, name, timeout=30):
        """
        Find elements by name
        Example:
        | find elements by name | name | 20 |
        """
        return self._safe_finds(by=By.NAME, value=name, timeout=timeout)

    def find_elements_by_id(self, id_, timeout=30):
        """
        Find elements by id
        Example:
        | find elements by id | id | 20 |
        """
        return self._safe_finds(by=By.ID, value=id_, timeout=timeout)

    def find_elements_by_link_text(self, link_text, timeout=30):
        """
        Find elements by link text
        Example:
        | find elements by link text | linktext | 20 |
        """
        return self._safe_finds(by=By.LINK_TEXT, value=link_text, timeout=timeout)

    def find_elements_by_partial_link_text(self, partial_link_text, timeout=30):
        """
        Find elements by partial link text
        Example:
        | find elements by partial link text | partiallinktext | 20 |
        """
        return self._safe_finds(by=By.PARTIAL_LINK_TEXT, value=partial_link_text, timeout=timeout)

    def find_elements_by_css_selector(self, css_selector, timeout=30):
        """
        Find elements by css selector
        Example:
        | find elements by css selector | cssselector | 20 |
        """
        return self._safe_finds(by=By.CSS_SELECTOR, value=css_selector, timeout=timeout)

    def find_elements_by_xpath(self, xpath, timeout=30):
        """
        Find elements by xpath
        Example:
        | find elements by xpath | //div[text='hello'] | 20 |
        """
        return self._safe_finds(by=By.XPATH, value=xpath, timeout=timeout)

    def find_elements_by_tag_name(self, tag_name, timeout=30):
        """
        Find elements by tag name
        Example:
        | find elements by tag name | tagname | 20 |
        """
        return self._safe_finds(by=By.TAG_NAME, value=tag_name, timeout=timeout)

    def element_should_contain_text(self, locator, expected=None, timeout=30):
        """
        Assert if the element contains expected text
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | element should contain text | id=kw | expectedtext |
        """
        (prefix, criteria) = self._parse_locator(locator)
        actual = self._get_text(locator, timeout=timeout)
        if expected not in actual:
            message = "Element '%s' should have contained text '%s' but " \
                      "its text was '%s'." % ((prefix, criteria), expected, actual)
            raise AssertionError(message)

    def element_should_not_contain_text(self, locator, expected=None, timeout=30):
        """
        Assert the element should not contain expected text
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | element should not contain text | id=kw | expectedtext |
        """
        (prefix, criteria) = self._parse_locator(locator)
        actual = self._get_text(locator, timeout=timeout)
        if expected in actual:
            message = "Element '%s' should not have contained text '%s' but " \
                      "its text was '%s'." % ((prefix, criteria), expected, actual)
            raise AssertionError(message)

    def element_should_contain_value(self, locator, expected=None, timeout=30):
        """
        Assert if the element contains expected value
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | element should contain value | id=kw | expectedvalue |
        """
        (prefix, criteria) = self._parse_locator(locator)
        actual = self._get_value(locator, timeout=timeout)
        if expected not in actual:
            message = "Element '%s' should have contained text '%s' but " \
                      "its text was '%s'." % ((prefix, criteria), expected, actual)
            raise AssertionError(message)

    def element_should_not_contain_value(self, locator, expected=None, timeout=30):
        """
        Assert the element should not contain expected text
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | element should not contain text | id=kw | expectedvalue |
        """
        (prefix, criteria) = self._parse_locator(locator)
        actual = self._get_value(locator, timeout=timeout)
        if expected in actual:
            message = "Element '%s' should not have contained text '%s' but " \
                      "its text was '%s'." % ((prefix, criteria), expected, actual)
            raise AssertionError(message)

    def element_should_be_enabled(self, locator, timeout=30):
        """
        Assert if the element should be enabled
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | element should be enabled | id=kw |
        """
        (prefix, criteria) = self._parse_locator(locator)
        if not self.is_element_enabled(locator, timeout=timeout):
            message = "Element '%s' is not enabled currently." % (prefix, criteria).__str__()
            raise AssertionError(message)

    def element_should_not_be_enabled(self, locator, timeout=30):
        """
        Assert if the element should not be enabled
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | element should not be enabled | id=kw |
        """
        (prefix, criteria) = self._parse_locator(locator)
        if self.is_element_enabled(locator, timeout=timeout):
            message = "Element '%s' is enabled currently." % (prefix, criteria).__str__()
            raise AssertionError(message)

    def click_element(self, locator, timeout=30):
        """
        Click the element by its element locator
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | click element | id = kw |
        """
        (prefix, criteria) = self._parse_locator(locator)
        element = self._safe_find(prefix, criteria, timeout)
        self._safe_click(element, timeout=30)

    def click_element_by_id(self, id_, timeout=30):
        """
        Click the element by its element id
        Example:
        | click element by id | id |
        """
        element = self._safe_find(by=By.ID, value=id_, timeout=timeout)
        self._safe_click(element, timeout=30)

    def click_element_by_name(self, name, timeout=30):
        """
        Click the element by its element name
        Example:
        | click element by name | name |
        """
        element = self._safe_find(by=By.NAME, value=name, timeout=timeout)
        self._safe_click(element, timeout=30)

    def click_element_by_xpath(self, xpath, timeout=30):
        """
        Click the element by its element xpath
        Example:
        | click element by xpath | //div[@class='hello'] |
        """
        element = self._safe_find(by=By.XPATH, value=xpath, timeout=timeout)
        self._safe_click(element, timeout=30)

    def double_click_element(self, locator, timeout=30):
        """
        Double Click the element by its element locator
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | double click element | id=kw |
        """
        (prefix, criteria) = self._parse_locator(locator)
        element = self._safe_find(by=prefix, value=criteria, timeout=timeout)
        ActionChains(self._get_current_browser()).double_click(element).perform()

    def double_click_element_by_id(self, id_, timeout=30):
        """
        Double Click the element by its element id
        Example:
        | double click element by id | kw |
        """
        element = self._safe_find(by=By.ID, value=id_, timeout=timeout)
        ActionChains(self._get_current_browser()).double_click(element).perform()

    def double_click_element_by_name(self, name, timeout=30):
        """
        Double Click the element by its element name
        Example:
        | double click element by name | kw |
        """
        element = self._safe_find(by=By.NAME, value=name, timeout=timeout)
        ActionChains(self._get_current_browser()).double_click(element).perform()

    def double_click_element_by_xpath(self, xpath, timeout=30):
        """
        Double Click the element by its element xpath
        Example:
        | double click element by xpath | //div[@id='kw'] |
        """
        element = self._safe_find(by=By.XPATH, value=xpath, timeout=timeout)
        ActionChains(self._get_current_browser()).double_click(element).perform()

    def click_element_at_coordinates(self, locator, xoffset=0, yoffset=0, timeout=30):
        """
        Click the element by horizontal offset and vertical offset by its element locator
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | click element at coordinates | id = kw | 50 | 80 |
        """
        (prefix, criteria) = self._parse_locator(locator)
        element = self._safe_find(by=prefix, value=criteria, timeout=timeout)
        ActionChains(self._get_current_browser()).move_to_element(element).\
            move_by_offset(xoffset, yoffset).click().perform()

    def click_element_at_coordinates_by_id(self, id_, xoffset=0, yoffset=0, timeout=30):
        """
        Click the element by horizontal offset and vertical offset by its element id
        Example:
        | click element at coordinates by id | kw | 50 | 80 |
        """
        element = self._safe_find(by=By.ID, value=id_, timeout=timeout)
        ActionChains(self._get_current_browser()).move_to_element(element). \
            move_by_offset(xoffset, yoffset).click().perform()

    def click_element_at_coordinates_by_name(self, name, xoffset=0, yoffset=0, timeout=30):
        """
        Click the element by horizontal offset and vertical offset by its element name
        Example:
        | click element at coordinates by name | kwname | 50 | 80 |
        """
        element = self._safe_find(by=By.NAME, value=name, timeout=timeout)
        ActionChains(self._get_current_browser()).move_to_element(element). \
            move_by_offset(xoffset, yoffset).click().perform()

    def click_element_at_coordinates_by_xpath(self, xpath, xoffset=0, yoffset=0, timeout=30):
        """
        Click the element by horizontal offset and vertical offset by its element xpath
        Example:
        | click element at coordinates by xpath | //div[@class='hello'] | 50 | 80 |
        """
        element = self._safe_find(by=By.XPATH, value=xpath, timeout=timeout)
        ActionChains(self._get_current_browser()).move_to_element(element). \
            move_by_offset(xoffset, yoffset).click().perform()

    def drag_and_drop(self, source_locator, target_locator, timeout=30):
        """
        Drag and drop the element from source element to target element
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | drag and drop | id=kw | name=ki |
        | drag and drop | xpath=//div[@class='hello'] | name=ki |
        """
        src_elem = self.find_element(source_locator, timeout=timeout)
        trg_elem = self.find_element(target_locator, timeout=timeout)
        ActionChains(self._get_current_browser()).drag_and_drop(src_elem, trg_elem).perform()

    def drag_and_drop_with_offset(self, locator, xoffset=0, yoffset=0, timeout=30):
        """
        Drag and drop the element within current element by locator by some offset
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | drag and drop by offset | id = kw | 30 | 60 | 10s |
        """
        (prefix, criteria) = self._parse_locator(locator)
        element = self._safe_find(by=prefix, value=criteria, timeout=timeout)
        ActionChains(self._get_current_browser()).drag_and_drop_by_offset(element, xoffset, yoffset).perform()

    def mouse_down(self, locator, timeout=30):
        """press mouse down on element by locator
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | mouse down | id | kw |
        """
        (prefix, criteria) = self._parse_locator(locator)
        element = self._safe_find(by=prefix, value=criteria, timeout=timeout)
        if element is None:
            raise AssertionError("ERROR: Element %s not found." % (prefix, criteria).__str__())
        ActionChains(self._get_current_browser()).click_and_hold(element).perform()

    def mouse_down_by_id(self, id_, timeout=30):
        """press mouse down on element by id
        Example:
        | mouse down by id | kw |
        """
        locator = 'id=' + id_
        self.mouse_down(locator, timeout=timeout)

    def mouse_down_by_name(self, name, timeout=30):
        """press mouse down on element by name
        Example:
        | mouse down by name | kw |
        """
        locator = 'name=' + name
        self.mouse_down(locator, timeout=timeout)

    def mouse_down_by_xpath(self, xpath, timeout=30):
        """press mouse down on element by xpath
        Example:
        | mouse down by xpath | //div[@class='hello'] |
        """
        locator = 'xpath=' + xpath
        self.mouse_down(locator, timeout=timeout)

    def set_value(self, locator, key=None, timeout=30, enter=False):
        """set value on a certain element by its locator
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | set value | id = kw | False |
        """
        if key.startswith('\\') and len(key) > 1:
            key = System.map_ascii_key_code_to_key(int(key[1:]))
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(key)
        if enter in [True, "true", "True", "TRUE"]:
            element.send_keys(Keys.ENTER)

    def set_value_by_id(self, id_, key=None, timeout=30, enter=False):
        """set value on a certain element by id
        Example:
        | set value by id | kw |
        """
        locator = "id=" + id_
        self.set_value(locator, key=key, timeout=timeout, enter=enter)

    def set_value_by_name(self, name, key=None, timeout=30, enter=False):
        """set value on a certain element by name
        Example:
        | set value by name | kw |
        """
        locator = "name=" + name
        self.set_value(locator, key=key, timeout=timeout, enter=enter)

    def set_value_by_xpath(self, xpath, key=None, timeout=30, enter=False):
        """set value on a certain element by xpath
        Example:
        | set value by xpath | //div[@class='hello'] |
        """
        locator = "xpath=" + xpath
        self.set_value(locator, key=key, timeout=timeout, enter=enter)

    def is_element_enabled(self, locator, timeout=30):
        """return if the element is enabled
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | ${enabled}=|is element enabled | id = kw |
        """
        element = self.find_element(locator, timeout)
        if not element.is_enabled():
            return False
        read_only = element.get_attribute('readonly')
        if read_only == 'readonly' or read_only == 'true':
            return False
        return True

    def is_element_enabled_by_id(self, id_, timeout=30):
        """return if the element is enabled by id
        Example:
        | ${enabled}=|is element enabled by id | kw |
        """
        locator = "id=" + id_
        return self.is_element_enabled(locator, timeout=timeout)

    def is_element_enabled_by_name(self, name, timeout=30):
        """return if the element is enabled by name
        Example:
        | ${enabled}=|is element enabled by name | kw |
        """
        locator = "name=" + name
        return self.is_element_enabled(locator, timeout=timeout)

    def is_element_enabled_by_xpath(self, xpath, timeout=30):
        """return if the element is enabled by xpath
        Example:
        | ${enabled}=|is element enabled by xpath | //div[text='hello'] |
        """
        locator = "xpath=" + xpath
        return self.is_element_enabled(locator, timeout=timeout)

    def is_element_visible(self, locator, timeout=30):
        """return if the element is visible by locator
        If you don't understand what present differ from visible, please use visible instead.
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | ${enabled}=|is element visible | id = kw |
        """
        element = self.find_element(locator, timeout=timeout)
        if element is not None:
            return element.is_displayed()
        return False

    def is_element_visible_by_id(self, id_, timeout=30):
        """return if the element is visible by id
        If you don't understand what present differ from visible, please use visible instead.
        Example:
        | ${enabled}=|is element visible by id | kw |
        """
        locator = "id=" + id_
        return self.is_element_visible(locator, timeout=timeout)

    def is_element_visible_by_name(self, name, timeout=30):
        """return if the element is visible by name
        If you don't understand what present differ from visible, please use visible instead.
        Example:
        | ${enabled}=|is element visible by name | kw |
        """
        locator = "name=" + name
        return self.is_element_visible(locator, timeout=timeout)

    def is_element_visible_by_xpath(self, xpath, timeout=30):
        """return if the element is visible by xpath
        If you don't understand what present differ from visible, please use visible instead.
        Example:
        | ${enabled}=|is element visible by xpath | //div[@class='hello'] |
        """
        locator = "xpath=" + xpath
        return self.is_element_visible(locator, timeout=timeout)

    def is_element_present(self, locator, timeout=30):
        """return if the element is present by locator
        If you don't understand what present differ from visible, please use visible instead.
        The possible locator could be
        id, xpath, link text, partial link text, name, tag name, class name, css selector
        Example:
        | ${enabled}=|is element present | name=kw |
        """
        return self.find_element(locator, timeout) is not None

    def is_element_present_by_id(self, id_, timeout=30):
        """return if the element is present by id
        If you don't understand what present differ from visible, please use visible instead.
        Example:
        | ${enabled}=|is element present by id | kw |
        """
        locator = "id=" + id_
        return self.is_element_present(locator, timeout=timeout)

    def is_element_present_by_name(self, name, timeout=30):
        """return if the element is present by name
        If you don't understand what present differ from visible, please use visible instead.
        Example:
        | ${enabled}=|is element present by name | kw |
        """
        locator = "name=" + name
        return self.is_element_present(locator, timeout=timeout)

    def is_element_present_by_xpath(self, xpath, timeout=30):
        """return if the element is present by xpath
        If you don't understand what present differ from visible, please use visible instead.
        Example:
        | ${enabled}=|is element present by xpath | //div[@class='hello'] |
        """
        locator = "xpath=" + xpath
        return self.is_element_present(locator, timeout=timeout)

    def _get_text_by_id(self, id_, timeout=30):
        locator = "id=" + id_
        return self._get_text(locator, timeout=timeout)

    def _get_text_by_name(self, name, timeout=30):
        locator = "name=" + name
        return self._get_text(locator, timeout=timeout)

    def _get_text_by_xpath(self, xpath, timeout=30):
        locator = "xpath=" + xpath
        return self._get_text(locator, timeout=timeout)

    def _get_text(self, locator, timeout=30):
        element = self.find_element(locator, timeout)
        return element.text if element is not None else None

    def _get_value_by_id(self, id_, timeout=30):
        locator = "id=" + id_
        return self._get_value(locator, timeout=timeout)

    def _get_value_by_name(self, name, timeout=30):
        locator = "name=" + name
        return self._get_value(locator, timeout=timeout)

    def _get_value_by_xpath(self, xpath, timeout=30):
        locator = "path=" + xpath
        return self._get_value(locator, timeout=timeout)

    def _get_value(self, locator, timeout=30):
        element = self.find_element(locator, timeout)
        return element.get_attribute('value') if element is not None else None

    def _get_current_browser(self):
        return self._current_browser()

    def _parse_locator(self, locator):
        prefix = None
        criteria = locator
        if not locator.startswith('//'):
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0:
                prefix = locator_parts[0]
                criteria = locator_parts[2].strip()
        return prefix, criteria

    def _safe_click(self, element, timeout=30):
        start = int(round(time.time() * 1000))
        while timeout * 1000 > int(round(time.time() * 1000)) - start:
            try:
                if element.is_enabled():
                    element.click()
                    return
            except:
                pass
        raise RuntimeError("Could not click element %s within %s millisecond." %
                           (element.__str__(), int(round(time.time() * 1000)) - start)
                           )

    def _safe_find(self, by, value, timeout=30):
        start = int(round(time.time() * 1000))
        while timeout * 1000 > int(round(time.time() * 1000)) - start:
            try:
                _driver = self._get_current_browser()
                _driver.implicitly_wait(1)
                element_list = _driver.find_elements(by, value)
                for element in element_list:
                    if element.is_displayed():
                        _driver.implicitly_wait(self.__default_implicit_wait_in_secs)
                        # print "debug time taken for safe_find is %s millisecond for element %s" % (
                        # int(round(time.time() * 1000)) - start, (by, value).__str__())
                        return element
            except:
                pass
            finally:
                _driver.implicitly_wait(self.__default_implicit_wait_in_secs)
                # print "debug time taken for safe_find is %s millisecond" % (int(round(time.time() * 1000)) - start)
        raise RuntimeError("Could not find element %s within %s millisecond." %
                           ((by, value).__str__(), int(round(time.time() * 1000)) - start)
                           )

    def _safe_finds(self, by, value, timeout=30):
        start = int(round(time.time() * 1000))
        _driver = self._get_current_browser()
        while timeout * 1000 > int(round(time.time() * 1000)) - start:
            try:
                try:
                    _driver.implicitly_wait(5)
                    WebDriverWait(_driver, 1, poll_frequency=0.1)\
                        .until(ec.visibility_of_any_elements_located(locator=(by, value)))
                except:
                    pass
                return _driver.find_elements(by, value)
            except:
                pass
            finally:
                _driver.implicitly_wait(self.__default_implicit_wait_in_secs)
        raise RuntimeError("Could not find element %s within %s millisecond." %
                           ((by, value).__str__(), int(round(time.time() * 1000)) - start)
                           )
