import torch
from transformers import BertTokenizer, BertModel

# Load the pre-trained BERT model and tokenizer
model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Define the input text
input_text = "Dogs are popular pets. They have been domesticated for thousands of years. They are loyal. They are friendly, and can be trained to perform a variety of tasks, from providing companionship to assisting people with disabilities. Dogs come in a wide range of breeds, sizes, and colors, each with their unique traits and personalities."

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
top_sentence_indices = similarity_scores.argsort(descending=True)[0][:3]

# Generate the summary
summary_sentences = [sentences[i] for i in top_sentence_indices]
summary = ' '.join(summary_sentences)

print(summary)
