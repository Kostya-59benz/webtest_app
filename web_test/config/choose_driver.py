
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options  as EdgeOptions



def browser_selector(selected_options):
    return BrowserSelector(selected_options)




class BrowserSelector:
    def __init__(self, browsers):
        self.browsers = browsers

    @staticmethod
    def get_common_options(browser):
        options = None
        if browser == "Chrome":
            options = ChromeOptions()
        elif browser == "Firefox":
            options = FirefoxOptions()
        elif browser == "Edge":
            options = EdgeOptions()
        else:
            raise ValueError("Unsupported browser type")
        
        options.add_argument("--headless")
        options.add_argument("--no-sandbox") 
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        return options

    def get_browsers(self):
        return [
            {"name": browser, "options": self.get_common_options(browser)}
            for browser in self.browsers
        ]