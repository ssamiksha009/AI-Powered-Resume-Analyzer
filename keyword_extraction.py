import yake

def extract_keywords(text, max_keywords=10):
    keyword_extractor = yake.KeywordExtractor(top=max_keywords, stopwords=None)
    keywords = [kw[0] for kw in keyword_extractor.extract_keywords(text)]
    return set(keywords)

def get_skill_recommendations(missing_skills):
    skill_resources = {
        "python": "📚 Learn Python: https://www.w3schools.com/python/",
        "machine learning": "📚 ML Course: https://www.coursera.org/learn/machine-learning",
        "deep learning": "📚 Deep Learning: https://www.deeplearning.ai/",
        "nlp": "📚 NLP Course: https://www.udacity.com/course/natural-language-processing-nanodegree--nd892",
        "data science": "📚 Data Science Guide: https://www.kaggle.com/learn",
        "sql": "📚 SQL Tutorial: https://www.w3schools.com/sql/",
        "cloud computing": "📚 AWS Training: https://aws.amazon.com/training/",
        "tensorflow": "📚 TensorFlow Guide: https://www.tensorflow.org/tutorials",
    }

    recommendations = []
    for skill in missing_skills:
        for key in skill_resources:
            if key in skill.lower():
                recommendations.append(skill_resources[key])

    return recommendations
