from playwright.sync_api import sync_playwright
import playwright_spy

playwright_spy.load_sync(1)

"""
load to page
"""
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    playwright_spy.load_sync(page)
    page.goto("https://bot.sannysoft.com/")
    page.screenshot(path="example2.png", full_page=True)
    browser.close()

"""
load to context
"""
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    playwright_spy.load_sync(context)

    page = context.new_page()
    page.goto("https://bot.sannysoft.com/")
    page.screenshot(path="example3.png", full_page=True)
    browser.close()
