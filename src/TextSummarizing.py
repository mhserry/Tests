import Constants as c

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer


class ExtractionSummarizer(object):
    def __init__(self):
        self.summary_lang = c.summary_lang
        self.stop_words = set(stopwords.words(self.summary_lang))
        self.word_stemmer = PorterStemmer()

    def get_summary_for_text(self, text):
        tokenized_words = self.__get_tokenized_words_from_text(text)
        wrd_freq_table = self.__gen_word_freq_table(tokenized_words, self.stop_words)
        tokenized_sentences = self.__get_tokenized_sentences_from_text(text)
        scored_sent_table = self.__gen_sentence_score_table(tokenized_sentences, wrd_freq_table)
        avg_sent_score = self.__find_avg_sent_score(scored_sent_table)
        return self.__gen_summary(tokenized_sentences, scored_sent_table, avg_sent_score)

    def __get_tokenized_words_from_text(self, text):
        return word_tokenize(text, self.summary_lang)

    def __gen_word_freq_table(self, tokenized_words, stop_words):
        freq_table = dict()

        for word in tokenized_words:
            word = self.word_stemmer.stem(word).lower()
            if word in stop_words:
                continue
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1

        return freq_table

    def __get_tokenized_sentences_from_text(self, text):
        return sent_tokenize(text, self.summary_lang)

    def __gen_sentence_score_table(self, sentences, word_freq_table):
        sentence_scores = dict()
        for sentence in sentences:
            wrd_cnt_except_stp_wrds = 0
            for wrd, freq in word_freq_table.items():
                if wrd in sentence.lower():
                    wrd_cnt_except_stp_wrds += 1
                    if sentence in sentence_scores:
                        sentence_scores[sentence] += freq
                    else:
                        sentence_scores[sentence] = freq

            if sentence in sentence_scores:
                sentence_scores[sentence] = sentence_scores[sentence] / wrd_cnt_except_stp_wrds

        return sentence_scores

    def __find_avg_sent_score(self, tokenized_sentences_scores):
        sum_of_scores = 0
        for scored_sentence in tokenized_sentences_scores:
            sum_of_scores += tokenized_sentences_scores[scored_sentence]

        return sum_of_scores / len(tokenized_sentences_scores)

    def __gen_summary(self, tokenized_sentences, sentence_scores, avg_score):
        summary = ''
        for sentence in tokenized_sentences:
            if sentence in sentence_scores and (sentence_scores[sentence] > avg_score):
                summary += " " + sentence

        return summary
