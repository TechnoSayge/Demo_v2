from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.google.com")
driver.find_element_by_name('q').send_keys('software testing tools')
driver.find_element_by_name('btnK').click()





















#Below are notes and lines that didn't work:

# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
#



#Below are notes and lines that didn't work:
#
# def setUp(self):
# 		self.driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
# 		self.URL = "Https://www.python.org"
# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get('http://google.com')
# from selenium.webdriver.firefox.options import Options
#
# opts = Options()
# opts.binary = '/Program Files/Mozilla Firefox/firefox.exe'
# opts.log.level = "trace"
#
# driver = webdriver.Firefox(options=opts)
#
# driver.get('http://www.google.com')


# binary = firefox_binary('/Program Files/Mozilla Firefox/firefox.exe')
# driver = webdriver.Firefox(firefox_binary=binary)
#driver = webdriver.Firefox()
# driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
#driver.get('http://www.twitter.com/')

# 'C:/Program Files/Mozilla Firefox/firefox.exe'

# driver = webdriver.Firefox(executable_path='/Users/yolanda/Documents/sandbox/Projects/geckdodriver.exe')
# driver.get('https://www.facebook.com/')
# driver.find_element_by_name('')

