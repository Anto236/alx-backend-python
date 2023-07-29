#!/usr/bin/env python3
""" Unittest module """

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized

import client
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """ Class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ Test method returns correct output """
        github_client = GithubOrgClient(org_name)
        github_client.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        '''self descriptive'''
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:

            mocked_public.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_public.assert_called_once()
            mocked_method.assert_called_once()
