import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    try:
        browser.get(link)
        time.sleep(10)
        btn = browser.find_element_by_css_selector(".btn-add-to-basket")
        assert btn
        print("!!" * 20)
        print(f"Текст на кнопке: '{btn.text}'")
        print("!!" * 20)
    except Exception as e:
        print(e)
        assert False
