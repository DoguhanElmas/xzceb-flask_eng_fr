"""Translator Module"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION = '2018-05-01'

AUTH = IAMAuthenticator(APIKEY)
LANGUAGETRANSLATOR = LanguageTranslatorV3(version=VERSION, authenticator=AUTH)
LANGUAGETRANSLATOR.set_service_url(URL)

def english_to_french(englishtext):
    """This function translates english to french"""
    if englishtext == "":
        return ""
    frtranslation = LANGUAGETRANSLATOR.translate(text=englishtext, model_id='en-fr').get_result()
    return frtranslation.get("translations")[0].get("translation")

def french_to_english(frenchtext):
    """This function translates french to english"""
    if frenchtext == "":
        return ""
    entranslation = LANGUAGETRANSLATOR.translate(text=frenchtext, model_id='fr-en').get_result()
    return entranslation.get("translations")[0].get("translation")
