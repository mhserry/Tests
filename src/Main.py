import Constants as c

from FileHandling import TextFileHandler as tfh
from TextSummarizing import ExtractionSummarizer as es

text = tfh.load_text_from_file(c.text_file_name)
summary = es().get_summary_for_text(text)
tfh.save_text_to_file(c.summary_title + summary, c.text_file_name)
