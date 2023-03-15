import json
import pytest
from ..microservices import rinex_to_csv, rinex_to_csv_with_tags
from fastapi.testclient import TestClient

@pytest.fixture(scope='module')
def openapi_json_rinex_to_csv():

    def _openapi_json_rinex_to_csv(tags=False):

        app = rinex_to_csv.app

        if tags:
            app = rinex_to_csv_with_tags.app

        client = TestClient(app)

        response = client.get("/openapi.json")
        openapi = response.text

        assert openapi is not None, "Failed to get OpenAPI file"

        yield client, openapi

    return _openapi_json_rinex_to_csv