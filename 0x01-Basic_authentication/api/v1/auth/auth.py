#!/usr/bin/env python3
"""
Module that implements authentication
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """
    This is a class that contains authorization
    functions
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns: True if path not in excluded_paths
        """
        if path is None or excluded_paths is None:
            return True

        if path[-1] != '/':
            path = path + "/"

        if path not in excluded_paths:
            return True

        else:
            return False

    def authorization_header(self, request=None) -> str:
        """
        Returns: None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns: None
        """
        return None
