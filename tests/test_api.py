import sys
import pytest
sys.path.append(r'D:\PROGRAMOWANIE\PYTHON\CASE')
from PROJECTBLOG.main import API



class Tests_Api():

    def test_status_of_api_requests(self, setup_API_get):
        assert setup_API_get.status_code == 200

    def test_if_API_got_same_address(self):
        assert "https://api.npoint.io/d6281a1edce99b4598cf" == API

    def test_if_url_for_API(self, setup_API_get):
        assert 'https://api.npoint.io/d6281a1edce99b4598cf' == setup_API_get.url

    def test_if_same_text_is_after_get(self, setup_API_text, setup_API_get):
        assert setup_API_get.text == setup_API_text

    def test_if_content_could_be_list(self, setup_API_json):
        assert type(setup_API_json) == list

    def test_if_all_post_in_API_are_json(self, setup_API_json):
        for i in setup_API_json:
            assert type(i) == dict

    def test_if_lenght_of_dict_is_2(self, setup_API_json):
        assert len(setup_API_json) == 2
    
    def test_if_text_start_with_first_post(self, setup_API_text):
        assert setup_API_text.startswith('[{"id":1,"body')
    
    def test_if_id_of_post_1_is_equal_id_1(self, setup_API_json):
        assert setup_API_json[0]["id"] == 1

    def test_if_id_of_post_2_is_equal_id_2(self, setup_API_json):
        assert setup_API_json[1]["id"] == 2

    def test_title_first_post(self, setup_API_json):
        assert setup_API_json[0]["title"] == "News Microsoft"

    def test_title_second_post(self, setup_API_json):
        assert setup_API_json[1]["title"] == "News Apple"

    def test_subtitle_first_post(self, setup_API_json):
        assert setup_API_json[0]["subtitle"] == "How brands are using Microsoft AI to be more productive and imaginative"

    def test_subtitle_first_post(self, setup_API_json):
        assert setup_API_json[1]["subtitle"] == "Apple partnerships are helping build new homes and new starts in communities across California"

    def test_wrong_API(self, setup_wrong_API):
        assert setup_wrong_API.status_code == 500

    def test_encoding_of_API(self, setup_API_get):
        assert setup_API_get.encoding == "utf-8"

    

    

    
    




    


    




