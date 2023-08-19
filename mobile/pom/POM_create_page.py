from selenium.webdriver.common.by import By

# ================================================ CREATE ================================================
CREATE_if_title = {
    "ANDROID": [By.ID, 'com.example.android.architecture.blueprints.todomvp.mock:id/add_task_title'],
    "IOS": ["", ""]
}

CREATE_if_desc = {
    "ANDROID": [By.ID, 'com.example.android.architecture.blueprints.todomvp.mock:id/add_task_description'],
    "IOS": ["", ""]
}
CREATE_btn_submit = {
    "ANDROID": [By.ID, 'com.example.android.architecture.blueprints.todomvp.mock:id/fab_edit_task_done'],
    "IOS": ["", ""]
}