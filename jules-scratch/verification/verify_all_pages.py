from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the HTML files
        base_path = os.path.abspath('.')
        js_code = "() => { for (const s of document.querySelectorAll('section')) { s.classList.remove('hidden'); s.classList.add('visible'); } }"

        # Verify index.html
        page.goto(f'file://{base_path}/index.html')
        page.wait_for_load_state('domcontentloaded')
        page.evaluate(js_code)
        page.screenshot(path='jules-scratch/verification/index_fixed.png')

        # Verify about.html with dark mode
        page.goto(f'file://{base_path}/about.html')
        page.wait_for_load_state('domcontentloaded')
        page.click('#theme-switcher')
        page.wait_for_timeout(500)
        page.evaluate(js_code)
        page.screenshot(path='jules-scratch/verification/about_fixed_dark.png')

        # Verify features.html with chatbot
        page.goto(f'file://{base_path}/features.html')
        page.wait_for_load_state('domcontentloaded')
        page.click('#chatbot-toggle')
        page.wait_for_timeout(500)
        page.evaluate(js_code)
        page.screenshot(path='jules-scratch/verification/features_fixed_chatbot.png')

        # Verify careers.html
        page.goto(f'file://{base_path}/careers.html')
        page.wait_for_load_state('domcontentloaded')
        page.evaluate(js_code)
        page.screenshot(path='jules-scratch/verification/careers_fixed.png')

        browser.close()

if __name__ == '__main__':
    run()