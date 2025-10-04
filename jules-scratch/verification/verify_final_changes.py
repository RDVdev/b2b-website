from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the HTML files
        base_path = os.path.abspath('.')
        js_code = "() => { for (const s of document.querySelectorAll('section')) { s.classList.remove('hidden'); s.classList.add('visible'); } }"

        # Verify index.html in dark mode
        page.goto(f'file://{base_path}/index.html')
        page.wait_for_load_state('domcontentloaded')
        page.click('#theme-switcher')
        page.wait_for_timeout(500) # Wait for animations
        page.evaluate(js_code)
        page.screenshot(path='jules-scratch/verification/index_final_dark.png')

        # Verify careers page in dark mode
        page.goto(f'file://{base_path}/careers.html')
        page.wait_for_load_state('domcontentloaded')
        page.click('#theme-switcher')
        page.wait_for_timeout(500) # Wait for animations
        page.evaluate(js_code)
        page.screenshot(path='jules-scratch/verification/careers_final_dark.png')

        browser.close()

if __name__ == '__main__':
    run()