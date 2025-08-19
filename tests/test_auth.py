import time
from pages.auth_page import AuthPage
from pages.wednsday import WedPage

def test_mover_uz_auth_and_video(driver):
    driver.get("https://mover.uz/")
    auth_page = AuthPage(driver)
    wed_page = WedPage(driver)

    auth_page.click_login_btn()
    time.sleep(2)
    auth_page.enter_login_input("Cosmo_Cat")
    auth_page.enter_password_input("cosmocat1202271939")
    auth_page.click_submit_btn()
    time.sleep(3)

    wed_page.enter_search_input("wednsday")
    wed_page.click_serch_btn()
    time.sleep(2)

    wed_page.click_video_btn()
    time.sleep(2)
    wed_page.click_maximize_btn()
    time.sleep(2)
    wed_page.click_parameters_btn()
    wed_page.click_qual_btn()
    wed_page.click_better_qual_btn()
    wed_page.click_qual_back_btn()
    wed_page.click_parameters_btn()
    wed_page.click_play_btn()