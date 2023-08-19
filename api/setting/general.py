# POSTKU
import os

# GENERAL
max_latency = 1000000
berear_token = "Bearer 38cebe5affdc6038017ae850b112f50d15613c3f40d9d2a5d7bfd75f6218fcc2"

# TEST CASE MANAGEMENT
api_key = os.environ.get('API_KEY_QASE')
host_test_management = "https://api.qase.io/v1/result"
test_run = 10
test_code_project = "TF"

# SLACK NOTIFICATION
slack_webhook = os.environ.get('CLIENT_SLACK')
slack_title = os.environ.get('TEST')
url_artifact = os.environ.get('RUNID')
notif_slack = "ON"
notif_slack_just_failed = "NO"
