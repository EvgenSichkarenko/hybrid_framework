
def example():
    depart_from = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='BE_flight_origin_city']")))
    depart_from.click()
    time.sleep(2)
    depart_from.send_keys(from_dp)
    time.sleep(1)
    depart_from.send_keys(Keys.ENTER)

    going_to = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='BE_flight_arrival_city']")))
    going_to.click()
    time.sleep(2)
    going_to.send_keys(going)
    search_results = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//li")))
    time.sleep(2)
    for result in search_results:
        if "New York (JFK)" in result.text:
            result.click()
            time.sleep(10)
            break

    self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
    all_dates = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody/tr"))). \
            find_elements(By.XPATH, "//td[@class=' weekend']")
    time.sleep(1)
    for date in all_dates:
        if date.get_attribute("data-date") == select_date:
            date.click()
            break

    self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
    time.sleep(6)

    height = self.driver.execute_script("return document.body.scrollHeight")
    while True:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        current_height = self.driver.execute_script("return document.body.scrollHeight")
        if height == current_height:
            break
        height = current_height

    self.driver.find_element((By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']")).click()

