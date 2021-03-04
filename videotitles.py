import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException

def get_image_title(url):
    driver_path="C:/Users/soyeon/Desktop/chromedriver"
    driver=webdriver.Chrome(driver_path)
    driver.implicitly_wait(5)
    
    driver.get(url)
    title_list=list()
    image_list = list()
    
    idx=1
    while True:
        try:
            img_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer['+str(idx)+']/div[1]/ytd-thumbnail/a/yt-img-shadow/img'
            title_xpath='/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer['+str(idx)+']/div[1]/div[1]/div[1]/h3/a'
            img = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, img_xpath))) 
            if img is None: 
                print(idx, 'img is not loaded.') 
            
            if idx%8 == 0:
                driver.execute_script('window.scrollBy(0,1080);')
                time.sleep(1)
                driver.execute_script('window.scrollBy(0,1080);')
                time.sleep(1)
                driver.execute_script('window.scrollBy(0,1080);')
                time.sleep(1)
                
            title=driver.find_element_by_xpath(title_xpath)
            print(idx,title.text)
            title_list.append(title.text)
            
            image = driver.find_element_by_xpath(img_xpath)
            img_url = image.get_attribute('src')
            image_list.append(img_url)
            
            idx +=1
            
        except Exception as e:
            print()
            print(e)
            break
            
        except NoSuchElementException:
            #continue
            title_list.append(None)
        
    assert len(image_list) == len(title_list)
    driver.close()
    return image_list, title_list

url='https://www.youtube.com/channel/UCZVD--cl8FLRn7kmSudAuBA/videos'
image1, title1=get_title(url)

import csv
import os
os.chdir('C:/Users/soyeon/Desktop')
with open("result5.csv","w",newline="") as f:
    writer=csv.writer(f,delimiter=" ", quotechar=',')
    writer.writerows(title)
