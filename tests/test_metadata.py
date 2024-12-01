from extrakt.metadata import extract_data
from extrakt.base import open_activity

gpx = open_activity("tests/fixtures/trace.gpx")


def test_extract_data():
    expected_result = {
        "distance": 16573,
        "moving_time": 9870,
        "stopped_time": 2532,
        "uphill": 1042,
        "downhill": 1061,
        "end_time": "2024-10-27T12:51:29+00:00",
        "start_time": "2024-10-27T09:24:47+00:00",
    }
    assert extract_data(gpx) == expected_result
