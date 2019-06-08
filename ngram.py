str = raw_input('Enter any string : ')
print str
unigrams = str.split()

n = int(input('Enter the n value for n-grams to calculate : '))
len_unigram = len(unigrams)
result = []

if n > 0 and n <= len_unigram:
    for i in range(len_unigram - n + 1):
        ngram = []
        for j in range(n):
            ngram.append(unigrams[i + j])
        result.append(ngram)

print(result)

print('------------------')
print('      NLTK        ')
print('------------------')

import nltk
bigrm = list(nltk.bigrams(unigrams))
print(bigrm)
nltk_result = list(nltk.ngrams(unigrams, n))
print(nltk_result)