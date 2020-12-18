from flask import Flask
import flask
import selenium
import sys

from selenium import webdriver
app = Flask(__name__)

@app.route("/")
def hello():
    get_page()
    return "Hello, World!" + ' ' + flask.__version__ + ' ' + selenium.__version__ + ' ' + sys.platform + ' ' + get_page()


'''
def get_page():
    options = webdriver.FirefoxOptions()
    options.headless = True
    # options.add_argument('headless')
    # driver = webdriver.Chrome(options=options)

    browser = webdriver.Firefox(executable_path=r'./geckodriver32', options=options)
    browser.get('https://gamefaqs.gamespot.com/')
    source = browser.page_source
    print(source[:200])
    login_link = browser.find_element_by_link_text('Log In')
    login_link.click()
    print()
    print(browser.page_source[:200])
    with open(r'./abc.txt', encoding='utf-8') as f:
        text = f.read()
    return text
'''

def get_page():
    options = webdriver.ChromeOptions()
    options.headless = True
    # options.add_argument('headless')
    # driver = webdriver.Chrome(options=options)

    browser = webdriver.Chrome(executable_path=r'./chromedriver64', options=options)
    browser.get('https://gamefaqs.gamespot.com/')
    source = browser.page_source
    print(source[:200])
    login_link = browser.find_element_by_link_text('Log In')
    login_link.click()
    print()
    print(browser.page_source[:200])
    with open(r'./abc.txt', encoding='utf-8') as f:
        text = f.read()
    return text


if __name__ == '__main__':
    print('a')



    app.run('127.0.0.1', 5000)