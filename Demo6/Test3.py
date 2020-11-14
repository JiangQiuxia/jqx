from threading import Thread
from time import ctime,sleep

from selenium import webdriver

def test_Baidu(browser,search):

    print("start:%s" %ctime())
    print("Browser:%s" %browser)
    # if browser == "ie":
    #     driver = webdriver.Ie()
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "ff":
        driver = webdriver.Firefox()
    else:
        print("browser参数有误，只能为ie,chrome,firefox")

    driver.get('http://www.baidu.com')
    driver.find_element_by_id("kw").send_keys(search)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()

if __name__ == '__main__':
    lists = {"chrome":"threading","ff":"webdirver"}
    threads = []
    files = range(len(lists))

    for browser,search in lists.items():
        t = Thread(target=test_Baidu,args=(browser,search))
        threads.append(t)

    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()

print("ending:%s" %ctime())

