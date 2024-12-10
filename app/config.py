import os

class Config:
    SECRET_KEY="79f4795a886afd13fe3c0ae3fd6b486a"

    #dal urls
    URL_DAL_API= "https://b713105a-dcb9-4bdc-b39d-d7c333de4a7c.mock.pstmn.io"
    DAL_ROUTE_DEVICES ="devices"
    DAL_ROUTE_ACCOUNT= "account"

    #jwt key
    JWT_SECRET_KEY = "020edb75e072aad4564e404eb4095c94"
    JWT_TOKEN_LOCATION = ['cookies']  # Store JWT tokens in cookies
    JWT_COOKIE_SECURE = True  # Secure cookies; requires HTTPS
    JWT_ACCESS_COOKIE_PATH = '/'  # Path for access token cookie
    JWT_REFRESH_COOKIE_PATH = '/refresh'  # Path for refresh token cookie
    JWT_COOKIE_CSRF_PROTECT = False  # Set to True if enabling CSRF protection
    JWT_COOKIE_SAMESITE = 'Strict'  # SameSite policy for cookies