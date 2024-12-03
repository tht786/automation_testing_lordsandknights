import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://lordsandknights.com/")
    page.get_by_role("img", name="Impregnable castles").click()
    page.locator(".pop-up--screenshot--right-control > .icon").click()
    page.locator(".pop-up--screenshot--right-control > .icon").click()
    page.locator(".pop-up--screenshot--right-control > .icon").click()
    page.locator(".pop-up--screenshot--right-control > .icon").click()
    page.locator(".pop-up--screenshot--right-control > .icon").click()
    page.locator(".pop-up--screenshot--closer").click()
    page.locator("label").click()
    page.get_by_role("button", name="PLAY NOW").click()
    page.get_by_role("button", name="OK").click()
    with page.expect_popup() as page1_info:
        page.locator("div:nth-child(2) > .form-social__button-icon > .icon").first.click()
    page1 = page1_info.value
    page1.get_by_label("Email or phone").click()
    page1.get_by_label("Email or phone").click()
    page1.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
