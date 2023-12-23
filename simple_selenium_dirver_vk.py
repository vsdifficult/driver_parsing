from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

url = "https://vk.com/feed?w=wall-130936589_468156"
options = webdriver.FirefoxOptions()
options.add_argument('--enable-javascript')
#options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

def login():
    try:
        driver.get(url=url)

        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "index_email"))
        )
        email_input.clear()
        num = str(input("Введите свой номер >>>> "))
        email_input.send_keys(num)

        login_button = driver.find_element(By.CLASS_NAME, "FlatButtonin")
        login_button.click()

        code_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "vkcTextFieldinput"))
        )
        
        code = input("Введите код >>>> ")
        code_input.send_keys(code)
        try:
             comment_parse()
        except Exception as e: 
            return e
    except TimeoutException:
        print("Тайм-аут при ожидании появления элемента. Проверьте правильность идентификатора элемента или увеличьте время ожидания.")
    except NoSuchElementException as e:
        print(f"Элемент не найден: {e}")
    except Exception as e:
        print(f"Ошибка во время входа: {e}")

def comment_parse():
    try:
        text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".reply_content"))
        )
        print(text.text)
    except Exception as e:
        print(e)

def main():
    try:
        login()
       
        
    except Exception as e:
        print(f"Ошибка main: {e}")

    # finally:
    #     try:
    #         time.sleep(5)
    #         driver.close()
    #         driver.quit()
    #     except Exception as e:
    #         print(f"Ошибка при закрытии драйвера: {e}")

if __name__ == "main__":
    main()
