import pytest


class TestTarget:
    @pytest.mark.API
    def test_segment_creation(self, api_client):
        id = api_client.seg_create()
        assert id != ''

    @pytest.mark.API
    def test_delete_segment(self, api_client):
        id_create = api_client.seg_create()
        resp_del = api_client.delete_segment(id_create)
        assert resp_del.status_code == 204
