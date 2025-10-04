from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the HTML files
        base_path = os.path.abspath('.')

        # This JS code will remove the 'hidden' class that causes the content to be invisible
        # and add the 'visible' class to make sure the content is shown.
        js_code = "() => { for (const s of document.querySelectorAll('section')) { s.classList.remove('hidden'); s.classList.add('visible'); } }"

        # Verify index.html
        page.goto(f'file://{base_path}/index.html')
        page.wait_for_load_state('domcontentloaded')
        page.evaluate(js_code)
        page.screenshot(path='jules-scratch/verification/index.png')

        # Verify about.html
        page.goto(f'file://{base_path}/about.html')
        page.wait_for_load_state('domcontentloaded')
        page.evaluate(js_code)
        page.screenshot(path='jules-scratch/verification/about.png')

        # Verify features.html
        page.goto(f'file://{base_path}/features.html')
        page.wait_for_load_state('domcontentloaded')
        page.evaluate(js_code)
        page.screenshot(path='jules-scratch/verification/features.png')

        # Verify careers.html
        page.goto(f'file://{base_path}/careers.html')
        page.wait_for_load_state('domcontentloaded')
        page.evaluate(js_code)
        page.screenshot(path='jules-scratch/verification/careers.png')

        browser.close()

if __name__ == '__main__':
    run()