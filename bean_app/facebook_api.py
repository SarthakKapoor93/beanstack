
class FacebookKeyAccess:

    def get_facebook_key(self):
        facebook_key = ''
        try:
            with open('social_auth_facebook_key.key', 'r') as f:
                facebook_key = f.readline().strip()
        except IOError('"social_auth_facebook_key.key" file not found'):
            pass
        return facebook_key

    def get_facebook_secret(self):
        facebook_secret = ''
        try:
            with open('social_auth_facebook_secret.key', 'r') as f:
                facebook_secret = f.readline().strip()
        except IOError('"social_auth_facebook_secret.key" file not found'):
            pass
        return facebook_secret

