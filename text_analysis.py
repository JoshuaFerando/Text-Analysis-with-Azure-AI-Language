from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

load_dotenv()
ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
ai_key = os.getenv('AI_SERVICE_KEY')
credential = AzureKeyCredential(ai_key)
ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

def analyze_text(user_text):   # ✅ user_text parameter is used
    try:
        results = {}

        # Detect Language
        detected = ai_client.detect_language(documents=[user_text])[0]
        results["language"] = detected.primary_language.name

        # Sentiment
        sentiment = ai_client.analyze_sentiment(documents=[user_text])[0]
        results["sentiment"] = sentiment.sentiment

        # Key Phrases
        phrases = ai_client.extract_key_phrases(documents=[user_text])[0].key_phrases
        results["key_phrases"] = phrases

        # Entities
        entities = ai_client.recognize_entities(documents=[user_text])[0].entities
        results["entities"] = [(e.text, e.category) for e in entities]

        # Linked Entities
        linked = ai_client.recognize_linked_entities(documents=[user_text])[0].entities
        results["linked_entities"] = [(l.name, l.url) for l in linked]

        return results
    except Exception as ex:
        return {"error": str(ex)}
