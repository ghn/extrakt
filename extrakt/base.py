import gpxpy
import gpxpy.gpx

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from .metadata import create_metadata_file
from .map import create_image, IMAGE_DIMENSION


def extract_all(file_path, output_dir):
    gpx = open_gpx(file_path)

    webdriver = create_webdriver()
    data_file = create_metadata_file(gpx, output_dir)
    map_file = create_image(gpx, output_dir, webdriver)

    return {"data_file": data_file, "map_file": map_file}


def open_gpx(file_path):
    gpx_file = open(file_path, "r")
    return gpxpy.parse(gpx_file)


def create_webdriver():
    """
    Create the selenium driver. Careful, this also downloads gecko driver from github!
    """
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()), options=options
    )

    offset = 84  # WHY is height not correctly set!!
    driver.set_window_size(IMAGE_DIMENSION["width"], IMAGE_DIMENSION["height"] + offset)

    return driver
