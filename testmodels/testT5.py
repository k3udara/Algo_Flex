from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('t5-base')
model = T5ForConditionalGeneration.from_pretrained('t5-base')

input_text = 'According to a recent study, the number of people working remotely has increased significantly in the last few years. The study found that the benefits of remote work include increased productivity, lower stress levels, and improved work-life balance. However, there are also some challenges associated with remote work, such as feelings of isolation and difficulty with communication. The study recommends that companies provide adequate support and resources to remote workers to address these challenges and ensure that they can be successful in their roles.'
inputs = tokenizer.encode("summarize: " + input_text, return_tensors='pt', max_length=512, truncation=True)

summary_ids = model.generate(inputs,
                              num_beams=4,
                              length_penalty=2.0,
                              max_length=150,
                              early_stopping=True)

summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print(summary)