from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-extensions')
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

driver.get('https://www.google.com/search?sxsrf=ALeKk028EJFf9OJj2KQllKYhw09PlBMh3A%3A1612207187353&ei=U1QYYLX3FLar5NoP2Oyj4AY&q=site%3Awww.facebook.com+%22Page+created+-+January+6%2C+2020%22+%22LLC%22+&oq=site%3Awww.facebook.com+%22Page+created+-+January+6%2C+2020%22+%22LLC%22+&gs_lcp=CgZwc3ktYWIQA1CKcFiKcGCKcmgAcAB4AIABQYgBgQGSAQEymAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwj17NLls8nuAhW2FVkFHVj2CGwQ4dUDCA0&uact=5')

# Search Result 
search_result = driver.find_elements_by_class_name("LC20lb")
for e in search_result:
    print(e.text)

search_link = driver.find_elements_by_css_selector('div.g')
for e in search_link:
    links = (e.find_element_by_tag_name("a").get_attribute("href"))
    print(links)

# Search Result Info
# Phone Number
company_num = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div")
print(search_result.text)