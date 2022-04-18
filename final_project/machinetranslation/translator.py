'''Needed libraries for this translations'''
import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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
    language = LanguageTranslatorV3(version='2021-08-01', authenticator=authenticator)
    # set service url to api url
    language.set_service_url(api_url)
    #language.set_disable_ssl_verification(True)
    return language

def english_to_french(english_text):
    '''translates english phrases to french'''
    # invokes translator instance
    language = translator_instance()
    # checks when text is empty
    if english_text == '' or english_text is None:
        return ''
    # else proceed with translatranslations
    # translates english text to french texts
    raw_text = language.translate(text=[english_text], model_id='en-fr').get_result()
    french_text = raw_text.get('translations')[0]['translation']
    return french_text

def french_to_english(french_text):
    '''translates french texts to english texts'''
    # invokes translation instance
    language = translator_instance()
    if french_text =='' or french_text is None:
        return ''
    # else proceed with transltranslations.
    # translates from french to english
    raw_text = language.translate(text=french_text, model_id='fr-en').get_result()
    english_text = raw_text.get('translations')[0]['translation']
    return english_text
