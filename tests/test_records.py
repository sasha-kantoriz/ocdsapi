from .base import storage, app
from werkzeug.exceptions import NotFound


def test_get(client, storage):
    with client.get('/api/record.json?ocid=test_ocid') as response:
        assert response.json['releases'][0] == storage.get_ocid('test_ocid')


def test_get_not_found(client, storage):
    with client.get('/api/record.json?ocid=') as response:
        assert response.status_code == 404


def test_response_ids_only(client, storage):
    with client.get('/api/records.json?idsOnly=True') as response:
        result = response.json
        assert result['records'] == [{"id": 'spam_id', "ocid": 'spam_ocid'}]


def test_prepare_response(client, storage):
    with client.get('/api/records.json') as response:
        result = response.json
        record = result['records'][0]
        assert 'compiledRelease' in record
        assert 'versionedRelease' in record
        assert 'releases' in record
