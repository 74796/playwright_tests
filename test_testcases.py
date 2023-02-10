from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to http://127.0.0.1:8000/login/?next=/
    page.goto("http://127.0.0.1:8000/login/?next=/")
    # Click input[name="username"]
    page.click("input[name=\"username\"]")
    # Fill input[name="username"]
    page.fill("input[name=\"username\"]", "alice")
    # Click input[name="password"]
    page.click("input[name=\"password\"]")
    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "Qamania123")
    # Click text=Login
    page.click("text=Login")
    # assert page.url == "http://127.0.0.1:8000/"
    # Click text=Create new test
    page.click("text=Create new test")
    # assert page.url == "http://127.0.0.1:8000/test/new"
    # Click input[name="name"]
    page.click("input[name=\"name\"]")
    # Fill input[name="name"]
    page.fill("input[name=\"name\"]", "hello")
    # Click textarea[name="description"]
    page.click("textarea[name=\"description\"]")
    # Fill textarea[name="description"]
    page.fill("textarea[name=\"description\"]", "world")
    # Click input:has-text("Create")
    page.click("input:has-text(\"Create\")")
    # assert page.url == "http://127.0.0.1:8000/test/new"
    # Click text=Test Cases
    page.click("text=Test Cases")
    # assert page.url == "http://127.0.0.1:8000/tests/"

    assert page.query_selector('//td[text()="hello"]') is not None

    # Click text=41 hello world alice Norun None PASS FAIL Details Delete >> :nth-match(button, 4)
    page.click("//tr[13]/td[9]/button[normalize-space(.)='Delete']")
    # ---------------------
    context.close()
    browser.close()


def test_new_testcase():
    with sync_playwright() as playwright:
        run(playwright)
