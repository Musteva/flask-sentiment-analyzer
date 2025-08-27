from textblob import TextBlob
import re

def sentiment_analyzer(text_to_analyse):
    
    if not text_to_analyse or not text_to_analyse.strip() or not re.search(r'[a-zA-Z]', text_to_analyse):
        return None

    blob = TextBlob(text_to_analyse)
    
    score = blob.sentiment.polarity
    
    if score > 0:
        label = 'SENT_POSITIVE'
    elif score < 0:
        label = 'SENT_NEGATIVE'
    else:
        label = 'SENT_NEUTRAL'
        
    return {'label': label, 'score': score}
