# 本程式檔總計2個檔案，目標為把所學的python技巧練得更熟，進行資料整理，以供後續收運路線整併使用。
# 以公司車管系統資料庫做練習標的，程式檔執行步驟為，上網將本年度車輛收運資料全部爬蟲下載下來，再將下載下來的資料做整理。
# 整理成預備套用於google map 上的 excel，可直接匯入成為收運點標籤內容。

# 先匯入相關套件，selenium、shutil，time為內建套件，無須下載，前2者若無下載皆須先行下載(pip install [selenium、shutil])
# 另須先行下載 chromedriver，置於檔案夾內使用。
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import shutil

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome(r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\chromedriver",chrome_options=options)
chrome.get("https://route.tyemid.gov.tw/lagi/")

personid = chrome.find_element_by_id("personid")
password = chrome.find_element_by_id("personpw")

personid.send_keys("*****yih***")
password.send_keys("****86***")
password.submit()
time.sleep(3)

chrome.get("https://route.tyemid.gov.tw/lagi/multi/page#")

menu_1 = chrome.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/ul/li[6]/a/b")
hidden_1 = chrome.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/ul/li[6]/ul/li[6]/a")
action_1 = ActionChains(chrome).move_to_element(menu_1).click(hidden_1).perform()
time.sleep(3)

button_1_1 = chrome.find_element_by_name("month").click()
button_1_2 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/select/option[1]").click()
button_1_3 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/input").click()
time.sleep(10)

button_2_1 = chrome.find_element_by_name("month").click()
button_2_2 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/select/option[2]").click()
button_2_3 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/input").click()
time.sleep(10)

button_3_1 = chrome.find_element_by_name("month").click()
button_3_2 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/select/option[3]").click()
button_3_3 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/input").click()
time.sleep(10)

button_4_1 = chrome.find_element_by_name("month").click()
button_4_2 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/select/option[4]").click()
button_4_3 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/input").click()
time.sleep(10)

button_5_1 = chrome.find_element_by_name("month").click()
button_5_2 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/select/option[5]").click()
button_5_3 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/input").click()
time.sleep(10)

button_6_1 = chrome.find_element_by_name("month").click()
button_6_2 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/select/option[6]").click()
button_6_3 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/input").click()
time.sleep(10)

button_7_1 = chrome.find_element_by_name("month").click()
button_7_2 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/select/option[7]").click()
button_7_3 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/input").click()
time.sleep(10)

button_8_1 = chrome.find_element_by_name("month").click()
button_8_2 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/select/option[8]").click()
button_8_3 = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/form[2]/div/table/tbody/tr[2]/td/input").click()
time.sleep(10)


shutil.move(r"C:\Users\莊馥羽\Downloads\lagi2-003.xls",r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data")
shutil.move(r"C:\Users\莊馥羽\Downloads\lagi2-003 (1).xls",r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data")
shutil.move(r"C:\Users\莊馥羽\Downloads\lagi2-003 (2).xls",r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data")
shutil.move(r"C:\Users\莊馥羽\Downloads\lagi2-003 (3).xls",r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data")
shutil.move(r"C:\Users\莊馥羽\Downloads\lagi2-003 (4).xls",r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data")
shutil.move(r"C:\Users\莊馥羽\Downloads\lagi2-003 (5).xls",r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data")
shutil.move(r"C:\Users\莊馥羽\Downloads\lagi2-003 (6).xls",r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data")
shutil.move(r"C:\Users\莊馥羽\Downloads\lagi2-003 (7).xls",r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data")



