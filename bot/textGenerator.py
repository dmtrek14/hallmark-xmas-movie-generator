from textgenrnn import textgenrnn 

# textgen = textgenrnn()
# textgen.train_from_file('./dataset/titles.txt', num_epochs=50, is_csv=False)

# #generate to file
# textgen.generate_to_file('./dataset/output-titles.txt', n=250)

titlesBot2 = textgenrnn()
titlesBot2.train_from_file('./dataset/titles.txt', num_epochs=10, is_csv=False)

#generate to file
titlesBot2.generate_to_file('./dataset/output-titles-2.txt', n=250)

#summaries
textgen2 = textgenrnn()
textgen2.train_from_file('./dataset/summaries.txt', num_epochs=10, is_csv=False)

textgen2.generate_to_file('./dataset/output-summaries.txt', n=250)