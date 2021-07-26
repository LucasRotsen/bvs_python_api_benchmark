import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#######################################################################################
#                              DATABASE VARIABLES                                     #
#######################################################################################

POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE')

#######################################################################################
#                              CORS CONFIGURATION                                     #
#######################################################################################

ALLOWED_ORIGINS = [
    "http://localhost",
    "http://localhost:8080",
]
