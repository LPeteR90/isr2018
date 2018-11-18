import sys
import re
import operator

try:
    sys.stdout = open('Text Analysis\\output.txt', 'w')
except:
    sys.stdout = open('output.txt', 'w')

if len(sys.argv) >= 2:
    print("Reading given txt file.")
    file_name = sys.argv[1]

else:
    print("No file given - reading from default file.")
    file_name = "austin.txt"


print("Filename:", file_name)


def get_number_of_words(words):
    return len(words)

def get_number_of_distinct_words(words):
    return len(set(words))

def get_word_frequencies(words):
    wordfreq = {}
    for w in words:
        if w not in wordfreq.keys():
            wordfreq[w] = words.count(w)
    sorted_freq = sorted(wordfreq.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_freq


def get_pr_r(frequencies, total_word_count):
    pr_r_dict = {}
    counter = 0
    for freq in frequencies:
        pr_r_dict[freq[0]] = freq[1] / total_word_count
        if counter == 9:
            break
        counter += 1
    return pr_r_dict

def get_number_of_occurrences(frequencies):
    l = []
    for freq in frequencies:
        if freq[1] <= 10:
            l.append(freq[1])

    occ_freq = {}
    for w in frequencies:
        num = w[1]
        if int(num) <= 10:
            if num not in occ_freq.keys():
                occ_freq[num] = l.count(num)
    sorted_freq = sorted(occ_freq.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_freq


try:
    with open(file_name, "r") as txt_file:
        content = txt_file.read()
        s = re.sub(r'[^\w\s]', '', content)
        words = s.split()
        num_words = get_number_of_words(words)
        print("Number of words:", num_words)
        print("Number of distinct words:", get_number_of_distinct_words(words))
        freq = get_word_frequencies(words)
        print("Word Frequencies:", freq[:10])
        print("r*pr:", get_pr_r(freq, num_words))
        print("Words only appearing x times:", get_number_of_occurrences(freq))
except FileNotFoundError as e:
    print("File not found!")