from textgenrnn import textgenrnn 

textgen = textgenrnn()
textgen.train_from_file('./dataset/hallmark-xmas-movies.csv', num_epochs=1)
# #textgen.generate(1, temperature=0.5, prefix='', return_as_list=True)
# textgen.generateSamples(100, temperature=0.5, prefix='', return_as_list=True)

textgen.generate(3, temperature=1.0)