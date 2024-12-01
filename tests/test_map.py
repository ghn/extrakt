import os
import tempfile

from extrakt.map import build_map_config, create_image
from extrakt.base import create_webdriver, open_activity

gpx = open_activity("tests/fixtures/trace.gpx")
webdriver = create_webdriver()


def test_create_image():
    with tempfile.TemporaryDirectory() as tmp_dir:
        output_file = create_image(gpx, tmp_dir, webdriver)
        assert os.path.exists(output_file)


def test_build_map_config():
    config = build_map_config(gpx)
    assert config["height"] == 436
    assert config["width"] == 1088

    coord = config["coordinates"]
    assert len(coord) == 9676
