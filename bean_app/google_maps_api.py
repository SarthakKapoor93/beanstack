import requests
import re

"""
NOTE: This class is not being used at the moment because the javascript that we downloaded from 
google is static and not dymanic, meaning that it was possible to just download it and store in the 
static file: beanstack/static/assets/js/googlemaps-api.js

I haven't deleted the class yet because we may want to use it in the future for other api calls eg GeoCoding.
"""


class Mapper:
    """
    This is just a simple class to separate out some of the
    functionality of the google maps api. We may need to add to
    it later. Although it is possible to make the api call directly
    from the client side, a server side call avoids having to expose
    the api in the html page. You can get your own key from here:
    https://developers.google.com/maps/web-services/
    """

    def __init__(self):
        self.google_maps_api_key = None
        self.url = "https://maps.googleapis.com/maps/api/js" \
                   "?key={}&libraries=places&callback=initMap"

    def get_api_key(self):
        """
        Returns the api key if it has already been read from file. Otherwise
        reads it first before returning.
        :return: the api key as a string
        """

        if not self.google_maps_api_key:
            try:
                with open('google_maps_api.key', 'r') as f:
                    self.google_maps_api_key = f.readline().strip()
            except IOError('search.key file not found'):
                pass

        return self.google_maps_api_key

    def get_javascript(self):
        """
        Uses the api key to make an api call
        and return the javascript
        :return: javascript as a string
        """

        url = self.url.format(self.get_api_key())
        return requests.get(url)

    def geocode(self, address=None, lat=None, lng=None):
        """
        If an address is passed in, the method tries to get the coordinates,
        if there is no address but there are coordinates, it tries to get the address.
        If no arguments are passed in None values are returned.

        Raises a GeolocationException if no results are found. This passes back the error
        from the Google API.

        :param address: the address as a string
        :param lat: the latitude as a float
        :param lng: the longitude as a float
        :return: the formatted address, the lat and the lng or (None, None, None)
        """

        if address:
            formatted_address = ",+".join(re.split("[,\s]+", address))

            url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}"
            formatted_url = url.format(formatted_address, self.get_api_key())

            response = requests.get(formatted_url)
            json = response.json()

            if json['status'] != 'OK':
                raise GeolocationException(json['status'])

            lat = json['results'][0]['geometry']['location']['lat']
            lng = json['results'][0]['geometry']['location']['lng']
            address = json['results'][0]['formatted_address']

        elif lat and lng:

            url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}"
            formatted_url = url.format(lat, lng, self.get_api_key())

            response = requests.get(formatted_url)
            json = response.json()

            if json['status'] != 'OK':
                raise GeolocationException(json['status'])

            address = json['results'][0]['formatted_address']

        return address, lat, lng


class GeolocationException(Exception):
    pass





