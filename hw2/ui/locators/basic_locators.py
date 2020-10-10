from selenium.webdriver.common.by import By


class LoginPageLocators:
    SIGNBUTTON = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    EMAILFIELD = (By.NAME, 'email')
    PASSWDFIELD = (By.NAME, 'password')
    AUTHBUTTON = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')
    LOGINSHOW = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div[1]')

class MainPageLocators:
    STARTCREATE = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')


class CreatingCampaignLocators:
    TYPE = (By.XPATH, '//div[@cid="view567"]')
    INPUTURL = (By.XPATH, '//input[@data-gtm-id="ad_url_text"]')
    BANNER = (By.XPATH, '//div[@id="patterns_4"]')
    BANNER_URL = (By.XPATH, '//input[@placeholder="Введите адрес ссылки"]')
    LOADIMAGE = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[6]/div/div[4]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/input')
    CLEAR = (By.CLASS_NAME, 'input__clear')
    SAVEADV = (By.XPATH,'//div[contains(text(), "Сохранить объявление")]')
    NAMEINPUT = (By.CLASS_NAME, 'input__inp')
    CREATECAMPAIGN= (By.XPATH, "//div[contains(text(), 'Создать кампанию')]")