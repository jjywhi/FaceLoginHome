import os
from utils.screenshot import take_screenshot

def before_all(context):
    if not os.path.exists('features/reports'):
        os.makedirs('features/reports')

def after_scenario(context, scenario):
    if scenario.status == "failed":
        take_screenshot(context.driver, scenario.name.replace(" ", "_"))
