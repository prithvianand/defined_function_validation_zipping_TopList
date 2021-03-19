# we need to import regex library for this function
import re


def password_validation(password):
    # this is the regex expression for password format
    pattern = "[\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff]+[A-Za-z\0-9\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff.-]+[\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff0-9]+"
    regex = re.compile(pattern)
    # this check for the length of the password
    if len(password) >= 1 and len(password) <= 20:
        # this will check the format that the password need to be in.
        if (re.search(regex, password)):
            return "valid * password is strong"
        else:
            return "invalid * please follow the password format"
    else:
        return "lenth of should not be less than 1 and should not exceed 20 "


# Uit Tests
# * the password must begin with a latin letter,
# * the password can consist of Latin letters, numbers, dot and minuses,
# * the password must end only with a latin letter or number;
# * minimum password length is one character
# * maximum password length is 20 characters

# test for first condition
# 1.the password must begin with a latin letter
def test_BeginWithLatinPass():
    Result = "valid * password is strong"
    passoword = "ØA123.-B1"
    assert Result == password_validation(passoword)


def test_BeginWithLatinFail():
    Result = "invalid * please follow the password format"
    passoword = "123.-B"
    assert Result == password_validation(passoword)


# 2.the password must end only with a latin letter or number;
def test_EndWithLatinPass():
    Result = "valid * password is strong"
    passoword = "ØA123.-BØ"
    assert Result == password_validation(passoword)


def test_EndWithLatinFail():
    Result = "invalid * please follow the password format"
    passoword = "A123.-B"
    assert Result == password_validation(passoword)


def test_EndWithNumPass():
    Result = "valid * password is strong"
    passoword = "ØA123.-B2"
    assert Result == password_validation(passoword)


def test_EndWithNumFail():
    Result = "invalid * please follow the password format"
    passoword = "`A123.-B"
    assert Result == password_validation(passoword)


# 3.minimum password length is one character
def test_MinimunLenPass():
    Result = "lenth of should not be less than 1 and should not exceed 20 "
    passoword = ""
    assert Result == password_validation(passoword)


def test_MaximumLenPass():
    Result = "lenth of should not be less than 1 and should not exceed 20 "
    passoword = "`1234567899876543212345678"
    assert Result == password_validation(passoword)