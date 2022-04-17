import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
# api key
api_key = os.environ['apikey']
# api url
api_url = os.environ['url']

def translator_instance():
    '''authenticates users and translates phrases from language to another'''
    # authenticate user
    authenticator = IAMAuthenticator(api_key)
    # create instance of service
    language_translator = LanguageTranslatorV3(version='2021-08-01', 
                                               authenticator=authenticator)
    # set service url to api url
    language_translator.set_service_url(api_url)
    return language_translator

def english_to_french(english_text):
    '''translates english phrases to french'''
    # invokes translator instance
    language = translator_instance()
    # translates english text to french texts
    french_text = language.translate(text=english_text, model_id='fr')
    return french_text

def french_to_english(french_text):
    '''translates french texts to english texts'''
    # invokes translation instance
    language = translator_instance()
    # translates from french to english
    english_text = language.translate(text=french_text, model_id='en')
    return english_text
