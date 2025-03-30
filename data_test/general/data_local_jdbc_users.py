import copy
from datetime import datetime

from utils.constants import BASE_CREDS

NOW = datetime.now().strftime("%Y%m%d%H%M%S")

# DO NOT REUSE THESE USERS ANYWHERE ELSE
MODIFIED_USER = {
    "username": "user_auto_modified",
    "password": "Password123!",
    "iss": BASE_CREDS["iss"],  # Used for login
    "tenant": BASE_CREDS["iss"],  # Used for create
    "confirmPassword": "Password123!",
    "roles": "ROLE_VIEW_DATA",  # The least permissions
    "firstname": "Auto",
    "lastname": "Modified",
    "email": "user_auto_modified@NotARealAddress.com",
    "enabled": True,
}
PASSWORD_USER = {
    "username": "user_auto_password",
    "password": "Password123!",
    "iss": BASE_CREDS["iss"],  # Used for login
    "tenant": BASE_CREDS["iss"],  # Used for create
    "confirmPassword": "Password123!",
    "roles": "ROLE_VIEW_DATA",  # The least permissions
    "firstname": "Auto",
    "lastname": "Password",
    "email": "user_auto_password@NotARealAddress.com",
    "enabled": True,
}
PL_NEW_USER = {
    "username": f"automation_temp_user{NOW}",
    "password": "Password123!",
    "confirmPassword": "Password123!",
    "firstname": "AutomationTempUser",
    "lastname": "AutomationTempUser",
    "email": f"automation_temp_user{NOW}@NotARealAddress.com",
    "tenant": BASE_CREDS["iss"],
}
MSG_NEW_USER = {
    "message":"Registration was successful! "
    "If auto-approval is not enabled, an administrator will need to approve "
    "this request before you can log in."
}
MSG_UPDATE_USER = {"message": f"Update for user {PL_NEW_USER['username']} was successful!"}
MSG_DEL_USER = {"message": f"User: {PL_NEW_USER['username']} was removed.  0 assignment(s) reset"}
MSG_PWD_CHANGE = {"message": "Password changed successfully"}
PL_USER_UPDATE = copy.deepcopy(PL_NEW_USER)
PL_USER_UPDATE["roles"] = "ROLE_ADMIN"
PL_USER_UPDATE["enabled"] = True
PL_USER_UPDATE["locked"] = False
PL_CHANGE_PASSWORD = {
    "currentPassword": PASSWORD_USER["password"],
    "newPassword": "Password1234!",
    "confirmPassword": "Password1234!",
}
NEW_PW_USER_LOGIN = {
    "username": PASSWORD_USER["username"],
    "password": PL_CHANGE_PASSWORD["newPassword"],
    "iss": PASSWORD_USER["iss"]
}
PL_RESTORE_PASSWORD = {
    "currentPassword": "Password1234!",
    "newPassword": PASSWORD_USER["password"],
    "confirmPassword": PASSWORD_USER["password"],
}
