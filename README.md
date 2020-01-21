## Atomized Ltd. Test
Text Summarization Problem Solution - Mohamed Serry

## Problem Solving Approach
For this problem i chose a stochastic Extraction based summariazation process that combines word frequency and word count into a final metric: score to word count ratio. 

## Improvised Problem Statement
Given N number of sentences budget, find summary of N sentences such that: MAX( overall score : word count in sentences) and N sentence scores > threshold of scores. 

Therefore, i rephrased the problem into an optimzation problem where i aim to maximize the score to word count ratio for each subset of sentence combinations.

## STEPS
1 - Tokenize Words
2 - Stem words to origin roots.
3 - Strip characters such as . , from the word tokens to get to the actual word count.
4 - Count words while ignoring stop words for the english language.
5 - Count word frequency.
6 - Tokenize sentences from the source text. 
7 - Score sentences based on the frequency of words in the sentence
8 - Calculate the average sentence score.
9 - Calculate the sentence budget for our summary (20%, 40%...etc from the total sentences count)
10 - Generate a set of the highest scored sentences, where each element is a tuple of: (sentence, score, word count in sentence)
11 - Generate N unique subsets of size K from the set of sentence tuples (possible valid summary candidates). 
12 - linear search through the subsets while scoring them to calculate the overall score to word count ratio in the summary and rank them accordingly. 
13 - find the best sentences that fit the summmary budget.

## FUTURE SOLUTIONS
towards the end of my solution i realized this could be easily encoded and solved using an evolutionary algorithim. and i may have been solving it with that in mind. bio inspired optimization techniques are relatively good with large search spaces. 

## REMARKS
this took me 4 pure hours without knowing anything about text processing beforehand. i literally didn't know what tokenization was. so in reality more like 2-3 hours as there was initial trial and error.

## WEAKNESSES
currently my solution does not do summaries larger than 40-50% of the text as it becomes invalid to generate good subsets of that size given our sentences.

the algorithimic complexity could defintely be improved. but the overall problem approach i chose is: solve for the base cases (20, 40%) and expand from there.

## INSTRUCTIONS TO RUN
i used pycharm during the development of this. but i just added the python files and defined a main function. the summary is appened to the original text file. 

