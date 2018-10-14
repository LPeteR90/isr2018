import numpy as np
import sys

try:
    sys.stdout = open('Levenshtein\\output.txt', 'w')
except:
    sys.stdout = open('output.txt', 'w')

if len(sys.argv) >= 3:
    print("Reading given words.")
    start_word = sys.argv[1]
    end_word = sys.argv[2]
else:
    print("No words given - calculation performed with default words.")
    start_word = "workday"
    end_word = "saturDay"


start_word = start_word.lower()
end_word = end_word.lower()
print("Calculating Levensthein Distance for", "'" + start_word + "' and '" + end_word + "'")

matrix = np.zeros((len(start_word) + 1, len(end_word) + 1), dtype=int)
print("Init column 0 with numbers from 0 to m")
for counter in range(len(start_word) + 1):
    matrix[counter, 0] = counter

print("Init row 0 with numbers from 0 to n")
for counter in range(len(end_word) + 1):
    matrix[0, counter] = counter

counter1 = 1
counter2 = 1
for letterA in start_word:
    print("----------------- row", counter1, "-----------------")
    counterAdd = 0
    counter2 = 1
    for letterB in end_word:
        print("----------------- column", counter2, "-----------------")
        if letterA == letterB:
            print("Same characters:", letterA, "vs.", letterB, "- insert value A[i-1, j-1]:")
            print("->", matrix[counter1 - 1, counter2 - 1])
            matrix[counter1, counter2] = matrix[counter1 - 1, counter2 - 1]
        else:
            print("Diff characters:", letterA, "vs.", letterB, "- select minimal value:")
            print("-> min(A[i-1, j-1]+1, A[i, j-1]+1, A[i-1, j]+1): min(", matrix[counter1 - 1, counter2 - 1] + 1,
                  ",", matrix[counter1, counter2 - 1] + 1, ",", matrix[counter1 - 1, counter2] + 1, ")")
            replace = matrix[counter1 - 1, counter2 - 1] + 1
            insertion = matrix[counter1, counter2 - 1] + 1
            deletion = matrix[counter1 - 1, counter2] + 1
            matrix[counter1, counter2] = min([replace, insertion, deletion])
            print("-> ", matrix[counter1, counter2])
        counterAdd += 1
        counter2 += 1
    counter1 += 1

print("\n\n")
print("----------------- Levenshtein Matrix: -----------------")
print(matrix)

print("Levenshtein Distance: ", matrix[-1, -1])
