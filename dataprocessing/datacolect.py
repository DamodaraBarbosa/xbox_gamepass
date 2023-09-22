from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from bs4 import BeautifulSoup

class Webdriver:
    # def __init__(self, url: str) -> None:
    #     self.url = url        
    
    def set_driver(self, directory: str=None, headless: bool=False):
        """
        Set the webdriver that will be used in scraping.
        
        headless: set the configs options to use it on Gooble colab, default= False.
        """
        if headless == True:
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument(
                '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
            )
            # prefs = {'download.default_directory': directory}
            # options.add_experimental_option('prefs', prefs)
            return webdriver.Chrome(chrome_options=options)
        else:
            # options = webdriver.ChromeOptions()
            # prefs = {'download.default_directory': directory}
            # options.add_experimental_option('prefs', prefs)
            return webdriver.Chrome()

class Soup:
    def __init__(self, url) -> None:
        self.url = url
    
    def get_soup(self):
        response = requests.get(self.url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        return soup


class Scrape:
    """
    Class with methods to scrape the website.
    """
    def __init__(self, webdriver=None) -> None:
        """
        The attributes:
        
        webdriver: the selected webdriver that is selected to work.
        """
        self.webdriver = webdriver

    def click(self, path: str, how: By=By.XPATH , timeout: int=3):
        """
        Method to click in page's elements. 
        
        path: class name, tag name or XPATH;
        how: set how locate the element in page (CLASS_NAME, TAG_NAME, CSS_SELECTOR or XPATH),
        default = By.XPATH;
        timeout: set the time until execute the method, default= 3.
        """
        button = WebDriverWait(self.webdriver, timeout).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        button.click()

    def insert_info(self, info: str, path: str, how: By=By.XPATH, timeout: int=3):
        """
        info: the information that is wanted to insert.
        path: class name, tag name or XPATH;
        how: set how locate the element in page (CLASS_NAME, TAG_NAME, CSS_SELECTOR or XPATH),
        default = By.XPATH;
        timeout: set the time (seconds) until execute the method, default= 3.
        """
        search = WebDriverWait(self.webdriver, timeout).until(
            EC.presence_of_element_located((how, path))
        )
        search.send_keys(info) # insert info.
        search.send_keys(Keys.ENTER) # ENTER to set the info in search bar.

    def find_element(self, soup, tag: str, tag_class=None, timeout: int=0):
        sleep(timeout)
        
        try:
            data = soup.find(tag, {'class': tag_class})
        except (AttributeError, TimeoutException, StaleElementReferenceException) as e:
            data = None
        
        return data
    
    def find_elements(self, soup, tag: str, tag_class=None, timeout: int=0):
        sleep(timeout)

        try:
            datas = soup.find_all(tag, {'class': tag_class})
        except (AttributeError, TimeoutException, StaleElementReferenceException) as e:
            datas = None
        
        return datas

    def get_element(self, path: str, how: By=By.XPATH, timeout: int=3):
        """
        Return the element in the path.
        
        path: class name, tag name or XPATH;
        how: set how locate the element in page (CLASS_NAME, TAG_NAME, CSS_SELECTOR or XPATH),
        default = By.XPATH;
        timeout: set the time (seconds) until execute the method, default = 3.
        """
        element = WebDriverWait(self.webdriver, timeout).until(
            EC.presence_of_element_located((how, path))
        )
        return element.find_element(how, path)
    
    def get_elements(self, path: str, how: By=By.XPATH, timeout: int=3):
        """
        Returns an array with all elements in the path.
        
        path: class name, tag name or XPATH;
        how: set how locate the element in page (CLASS_NAME, TAG_NAME, CSS_SELECTOR or XPATH),
        default = By.XPATH;
        timeout: set the time (seconds) until execute the method, default= 3.
        """
        elements = WebDriverWait(self.webdriver, timeout).until(
            EC.presence_of_element_located((how, path))
        )
        return elements.find_elements(how, path)

    def elements_text(self, elements: list):
        """
        Shows texts obtained from elements of BeautifulSoup's selenium.webdriver or soup objects.
        
        elements: element list selenium.webdriver or BeautifulSoup objects.
        """
        try:
            for index, element in enumerate(elements):
                if isinstance(element, WebElement):
                    print(f'{index}: {element.text}')
                else:
                    print(f'{index}: {element.get_text()}')
        except:
            raise 'The passed elements do not contain texts.'
    
    def switch_tab(self, tab: int, timeout: int=5):
        """
        Switch tabs openened in the browser.
        
        tab: selects the tab to which it should be switched.
        timeout: time sleep after switch tabs.
        """
        self.webdriver.switch_to.window(self.webdriver.window_handles[tab])
        sleep(timeout)
    
    def select_elements(self, elements: list, index: list):
        """
        Iterates the selenium webdriver objects to get the data.
        
        infos: list with selenium webdriver objects.
        """
        only_selected_elements = list()

        for element_index, element in enumerate(elements):
            if element_index in index:
                only_selected_elements.append(element)
            else:
                pass
            
        return only_selected_elements





    





