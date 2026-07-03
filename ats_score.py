import re

def calculate_ats_score(resume_text, job_description):

    jd_keywords = set(
        re.findall(r'\b[a-zA-Z+#.]+\b', job_description.lower())
    )

    resume_words = set(
        re.findall(r'\b[a-zA-Z+#.]+\b', resume_text.lower())
    )

    matched = jd_keywords.intersection(resume_words)

    if len(jd_keywords) == 0:
        return 0, []

    score = int((len(matched) / len(jd_keywords)) * 100)

    missing = jd_keywords - resume_words

    return score, list(missing)[:10]