import itertools

import Constants as c
import string

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
        scored_sent_table, sent_wrd_cnt_table = self.__gen_sentence_score_and_wrd_cnt_tables(tokenized_sentences,
                                                                                             wrd_freq_table)
        return self.__gen_summary(scored_sent_table, sent_wrd_cnt_table, c.threshold_percentage)

    def __get_tokenized_words_from_text(self, text):
        tokenized_words = word_tokenize(text, self.summary_lang)
        return list(filter(lambda token: token not in string.punctuation, tokenized_words))

    def __gen_word_freq_table(self, tokenized_words, stop_words):
        freq_table = dict()

        for word in tokenized_words:
            word = self.word_stemmer.stem(word).lower()
            if word not in stop_words:
                if word in freq_table:
                    freq_table[word] += 1
                else:
                    freq_table[word] = 1

        return freq_table

    def __get_tokenized_sentences_from_text(self, text):
        return sent_tokenize(text, self.summary_lang)

    def __gen_sentence_score_and_wrd_cnt_tables(self, sentences, word_freq_table):
        sentence_scores = dict()
        sentence_wrd_cnt_table = dict()
        for sentence in sentences:
            wrd_cnt_except_stp_words = 0
            for wrd, freq in word_freq_table.items():
                if wrd in sentence.lower():
                    wrd_cnt_except_stp_words += 1
                    sentence_wrd_cnt_table[sentence] = wrd_cnt_except_stp_words

                    if sentence in sentence_scores:
                        sentence_scores[sentence] += freq
                    else:
                        sentence_scores[sentence] = freq

            if sentence in sentence_scores:
                sentence_scores[sentence] = sentence_scores[sentence]

        return sentence_scores, sentence_wrd_cnt_table

    def __find_avg_sent_score(self, tokenized_sentences_scores):
        sum_of_scores = 0
        for scored_sentence in tokenized_sentences_scores:
            sum_of_scores += tokenized_sentences_scores[scored_sentence]

        return sum_of_scores / len(tokenized_sentences_scores)

    def __gen_summary(self, sentence_scores, sent_wrd_count_table, threshold):
        avg_sent_score = self.__find_avg_sent_score(sentence_scores)
        sentence_budget = int(threshold * len(sentence_scores))
        sentence_set = self.__gen_set_of_sentences(sentence_scores.keys(), sentence_scores,
                                                   sent_wrd_count_table, c.avg_score_factor * avg_sent_score)
        sub_sets_lst = self.__get_all_sub_sets_of_n_size(sentence_set, sentence_budget)
        max_sub_set = self.__find_max_subset(sub_sets_lst)

        summary = ''
        for sent_tuple in max_sub_set:
            summary += " " + sent_tuple[0]

        return summary

    def __gen_set_of_sentences(self, sentences, sentence_scores_table, sentence_word_count_table, avg_score):
        optimal_set_of_sentences = set()
        for sent, score, count in zip(sentences, sentence_scores_table, sentence_word_count_table):
            if sentence_scores_table[sent] >= avg_score:
                sent_tuple = (sent, sentence_scores_table[sent], sentence_word_count_table[sent])
                optimal_set_of_sentences.add(sent_tuple)

        return optimal_set_of_sentences

    def __get_all_sub_sets_of_n_size(self, sent_set, sent_budget):
        return list(itertools.combinations(sent_set, sent_budget))

    def __find_max_subset(self, subsets_list):
        max_scr_to_wrd_cnt_ratio = 0
        max_subset = tuple()
        for subset in subsets_list:
            subset_wrd_cnt = sum(n for _, _, n in subset)
            subset_score = sum(n for _, n, _ in subset)
            scr_to_wrd_cnt_ratio = self.__get_scr_to_wrd_cnt_ratio(subset_wrd_cnt, subset_score)
            if max_scr_to_wrd_cnt_ratio < scr_to_wrd_cnt_ratio:
                max_scr_to_wrd_cnt_ratio = subset_wrd_cnt
                max_subset = subset
        return max_subset

    def __get_scr_to_wrd_cnt_ratio(self, wrd_cnt, score):
        return score / wrd_cnt
