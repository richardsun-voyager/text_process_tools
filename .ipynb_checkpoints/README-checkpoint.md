# text_process_tools
Text data usually consists of a series of unstructured symbols like words, punctuation, digits all of which combine into strings with varied lengths. It is complex but also necessary to handle text data ahead of NLP tasks such as feature extraction, classification and etc. In order to facilitate text processing, I wrote four tools to handle text data(English):
- text_preprocess.py : Remove punctuation and digits, lemmatize words and return clean text strings
- text_vectorizer.py : Simply clean the texts, vectorize them using tools from scikit-learn
- text_hier_split: Split texts into hierarchical structure, for example, a text can be divided into several sentences, and each sentence can be devided into tokens like words and punctuation
- token_idx_map: Build a vacabulary and a dictionary for texts of hierarchical-structure, map each word into an unique ID for latter usage like deep learning applications

Similar function can also be acquired by [textBlob](http://textblob.readthedocs.io/en/dev/) package, however it does not include punctuation for the texts.