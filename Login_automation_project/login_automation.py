from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def login(username, password):
    driver = webdriver.Chrome(
        '/home/softnautics/Public/Murtaza/Login_automation_project/chromedriver')

    driver.get('https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page')
    
    driver.find_element_by_id('wpName1').send_keys(username)
    driver.find_element_by_id('wpPassword1').send_keys(password)
    driver.find_element_by_id('wpLoginAttempt').click()

    WebDriverWait(driver=driver, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))

    error_msg = 'Incorrect username or password entered. Please try again.'
    success_msg = 'Welcome to Wikipedia'
    errors = driver.find_elements_by_xpath("//*[@id='userloginForm']/form/div[1]")
    success = driver.find_elements_by_xpath("//*[@id='Welcome_to_Wikipedia']")



    if any(error_msg in e.text for e in errors):
        result = "Login failed"
    elif any(success_msg in s.text for s in success):
        result = 'Login successfull'
    else:
        result = "captcha occured"

    driver.close()

    return result

#if __name__ == "__main__":
#    file = "/home/softnautics/Desktop/Login_automation_project/login_page_testcases.xlsx"
#    data = Data_Extraction(file)