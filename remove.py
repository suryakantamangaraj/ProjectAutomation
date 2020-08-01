import sys
import os
from github import Github
from selenium import webdriver
import time
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

username = str(sys.argv[1])
password = str(sys.argv[2])
reponame = str(sys.argv[3])

#binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
#browser = webdriver.Firefox(firefox_binary=binary)
browser = webdriver.Firefox(executable_path="C:\\Users\\manga\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\geckodriver.exe",log_path=None)
browser.get('https://github.com/login')
time.sleep(2)

def remove():
    browser.find_elements_by_xpath("//input[@name='login']")[0].send_keys(username)
    time.sleep(5)
    browser.find_elements_by_xpath("//input[@name='password']")[0].send_keys(password)
    time.sleep(10)
    browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
    time.sleep(10)
    browser.get('https://github.com/' + username + '/' + reponame + '/settings')
    time.sleep(5)
    browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0].click()
    time.sleep(5)
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0].send_keys(username + '/' + reponame)
    time.sleep(10)
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()
    time.sleep(3)
    browser.get("https://github.com/" + username + "?tab=repositories")


if __name__ == "__main__":
    remove()
