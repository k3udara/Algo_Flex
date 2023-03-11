from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('t5-base')              #can use t5-large for better resukts but take more time for prog to run
model = T5ForConditionalGeneration.from_pretrained('t5-base')

input_text = "Writing under the pen name J. K. Rowling, before her remarriage her name was Joanne Rowling,[2] or Jo.[" \
             "3] At birth, she was given no middle name.[2] Staff at Bloomsbury Publishing asked that she use two " \
             "initials rather than her full name, envisaging that young boys – their target readership – would not " \
             "want to read a book written by a woman.[2] She chose K (for Kathleen) as the second initial of her pen " \
             "name, from her paternal grandmother, and because of the ease of pronunciation of two consecutive " \
             "letters.[4] Following her 2001 remarriage,[5] she has sometimes used the name Joanne Murray when " \
             "conducting personal business.[6]"
inputs = tokenizer.encode("summarize: " + input_text, return_tensors='pt', max_length=512, truncation=True)

summary_ids = model.generate(inputs,
                              num_beams=4,          #increasing this will provide better sentences but will use more computing power
                              length_penalty=1.0,   #decreasing this will provide more accurate summaries but will provide shorter summaries
                              max_length=150,       #max length of summary
                              early_stopping=True)

summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print(summary)
