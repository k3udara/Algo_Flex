import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer

class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.paragraphs = self.extract_paragraphs(text)
        self.keywords = self.preprocess_and_extract_keywords()

    def extract_paragraphs(text):
        return re.split(r'\n+', text)

    def preprocess_paragraph(paragraph):
        # lowercase
        paragraph = paragraph.lower()
        # remove numbers
        paragraph = re.sub(r'\d', '', paragraph)
        # remove punctuation
        paragraph = re.sub(r'[^\w\s]', '', paragraph)
        # tokenize words
        words = word_tokenize(paragraph)
        # remove stop words
        words = [word for word in words if word not in stopwords.words('english')]
        # lemmatize words
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word) for word in words]
        # join words back into a single string
        preprocessed_paragraph = ' '.join(words)
        return preprocessed_paragraph

    def keyword_extraction(words):
        # find frequency of each word
        fdist = FreqDist(words)
        # return the top N most frequent words
        N = 10
        return fdist.most_common(N)

    text = "The modern world courses are too boring to be theoretical. We adapt the current trends in Ed-Tech and engineer our courses so that you learn all the concepts upon completing well-designed projects. The project-based courses will have two key advantages; first, you would learn everything effortlessly with more interest, and second, you would unintentionally build a solid portfolio to showcase by the end of the course. Our teaching process involves going beyond the textbooks and exposing students to the latest technological tools and visual methods. When teaching analytical and logical subjects, there are multiple tools, technologies and visual aids that could be incooparated to streamline the learning process."

    # extract paragraphs
    paragraphs = extract_paragraphs(text)

    # preprocess each paragraph and extract keywords
    
    keywords = []
    for paragraph in paragraphs:
        preprocessed_paragraph = preprocess_paragraph(paragraph)
        words = word_tokenize(preprocessed_paragraph)
        keywords.append(keyword_extraction(words))

    # print the keywords for each paragraph
    for i, paragraph_keywords in enumerate(keywords):
        print(f"Paragraph {i}:")
        print(paragraph_keywords)