# -*- coding: utf-8 -*-
import unittest

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import pytest

from ini.model.user import User


def test_login_with_invalid_credentials(app):
    app.ensure.logout()
    app.login(User.random())
    assert app.is_not_logged_in()


def test_login_with_valid_credentials(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_not_logged_in()
