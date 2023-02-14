from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, devtools=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto('http://127.0.0.1:8000/login/?next=/')

    page.fill("input[name=\"username\"]", "alice")
    page.fill("input[name=\"password\"]", "Qamania123")
    page.click("text=Login")

    page.click("text=Create new test")
    page.click("input[name=\"name\"]")
    page.fill("input[name=\"name\"]", "hello")
    page.click("textarea[name=\"description\"]")
    page.fill("textarea[name=\"description\"]", "world")
    page.click("input:has-text(\"Create\")")

    page.click("text=Test Cases")

    assert page.query_selector('//td[text()="hello"]') is not None

    page.goto('http://127.0.0.1:8000/tests/')

    page.click("//tr[13]/td[9]/button[normalize-space(.)='Delete']")

    page.close()
    context.close()
    browser.close()


def test_new_testcase():
    with sync_playwright() as playwright:
        run(playwright)
