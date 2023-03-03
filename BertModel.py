import torch
from transformers import BertTokenizer, BertModel

# Load the pre-trained BERT model and tokenizer
model = BertModel.from_pretrained('bert-base-uncased')    #The bert-base-uncased model is used, can use bert-large-uncased for better results
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Define the input text
input_text = "Good and evil are the central themes of the series. Its influences include Bildungsroman." \
             "Born in Yate, Gloucestershire, Rowling was working as a researcher and bilingual secretary for Amnesty " \
             "International in 1990 when she conceived the idea for the Harry Potter series while on a delayed train " \
             "from Manchester to London. The seven-year period that followed saw the death of her mother, " \
             "the birth of her first child, divorce from her first husband, and relative poverty until the first " \
             "novel in the series, Harry Potter and the Philosopher's Stone, was published in 1997. Six sequels " \
             "followed, and by 2008, Forbes had named her the world's highest-paid author.Rowling concluded the Harry " \
             "Potter series with Harry Potter and the Deathly Hallows (2007). The novels follow a boy called Harry " \
             "Potter as he attends Hogwarts, a school for wizards, and battles Lord Voldemort. Death and the divide " \
             "coming-of-age genre), school stories, fairy tales, and Christian allegory. The series revived fantasy " \
             "as a genre in the children's market, spawned a host of imitators, and inspired an active fandom. " \
             "Critical reception has been more mixed. Many reviewers see Rowling's writing as conventional; some " \
             "regard her portrayal of gender and social division as regressive. There were also religious debates " \
             "over Harry Potter.Rowling has won many accolades for her work. She has received an OBE and made a " \
             "Companion of Honour for services to literature and philanthropy. Harry Potter brought her wealth and " \
             "recognition, which she has used to advance philanthropic endeavours and political causes. She " \
             "co-founded the charity Lumos and established the Volant Charitable Trust, named after her mother. " \
             "Rowling's charitable giving centres on medical causes and supporting at-risk women and children. In " \
             "politics, she has donated to Britain's Labour Party and opposed Scottish independence and Brexit. Since " \
             "late 2019, she has publicly expressed her opinions on transgender people and related civil rights. " \
             "These have been criticised as transphobic by LGBT rights organisations and some feminists, " \
             "but have received support from other feminists and individuals."





# Preprocess the input text
sentences = input_text.split('.')
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Encode the input text using BERT
with torch.no_grad():
    model_output = model(**encoded_input)

# Extract the sentence embeddings from the BERT output
sentence_embeddings = model_output.last_hidden_state[:, 0, :]

# Rank the importance of each sentence based on its similarity to the input text
similarity_scores = torch.matmul(sentence_embeddings, sentence_embeddings.T)
top_sentence_indices = similarity_scores.argsort(descending=True)[0][:8]

# Generate the summary
summary_sentences = [sentences[i] for i in top_sentence_indices]
summary = ' '.join(summary_sentences)

print(summary)
