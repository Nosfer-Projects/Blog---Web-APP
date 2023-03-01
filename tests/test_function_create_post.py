import sys
import pytest
sys.path.append(r"D:\PROGRAMOWANIE\PYTHON\CASE")
from PROJECTBLOG.main import post_to_flask_app
from PROJECTBLOG.post import Post


@pytest.mark.createpost
class TestsPost():

    def test_create_post(self, setup_API_json):
        data = post_to_flask_app(setup_API_json)
        assert len(data) == 2

    def test_check_post_id(self,setup_API_json ):
        post = post_to_flask_app(setup_API_json)
        id_of_posts = []
        for i in post:
            id_of_posts.append(i.id)

        assert id_of_posts == [1, 2]

    def test_check_post_title(self, setup_API_json):
        post = post_to_flask_app(setup_API_json)
        title_post = []
        for i in post:
            title_post.append(i.title)
        assert title_post == ["News Microsoft", "News Apple"]




