from tt import TruthTable, BooleanExpression
import sys

try:
    sys.stdout = open('Boolean Model\\output.txt', 'w')
except:
    sys.stdout = open('output.txt', 'w')

query_terms = {"ka": "information", "kb": "retrieval", "kc": "science", "kd": "data"}
print("query terms:", query_terms)

query = query_terms["ka"] and (query_terms["kb"] or query_terms["kc"] or not query_terms["kd"])
b = BooleanExpression('ka and (kb or kc or not kd)')
print("query:", b.raw_expr, "\n")
t = TruthTable(b)
# t = TruthTable("ka and (kb or not kc)")
eq = t.equivalent_to(t)
print(t)

dnf = ""
cq = ""
print("DNF:")
for line in t:
    if line[1]:
        dnf += "("
        cq += "("
        for counter in range(len(b.symbols)):
            if line[0][counter] == 1:
                dnf += b.symbols[counter]
                cq += "1"
            else:
                dnf += "!" + b.symbols[counter]
                cq += "0"

            dnf += " & "
            cq += ", "
        dnf = dnf[:-3]
        dnf += ") || "
        cq = cq[:-2]
        cq += ") || "

dnf = dnf[:-3]
cq = cq[:-3]
print(dnf)
print("\ncq:")
print(cq)



