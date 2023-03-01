import sys
sys.path.append(r'D:\PROGRAMOWANIE\PYTHON\CASE')
import pytest

@pytest.mark.smoke
class TestsPost():

    def test_Post_id(self,setup_Post):
        assert setup_Post.id == "999"

    def test_Post_title(self, setup_Post):
        assert setup_Post.title == "WoW"
    
    def test_Post_subtitle(self, setup_Post):
        assert setup_Post.subtitle == "World of Warcraft"

    def test_Post_body(self, setup_Post):
        assert setup_Post.body == "The best game of from MMO category"

    def test_Post_change_title(self, setup_Post):
        setup_Post.name = "66"
        assert setup_Post.id == "66"

    def test_Post_change_title(self, setup_Post):
        setup_Post.title = "Valhalla"
        assert setup_Post.title == "Valhalla"

    def test_Post_change_subtitle(self, setup_Post):
        setup_Post.subtitle = "Assasin Valhalla"
        assert setup_Post.subtitle == "Assasin Valhalla"
    
    def test_Post_change_body(self, setup_Post):
        setup_Post.body = "Vikings game"
        assert setup_Post.body == "Vikings game"

    def test_complex_class_Post(self, setup_Post):
        setup_Post.body = "Vikings game"
        setup_Post.id = "66"
        setup_Post.title = "Valhalla"
        setup_Post.subtitle = "Assasin Valhalla"

        assert setup_Post.id == "66"
        assert setup_Post.title == "Valhalla"
        assert setup_Post.subtitle == "Assasin Valhalla"
        assert setup_Post.body == "Vikings game"

    