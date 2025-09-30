def extract_resume(resume_file):
    # Example using PDF/minimal placeholder (implement full extraction)
    text = resume_file.read().decode('utf-8')
    return {
        # Use custom logic or regex to extract sections
        'education': ...,
        'experience': ...,
        'skills': ...,
    }

def extract_jd_keywords(jd_text):
    # Use simple split, advanced: spacy/sklearn for phrase extraction
    keywords = [word for word in jd_text.split() if len(word) > 3]
    return keywords
