'''
This file works as a language translator for english and french
'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text: str) -> str:
    """
    This function translates english text to french
    """
    #write the code here
    print(f"Translating {english_text} to french")
    french_translation: dict = language_translator.translate(
        text=english_text,
        model_id="en-fr").get_result()
    translations = french_translation.get("translations")
    return translations[0].get("translation")

def french_to_english(french_text: str) -> str:
    """
    This function translates french text to english
    """
    #write the code here
    print()
    print(f"Translating {french_text} to english")
    english_translation = language_translator.translate(
        text=french_text,
        model_id="fr-en").get_result()
    translations = english_translation.get("translations")
    return translations[0].get("translation")
