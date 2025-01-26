import pytest
from exercise4.source import get_weather_data
import unittest.mock as mock


@mock.patch("exercise4.source.requests.get")
def test_get_weather_data(mocked_object):
    mocked_response = mock.Mock()
    mocked_response.status_code = 200
    mocked_response.json.return_value = {"temperature": 20, "condition": "good", "time": "20:31"}
    mocked_object.return_value = mocked_response
    city = "Warsaw"
    temperature, condition = get_weather_data(city)
    assert temperature == 20
    assert condition == "good"


@mock.patch("exercise4.source.get_weather_data")
def test_get_weather_data_failure(mocked_object):
    mocked_response = mock.Mock()
    mocked_response.status_code = 404
    mocked_object.return_value = mocked_response
    city = "Warsaw"
    with pytest.raises(ValueError, match="Failed to fetch weather data"):
        get_weather_data(city)
