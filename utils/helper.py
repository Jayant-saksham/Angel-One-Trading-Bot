from pyotp import TOTP

def get_totp(secret):
    """Generate a TOTP based on the provided secret."""
    return TOTP(secret).now()
