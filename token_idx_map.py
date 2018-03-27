from collections import Counter
class token2idx:
    '''
    Build a vacabulary and dictionary of tokens
    Map each token into an unique ID
    Note, a text can be viewed as a series of sentences
    a sentence consist of words
    '''
    def __init__(self, texts, vocab_size=20000):
        '''
        Args:
        sents: a list of words or lists
        vocab_size: length of the vocabulary
        '''
        assert isinstance(texts, list) == True
        #sentences
        self.__texts = texts
        self.__vocab_size = vocab_size
        self.__word_idx_dict = None
        self.__idx_word_dict = None

    def proceed(self):
        '''
        Flatten word lists and build vocabulary
        '''
        #Flatten word lists
        words_all = list(self.__flatten__(self.__texts))
        #Calculate word frequences
        word_freq_pair = Counter(words_all)
        #Select the most common ones
        if len(word_freq_pair) <= self.__vocab_size:
            word_common = word_freq_pair
        word_common = word_freq_pair.most_common(self.__vocab_size)
        #Build a vocabulary and dictionaries
        vocab, _ = list(zip(*word_common))
        self.__word_idx_dict = {word: i for i, word in enumerate(vocab)}
        #Add one more as unknown symbols
        self.__word_idx_dict['*unknown*'] = len(vocab)
        self.__idx_word_dict = dict(zip(self.__word_idx_dict.values(), 
                                        self.__word_idx_dict.keys()))

        #Map the texts into series of IDs
        texts_idx = self.map_text_idx(self.__texts)
        return texts_idx

    def map_text_idx(self, texts):
        '''
        Map text of words into idx
        '''
        texts_idx = []
        #Traverse each text
        for text in texts:
            text_idx = []
            if (len(text) > 0) and isinstance(text[0], str):
                text_idx = list(map(self.__word2idx__, text))
            elif (len(text) > 0) and isinstance(text[0], list):
                #Traverse each sentence
                for sent in text:
                    #If a text consists of sentences
                    if isinstance(sent, list):
                        sent_idx = list(map(self.__word2idx__, sent))
                        text_idx.append(sent_idx)
            texts_idx.append(text_idx)
        return texts_idx

    def __word2idx__(self, word):
        '''
        Map a word into an ID
        '''
        try:
            ID = self.__word_idx_dict[word]
        except:
            ID = len(self.__word_idx_dict)
        return ID

    def __idx2word__(self, ID):
        '''
        Map an ID into a word
        '''
        try:
            word = self.__idx_word_dict[ID]
        except:
            word = '*unknown*'
        return word

    ##https://www.zhihu.com/question/27010691/answer/248832634
    def __flatten__(self, l): 
        for k in l: 
            if not isinstance(k, (list, tuple)): 
                yield k 
            else: 
                yield from self.__flatten__(k)

