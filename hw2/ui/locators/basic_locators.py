from selenium.webdriver.common.by import By


class LoginPageLocators:
    SIGNBUTTON = (By.XPATH, '//div[contains(@class,"responseHead-module-button") and contains(text(),"Войти") ]')
    EMAILFIELD = (By.NAME, 'email')
    PASSWDFIELD = (By.NAME, 'password')
    AUTHBUTTON = (By.XPATH, '//div[contains(@class, "authForm-module-button") and contains(text(), "Войти") ]')
    LOGINSHOW = (By.XPATH, '//div[contains(text(),"condackow.aleck@yandex.ru")]')


class MainPageLocators:
    STARTCREATE = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')
    AUDIENCE = (By.XPATH, '//a[contains(text(), "Аудитории")]')


class CreatingCampaignLocators:
    TYPE = (By.XPATH, '//div[@cid="view567"]')
    INPUTURL = (By.XPATH, '//input[@data-gtm-id="ad_url_text"]')
    BANNER = (By.XPATH, '//div[@id="patterns_4"]')
    BANNER_URL = (By.XPATH, '//input[@placeholder="Введите адрес ссылки"]')
    LOADIMAGE = (By.XPATH, '//div[contains(@class,"upload-module-wrapper") and contains(@class,"upload-module-hidden")  ]/input')
    CLEAR = (By.CLASS_NAME, 'input__clear')
    SAVEADV = (By.XPATH, '//div[contains(text(), "Сохранить объявление")]')
    NAMEINPUT = (By.CLASS_NAME, 'input__inp')
    CREATECAMPAIGN= (By.XPATH, '//div[contains(text(), "Создать кампанию")]')


class NewSegmentLocators:
    STARTCREATE_01 = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    STARTCREATE_02 = (By.XPATH, '//div[contains(text(), "Создать сегмент")]')
    SEGMENT = (By.XPATH, '//div[contains(text(), "Приложения и игры в соцсетях")]')
    MAINCHECK = (By.XPATH, '//span[contains(text(), "Игравшие и платившие в платформе")]/parent::div/parent::div/parent::div/input')
    ADD = (By.XPATH, '//div[contains(text(), "Добавить сегмент")]')
    NAMEINPUT = (By.XPATH, '//input[@type="text" and @maxlength=60]')

    ACTIONS = (By.XPATH, '//span[contains(text(), "Действия")]')
    DELETE = (By.XPATH, '//li[@title = "Удалить"]')
