import Constants as c

from FileHandling import TextFileHandler as tfh
from TextSummarizing import ExtractionSummarizer as es


def run_text_summary_demo():
    text = tfh.load_text_from_file(c.text_file_name)
    summary = c.summary_title + es().get_summary_for_text(text)
    tfh.save_text_to_file(summary, c.text_file_name)


if __name__ == "__main__":
    run_text_summary_demo()
