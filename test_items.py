def test_link_with_language(browser, language):
    browser.get(f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/')
    button = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form button')
    assert button
