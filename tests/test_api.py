import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_generate_text(self):
        url = "http://127.0.0.1:8000/generate/"
        data = {"prompt": "Once upon a time", "max_length": 50}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("generated_text", response.json())

if __name__ == "__main__":
    unittest.main()
