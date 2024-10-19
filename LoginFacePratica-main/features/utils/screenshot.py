import os

def take_screenshot(driver, name):
    if not os.path.exists('features/reports/screenshots'):
        os.makedirs('features/reports/screenshots')
    driver.save_screenshot(f'features/reports/screenshots/{name}.png')
