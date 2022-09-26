import json
import unittest

from geocodingapibackend import create_app


class GetAddressDetailsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app().test_client()

    def test_get_address_details(self):

        payload = json.dumps(
            {
                "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru, Karnataka 560008",
                "output_format": "json",
            }
        )

        response = self.app.post(
            "/getAddressDetails",
            headers={"Content-Type": "application/json"},
            data=payload,
        )

        self.assertEqual(200, response.status_code)
