from playwright.sync_api import sync_playwright
import playwright_spy

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    playwright_spy.load_sync(page)
    page.goto("https://bot.sannysoft.com/")
    page.screenshot(path="example3.png", full_page=True)
    browser.close()
