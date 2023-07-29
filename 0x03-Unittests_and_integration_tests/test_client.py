#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient class
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class to test the GithubOrgClient class
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test the GithubOrgClient.org method with mocked get_json.
        """
        """Configure the mock to return a specific
        value when get_json is called."""
        expected_result = {
            "name": org_name,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        }
        mock_get_json.return_value = expected_result

        """Create an instance of GithubOrgClient"""
        github_client = GithubOrgClient(org_name)

        """Call the org method"""
        result = github_client.org()

        """Check that get_json is called once with the expected argument"""
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        """Check that the result is correct"""
        self.assertEqual(result, expected_result)
