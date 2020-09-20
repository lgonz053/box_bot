import os
import time

from selenium import webdriver

DRIVER_ROOT = os.path.abspath(os.path.join(__file__, "../chromedriver/chromedriver"))

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--headless")
options.add_experimental_option("detach", True)

def main():
  #open browser
  browser = webdriver.Chrome(DRIVER_ROOT)
  browser.get("https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161")
  browser.set_window_size(1600, 1000)

  #login
  login_steps = {
      "acct_btn": "/html/body/div[3]/div/div/header/div[2]/div[2]/div/nav[2]/ul/li[1]/button",
      "sign_btn": "/html/body/div[3]/div/div/header/div[2]/div[2]/div/nav[2]/ul/li[1]/div/div/div/div/div[2]/div/div/a/button",
      "email": "/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[1]/div/input",
      "pw": "/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[2]/div/input"
  }

  for step, path in login_steps.items():
      if step in ["email", "pw"]:
          # push email and pw for login attempt
          input = browser.find_element_by_xpath(path)
          input.send_keys(os.environ[step])
          time.sleep(2)
          if step == "pw":
              # hit login btn
              browser.find_element_by_xpath("/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[4]/button").click()

      print(step)
      browser.find_element_by_xpath(path).click()
      time.sleep(1)

  searching = True

  while searching:
      try:
          # look pre-order btn
          print("looking for pre-order btn")
          preorder_btn = browser.find_element_by_xpath("/html/body/div[4]/main/div[1]/div[3]/div[2]/div/div/div[8]/div[1]/div/div/button")
          text = preorder_btn.text

          # make sure btn is there and it is not coming soon btn
          if preorder_btn and text == "Pre-Order":
              preorder_btn.click()
              # pause for render of pop-up window
              time.sleep(2)
              browser.find_element_by_xpath("/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a").click()
              searching = False
      except Exception as e:
          print(e)
      else:
          print("didn't find it")
          browser.refresh()


if __name__ == "__main__":
    main()
