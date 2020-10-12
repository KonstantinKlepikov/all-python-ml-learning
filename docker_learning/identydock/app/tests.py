import unittest
import identydock


class TestCase(unittest.TestCase):

    def setUp(self):
        identydock.app.config["TESTING"] = True
        self.app = identydock.app.test_client()

    def test_get_mainpage(self):
        page = self.app.post("/", data=dict(name="Moby Dock"))
        assert page.status_code == 200
        assert 'Hello' in str(page.data)
        assert 'Moby Dock' in str(page.data)

    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>TEST</b><!--'))
        assert '<b>' not in str(page.data)


if __name__ == '__main__':
    unittest.main()
