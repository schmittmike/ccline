# Michael Schmitt
# ECE 275 - HW03
# quine mcclusky method

import copy

class Terms:
    def __init__(self, inTerms):
        self.terms = inTerms
        self.length = len(inTerms)
        self.size = len(inTerms[0])
        self.used = []
        self.unused = self.terms
        self.groups = []
        self.group(self.terms)
        self.final = []

        while(True):
            temp = copy.deepcopy(self.groups)
            if (temp == self.group(self.compareOnes())):
                break

        for i in self.groups:
            for j in i:
                self.final.append(j)

        print(self.final)

    def numberOnes(self, ind, toIndex):
        count = 0
        for i in toIndex[ind]:
            if (i == "1"):
                count+=1
        return count

    def numberNonStars(self, toIndex):
        count = 0
        checker = 0
        print('this one')
        print(toIndex)

        for i in toIndex[checker]:
            if (i != "*"):
                count+=1
        return count

    def group(self, toGroup):
        self.groups.clear()
        for i in range(self.size + 1):
            self.groups.append([])
        for i in range(len(toGroup)):
            for j in range(self.size + 1):
                if (self.numberOnes(i, toGroup) == j):
                    self.groups[j].append(toGroup[i])
                    continue
        return self.groups

    def compareTerm(self, term1, term2):
        count = 0
        for i in range(self.size):
            if term1[i] == term2[i]:
                count += 1
        if count == 3:
            return True
        else:
            return False

    def compareOnes(self):
        result = []
        for i in range(len(self.groups) - 1):
            for j in self.groups[i]:
                for k in self.groups[i + 1]:
                    if self.compareTerm(j, k):
                        tempj = [z for z in j]
                        for w in range(self.size):
                            if tempj[w] != k[w]:
                                tempj[w] = "*"
                                if ''.join(tempj) not in result:
                                    result.append(''.join(tempj))
        return result


def termsToBinary(minterms, numberOfLiterals):
    print([("{0:0" + str(numberOfLiterals) + "b}").format(i) for i in minterms])
    return [("{0:0" + str(numberOfLiterals) + "b}").format(i) for i in minterms]

def main():
    #literals = input('how many literals per term? ')
    #raw = input('list minterms with spaces in between ')
    literals = '3'
    literals = '4'
    raw = '2 3 4 5'
    raw = '0 4 8 10 11 12 13 15'
    terms = [int(i) for i in raw.split()]
    #cline = Terms(termsToBinary(terms, literals))
    cline = Terms(termsToBinary(terms, literals))

main()
