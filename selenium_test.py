from selenium import webdriver
import os
import time
import pickle


URL = 'http://diamondexch.com/game-detail/30337491'



options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')
options.add_argument('accept=accept: ')
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument("user-data-dir=chrome_data\\")
# options.add_argument(r"user-data-dir=C:\Users\Workspace\AppData\Local\Google\Chrome\User Data")
# options.add_argument("--profile-directory=Default")
# options.add_argument("--disable-extensions")
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(
    executable_path=os.path.join('chromedriver', 'chromedriver.exe'),
    options=options
)


# # Сохранение куки
# def save_cookie(driver, path='/tmp/cookie'):
#     with open(path, 'wb') as filehandler:
#         pickle.dump(driver.get_cookies(), filehandler)
#
#
# # Чтение куки
# def load_cookie(driver, path='/tmp/cookie'):
#     with open(path, 'rb') as cookiesfile:
#         cookies = pickle.load(cookiesfile)
#         for cookie in cookies:
#             driver.add_cookie(cookie)
#
#
# # Получение ссылок на страницу
# def get_page_links(url, amount):
#     driver.get(url)
#     driver.implicitly_wait(10)
#     time.sleep(3)
#     links = []
#     for i in range(1, amount):
#         link = driver.find_element_by_xpath(f'//*[@id="content"]/div/div[3]/div/div[2]/div[{i}]/a').get_attribute(
#             'href')
#         links.append(link)
#     return links
#
#
# # Пагинация
# def pagination(url, amount):
#     pagination_urls = []
#     for i in range(1, amount):
#         new_url = url + f'{i}'
#         pagination_urls.append(new_url)
#     return pagination_urls
#
#
# # Получение всех ссылок
# def get_all_links():
#     pagination_list = pagination(URL_PAGINATION, 3)
#     links = []
#     for i in pagination_list:
#         link_list = get_page_links(i, 3)
#         for item in link_list:
#             links.append(item)
#     return links


try:
    driver.maximize_window()
    # driver.set_window_size(1980, 2000)
    driver.get(URL)
    driver.implicitly_wait(10)
    time.sleep(50)
    with open("page_source.html", "w", encoding='UTF-8') as f:
        f.write(driver.page_source)
    driver.save_screenshot('screenshot.png')
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
