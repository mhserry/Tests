# sentence score threshold factor, hyper parameter that can be
# tweaked that dictates the boundary on which we choose the top sentences.
avg_score_factor = 1.25

# percentage summary any value < 50% only
threshold_percentage = 0.4

# files directory to load from. please change this first before you proceed.
data_files_dir = 'C:\\Users\\semap\\Downloads\\Tests-master\\Tests-master\\data'

# default name for the text file. please change this if you'd require loading from a different file.
text_file_name = "Text_To_Summarize.txt"

# constants for file reading / writing operations.
file_read_command = "r"
file_append_command = "a"

# constant for choosing nltk summary language
summary_lang = "english"

# constant string to separate the summary in the result file
summary_title = "\n\n\n============================ SUMMARY ========================\n\n\n"
