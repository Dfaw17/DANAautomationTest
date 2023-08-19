from selenium.webdriver.common.by import By

# ================================================ HOME ================================================
HOME_btn_add = {
    "ANDROID": [By.ID, 'com.example.android.architecture.blueprints.todomvp.mock:id/fab_add_task'],
    "IOS": ["", ""]
}

HOME_data_1 = {
    "ANDROID": [By.XPATH, '(//android.widget.ListView/child::*)[1]'],
    "IOS": ["", ""]
}

HOME_checked_1 = {
    "ANDROID": [By.XPATH, '(//*[@resource-id = "com.example.android.architecture.blueprints.todomvp.mock:id/complete"])[1]'],
    "IOS": ["", ""]
}

HOME_checked_2 = {
    "ANDROID": [By.XPATH, '(//*[@resource-id = "com.example.android.architecture.blueprints.todomvp.mock:id/complete"])[2]'],
    "IOS": ["", ""]
}

HOME_no_task = {
    "ANDROID": [By.ID, 'com.example.android.architecture.blueprints.todomvp.mock:id/noTasks'],
    "IOS": ["", ""]
}

HOME_list_data_todo = {
    "ANDROID": [By.XPATH, '//android.widget.ListView/child::*'],
    "IOS": ["", ""]
}
