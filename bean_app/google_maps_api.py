import requests


class Mapper:
    """
    This is just a simple class to separate out some of the
    functionality of the google maps api. We may need to
    it later. Although it is possible to make the api call directly
    from the client side, a server side call avoids having to expose
    the api in the html page.
    """

    def __init__(self):
        self.google_maps_api_key = None
        self.url = "https://maps.googleapis.com/maps/api/js" \
                   "?key={}&libraries=places&callback=initMap"
        self.javascript = None

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
        Uses the api key to make an api call. If the javascript has not
        already been cached retrieve it and return it.
        :return: javascript as a string
        """

        if not self.javascript:
            url = self.url.format(self.get_api_key())
            self.javascript = requests.get(url)

        return self.javascript

    def get_coordinates(self, address):
        """
        Use the  google geocoding api to convert the address into
        lat and long coordinates.
        :param address:
        :return: lat, long
        """
        pass
