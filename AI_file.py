import re
from difflib import SequenceMatcher

TOPIC_KEYWORDS = {
    "love": ["love", "caring", "affection"],
    "faith": ["faith", "trust", "belief"],
    "strength": ["strength", "weak", "tired", "overwhelmed"],
    "hope": ["hope", "hopeless", "future"],
    "peace": ["peace", "calm", "still"],
    "wisdom": ["wisdom", "confused", "decisions"],
    "guidance": ["guidance", "lost", "direction"],
    "healing": ["healing", "hurt", "pain"],
    "patience": ["patience", "waiting"],
    "temptation": ["temptation", "struggle"],
    "forgiveness": ["forgive", "forgiveness"],
    "fear": ["fear", "scared", "afraid"],
    "anxiety": ["anxiety", "anxious", "worried"],
    "depression": ["depressed", "sad", "down"],
    "grief": ["grief", "loss"],
    "anger": ["anger", "angry", "frustrated"],
    "loneliness": ["lonely", "alone"],
    "stress": ["stress", "stressed"],
    "relationships": ["relationship", "marriage", "family"],
    "purpose": ["purpose", "meaning"],
}

def detect_topic(message):
    message = message.lower()

    # 1. Direct keyword match
    for topic, words in TOPIC_KEYWORDS.items():
        for w in words:
            if w in message:
                return topic

    # 2. Semantic similarity fallback
    best_topic = None
    best_score = 0

    for topic, words in TOPIC_KEYWORDS.items():
        for w in words:
            score = SequenceMatcher(None, message, w).ratio()
            if score > best_score:
                best_score = score
                best_topic = topic

    return best_topic or "guidance"
