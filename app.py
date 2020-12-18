from flask import Flask
import flask
import selenium
import sys
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import zipfile
with zipfile.ZipFile('./bin/headless-chromium.zip', 'r') as zip_ref:
    zip_ref.extractall('./bin')




app = Flask(__name__)

@app.route("/")
def hello():
    get_page()
    return "Hello, World!" + ' ' + flask.__version__ + ' ' + selenium.__version__ + ' ' + sys.platform + ' ' + get_page()


def get_page():
    print("XXXXXXXX")
    print("HEADLESS", os.path.abspath('./bin/headless-chromium'))
    print("CHROMEDRIVER", os.path.abspath('./bin/chromedriver'))

    options = Options()
    options.binary_location = './bin/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path='./bin/chromedriver', chrome_options=options)

    driver.get('https://www.google.com/')
    source =  driver.page_source[:250]
    print(source)
    with open(r'./abc.txt', encoding='utf-8') as f:
        text = f.read()

    driver.close()
    driver.quit()

    return text


if __name__ == '__main__':
    print('a')



    app.run('127.0.0.1', 5000)