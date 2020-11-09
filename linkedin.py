from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


#Kendi webdriver yolumuzu gösteriyoruz.
browser = webdriver.Chrome("/Users/Emin Can Kurt/Desktop/chromedriver")
browser.get("https://www.linkedin.com/")

browser.maximize_window()

email = browser.find_element_by_xpath("//*[@id='session_key']")
password = browser.find_element_by_xpath("//*[@id='session_password']")
#Linkedin sayfamıza girebilmek için kendi email ve şifemizi giriyoruz.
email.send_keys("")
password.send_keys("")

login_buton =browser.find_element_by_css_selector("body > main > section.section.section--hero > div.sign-in-form-container > form > button")
login_buton.click()

time.sleep(5)
# Bir search işlemi yapmak istersek yorum satırından çıkartınız.Bu kısım ana sayfamızdan istediğimizi aramamızı sağlıyor.
# search_bar=browser.find_element_by_xpath("//*[@id='ember16']/input")
#Aramak istediğimiz kısmı buraya yazıyoruz
# search_bar.send_keys("")
# search_bar.send_keys(Keys.RETURN)
# time.sleep(3)


contacts = browser.find_element_by_xpath("//*[@id='ember23']")
contacts.click()
time.sleep(5)


contacts_button = browser.find_element_by_class_name("mn-community-summary__entity-info")
contacts_button.click()
time.sleep(5)

#burdaki kod sitemızı asagı kaymasısını saglayan scroll harektı ıcın yazılan bir script
for i in range(1,3):
   browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
   time.sleep(3)
#kullanıcılarımızı followers değişkenine atadık   
followers=browser.find_elements_by_class_name("mn-connection-card__details")   
#bunları bir listeye atamamız lazım ama bir dongu ıcınde yapalım ki hepsine ulaşalım
followerList=[]
for follower in followers:
    followerList.append(follower.text)

with open ("follwers.txt","w",encoding="UTF-8") as file:
    for follower in followerList :
        file.write(follower + "\n")
time.sleep(5)        

browser.quit()