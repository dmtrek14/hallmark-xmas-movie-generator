from textgenrnn import textgenrnn 

textgen = textgenrnn()
textgen.train_from_file('bot/dataset/hallmark-xmas-movies.csv', num_epochs=100)
textgen.generate(1, temperature=0.5, prefix='', return_as_list=True)