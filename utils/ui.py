import allure
import uuid
from allure_commons.types import AttachmentType


def screen(driver):
    try:
        name = str(uuid.uuid4()) + ".png"
        allure.attach.file(driver.save_screenshot("/allure_report/" + name), name=name,
                           attachment_type=AttachmentType.PNG)
    except Exception as e:
        print(str(e))
