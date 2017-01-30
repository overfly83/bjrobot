import os
import robot
import robot.utils
from BJRobot.utilities.system import System
from keywordgroup import KeywordGroup


class Screenshot(KeywordGroup):

    def __init__(self):
        self._screenshot_index = {}
        self._screenshot_path_stack = []
        self.screenshot_root_directory = None

    # Public

    def capture_page_screenshot(self, filename='selenium-screenshot-{index}.png'):
        """Takes a screenshot of the current page and embeds it into the log.

        ``filename`` argument specifies the name of the file to write the
        screenshot into. If no ``filename`` is given, the screenshot is saved
        into file _selenium-screenshot-{index}.png_ under the directory where
        the Robot Framework log file is written into. The ``filename`` is
        also considered relative to the same directory, if it is not
        given in absolute format. If an absolute or relative path is given
        but the path does not exist it will be created.

        Example 1:
        | ${file1} = | Capture Page Screenshot |
        | File Should Exist | ${OUTPUTDIR}${/}selenium-screenshot-1.png |
        | Should Be Equal | ${file1} | ${OUTPUTDIR}${/}selenium-screenshot-1.png |
        | ${file2} = | Capture Page Screenshot |
        | File Should Exist | ${OUTPUTDIR}${/}selenium-screenshot-2.png |
        | Should Be Equal | ${file2} | ${OUTPUTDIR}${/}selenium-screenshot-2.png |

        Example 2:
        | ${file1} = | Capture Page Screenshot | ${OTHER_DIR}${/}other-{index}-name.png |
        | ${file2} = | Capture Page Screenshot | ${OTHER_DIR}${/}some-other-name-{index}.png |
        | ${file3} = | Capture Page Screenshot | ${OTHER_DIR}${/}other-{index}-name.png |
        | File Should Exist | ${OTHER_DIR}${/}other-1-name.png |
        | Should Be Equal | ${file1} | ${OTHER_DIR}${/}other-1-name.png |
        | File Should Exist | ${OTHER_DIR}${/}some-other-name-1.png |
        | Should Be Equal | ${file2} | ${OTHER_DIR}${/}some-other-name-1.png |
        | File Should Exist | ${OTHER_DIR}${/}other-2-name.png |
        | Should Be Equal | ${file3} | ${OTHER_DIR}${/}other-2-name.png |

        Example 3:
        | Capture Page Screenshot | ${OTHER_DIR}${/}sc-{index:06}.png |
        | File Should Exist | ${OTHER_DIR}${/}sc-000001.png |
        """
        path, link = self._get_screenshot_paths(filename)
        System.create_directory(path)
        if hasattr(self._current_browser(), 'get_screenshot_as_file'):
            if not self._current_browser().get_screenshot_as_file(path):
                raise RuntimeError('Failed to save screenshot ' + link)
        else:
            if not self._current_browser().save_screenshot(path):
                raise RuntimeError('Failed to save screenshot ' + link)
        # Image is shown on its own row and thus prev row is closed on purpose
        self._html('</td></tr><tr><td colspan="3"><a href="%s">'
                   '<img src="%s" width="800px"></a>' % (link, link))
        return path

    # Private

    def _get_screenshot_directory(self):

        # Use screenshot root directory if set
        if self.screenshot_root_directory is not None:
            return self.screenshot_root_directory

        # Otherwise use RF's log directory
        return self._get_log_dir()

    # should only be called by set_screenshot_directory
    def _restore_screenshot_directory(self):
        self.screenshot_root_directory = self._screenshot_path_stack.pop()

    def _get_screenshot_paths(self, filename):
        filename = filename.format(
            index=self._get_screenshot_index(filename))
        filename = filename.replace('/', os.sep)
        screenshotdir = self._get_screenshot_directory()
        logdir = self._get_log_dir()
        path = os.path.join(screenshotdir, filename)
        link = robot.utils.get_link_path(path, logdir)
        return path, link

    def _get_screenshot_index(self, filename):
        if filename not in self._screenshot_index:
            self._screenshot_index[filename] = 0
        self._screenshot_index[filename] += 1
        return self._screenshot_index[filename]
