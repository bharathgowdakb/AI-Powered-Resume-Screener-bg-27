import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def parse_resume(file_path):
    pdf_reader = PyPDF2.PdfReader(open(file_path, "rb"))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def match_resume(resume_text, jd_text):
    stop_words = set(stopwords.words('english'))
    resume_text = ' '.join([w for w in resume_text.lower().split() if w not in stop_words])
    jd_text = ' '.join([w for w in jd_text.lower().split() if w not in stop_words])

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    keywords = list(set(jd_text.split()).intersection(set(resume_text.split())))
    return round(similarity, 2), keywords
