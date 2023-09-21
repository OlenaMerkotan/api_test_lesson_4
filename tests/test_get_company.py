import pytest
import requests
from pprint import pprint
from data.data_files import StatusCompanies
from src.my_requests import MyRequests


class TestStatusCompanies:
    status_list = StatusCompanies.status_list
    requests = MyRequests()

    @pytest.mark.parametrize("status", status_list)
    def test_get_statuses_companies(self, status):
        response = self.requests.get(f"/?status={status}&limit=3&offset=0")
        # print(response.json())
        pprint(response.json())
    def test_get_closed_companies(): #rerun tomorrow status code actual 422
        response = self.request(f"""{base_url}/?status=CLOSED&limit=3&offset=0""")
        assert response.status_code == 200, f"Status code is not 200, it is {response.status_code}"
        # print(response.json())
        # pprint(response.json())
        # print(response.status_code)
        # print(response.request)
        print(response.headers)
    def test_get_bankrupt_companies():

        response = requests.get(f"""{base_url}/?status=BANKRUPT&limit=3&offset=0""")
        # print(response.json())
        pprint(response.json())

