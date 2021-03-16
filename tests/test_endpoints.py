import pytest
import requests
from .configuration import config
# from api_test_utils.oauth_helper import OauthHelper


class TestEndpoints:

    def test_ping_endpoint(self):
        response = requests.get(f"{config.BASE_URL}/{config.PROXY}/_ping")
        assert response.status_code == 200
        assert list(response.json().keys()) == ['version', 'revision', 'releaseId', 'commitId']

    # def test_user_restricted(self):
    #     oauth = OauthHelper(client_id="<client_id>", client_secret="<client_secret>", redirect_uri="<redirect_uri>")
