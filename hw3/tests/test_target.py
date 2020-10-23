import pytest


class TestTarget:
    @pytest.mark.API
    def test_segment_creation(self, api_client):
        response = api_client.seg_create()

        assert response.status_code == 200

    @pytest.mark.API
    def test_delete_segment(self, api_client):
        response = api_client.delete_segment()
        assert response.status_code == 204