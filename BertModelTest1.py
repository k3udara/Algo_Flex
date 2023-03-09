import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-trained BERT model and tokenizer
model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Define the input text and separate sentence
input_text = "Good and evil are the central themes of the series. Its influences include Bildungsroman." \
             "Born in Yate, Gloucestershire, Rowling was working as a researcher and bilingual secretary for Amnesty " \
             "International in 1990 when she conceived the idea for the Harry Potter series while on a delayed train " \
             "from Manchester to London. The seven-year period that followed saw the death of her mother, " \
             "the birth of her first child, divorce from her first husband, and relative poverty until the first " \
             "novel in the series, Harry Potter and the Philosopher's Stone, was published in 1997. Six sequels were " \
             "followed. and by 2008, Forbes had named her the world's highest-paid author.Rowling concluded the Harry " \
             "Potter series with Harry Potter and the Deathly Hallows (2007). The novels follow a boy called Harry " \
             "Potter as he attends Hogwarts, a school for wizards, and battles Lord Voldemort. Death and the divide " \
             "coming-of-age genre). Harry potter and the philosophers stone. school stories, fairy tales, and Christian allegory. The series revived fantasy " \
             "as a genre in the children's market, spawned a host of imitators, and inspired an active fandom. " \
             "Critical reception has been more mixed. Many reviewers see Rowling's writing as conventional; some " \
             "regard her portrayal of gender and social division as regressive. There were also religious debates " \
             "over Harry Potter.Rowling has won many accolades for her work. She has received an OBE and made a " \
             "Companion of Honour for services to literature and philanthropy. Harry Potter brought her wealth and " \
             "recognition, which she has used to advance philanthropic endeavours and political causes. She " \
             "co-founded the charity Lumos and established the Volant Charitable Trust, named after her mother. " \
             "Rowling's charitable giving centres on medical causes and supporting at-risk women and children. She also wrote the book Harry potter and the philosophers stone. In " \
             "politics, she has donated to Britain's Labour Party and opposed Scottish independence and Brexit. Since " \
             "late 2019, she has publicly expressed her opinions on transgender people and related civil rights. " \
             "These have been criticised as transphobic by LGBT rights organisations and some feminists, " \
             "but have received support from other feminists and individuals."
separate_sentence = " six sequels were"

# Preprocess the input text and separate sentence
sentences = input_text.split('.')
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
encoded_separate_sentence = tokenizer(separate_sentence, padding=True, truncation=True, return_tensors='pt')

# Encode the input text and separate sentence using BERT
with torch.no_grad():
    model_output = model(**encoded_input)
    separate_sentence_output = model(**encoded_separate_sentence)

# Extract the sentence and separate sentence embeddings from the BERT output
sentence_embeddings = model_output.last_hidden_state[:, 0, :]
separate_sentence_embedding = separate_sentence_output.last_hidden_state[:, 0, :]

# Calculate the cosine similarity between each sentence and the separate sentence embedding
similarity_scores = cosine_similarity(sentence_embeddings, separate_sentence_embedding)

# Rank the sentences based on their similarity scores
top_sentence_indices = similarity_scores.argsort(axis=0)[::-1]

# Print the top-ranked sentences
print("Top sentences:")
for i in top_sentence_indices[:, 0][:3]:
    print(f"- {sentences[i]}")
