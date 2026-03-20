import allure

def attach_request(url, payload):
    allure.attach(str(payload), name=f"Request → {url}", attachment_type=allure.attachment_type.JSON)

def attach_response(response):
    allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.JSON)
