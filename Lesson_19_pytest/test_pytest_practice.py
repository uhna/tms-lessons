import pytest as pytest


class TestMyClass():
    @pytest.mark.parametrize("lady", ["Sarah", "Jane", "Elizabeth"])
    def test_my_first_test(self, person, lady, end_of_story, big_end_of_story):
        print(f"{person} loves {lady}")

    @pytest.mark.skip
    def test_i_dont_like(self):
        pass

    @pytest.mark.fast
    def test_favorite(self):
        pass
