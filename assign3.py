from operator import le
import sys
import random

# box class
class box:
    def __init__(self):
        self.string1 = None
        self.string2 = None
        self.score = None

# retrieve score of two letters from scoring matrix
def score(letter1, letter2, smatrix):
    if 'A' == letter1:
        x = 1  
    elif 'C' == letter1:
        x = 2
    elif 'G' == letter1:
        x = 3
    elif 'T' == letter1:
        x = 4
    else:
        x = 5 

    if 'A' == letter2:
        y = 1  
    elif 'C' == letter2:
        y = 2
    elif 'G' == letter2:
        y = 3
    elif 'T' == letter2:
        y = 4
    else:
        y = 5 

    score1 = smatrix[x][y]

    return score1

def sequence(smatrix, s1, s2):

    # length of dynamic programming table
    # columns
    length1 = len(s1) + 1
    # rows
    length2 = len(s2) + 1

    # initialize dyanmic programming table
    # length2 lists of length1 items
    dptable = [[box() for x in range(length1)] for y in range(length2)] 

    # rows counter
    i = 0
    #columns counter
    j = 0

    # column string name
    news1 = "-" + s1
    # row string name
    news2 = "-" + s2

    # out of bounds boolean
    outofbounds = 0

    for j in range(length1):
        #print("end")
        outofbounds = 0
        for i in range(length2):
            outofbounds = 0

            # first iteration (0,0)
            if (i) == 0 and (j) == 0:
                #print("First Iteration")

                # assign score 0
                dptable[i][j].score = 0
                # empty strings
                dptable[i][j].string1 = ""
                dptable[i][j].string2 = ""
                continue
            
            # check if i is out of bounds
            if (i - 1) == -1:
                #print("i out of bounds")

                # set out of bounds flag to 1
                outofbounds = 1
                # set score to 0
                #dptable[i][j].score = 0

                  # set score for left 
                leftiscore = int(score(news1[j], "-", smatrix))
                dptable[i][j].score = dptable[i][j-1].score + leftiscore

                # assign string values to left string values
                dptable[i][j].string1 = dptable[i][j-1].string1 + news1[j]
                dptable[i][j].string2 = dptable[i][j-1].string2 + news2[i]

                # print(dptable[i][j].string1)
                # print(dptable[i][j].string2)
                # print(dptable[i][j].score)
                
            # check if j is out of bounds
            if (j - 1) == -1:
               #print("j out of bounds")

               # set out of bounds flag to 1
               outofbounds = 1
               # set score to 0
               #dptable[i][j].score = 0

               # set score for up
               upjscore = int(score("-", news2[i], smatrix))
               dptable[i][j].score = dptable[i-1][j].score + upjscore
               
               # assign string values to up string values
               dptable[i][j].string1 = dptable[i-1][j].string1 + news1[j]
               dptable[i][j].string2 = dptable[i-1][j].string2 + news2[i]

            #    print(dptable[i][j].string1)
            #    print(dptable[i][j].string2)
            #    print(dptable[i][j].score)
               
            # if outofbounds skip calculation
            if(outofbounds == 1):
                continue

            #calculate every score with new letters (up, diagonal, left)
            uscore = int(score("-", news2[i], smatrix))
            dscore = int(score(news1[j], news2[i], smatrix))
            lscore = int(score(news1[j], "-", smatrix))

            # print("u", uscore)
            # print("d", dscore)
            # print("l", lscore)
            
            # calculate scores of previous boxes
            upscore = dptable[i-1][j].score + uscore
            diagonalscore = dptable[i-1][j-1].score + dscore
            leftscore = dptable[i][j-1].score + lscore

            # print("pu", upscore)
            # print("pd", diagonalscore)
            # print("pl", leftscore)

            # get max variable name
            var = {upscore:"up",diagonalscore:"diagonal",leftscore:"left"}
            
            # get max value
            maxscore = max(var)
            #print("maxscore", maxscore)

            # get max name (up, left, or diagonal)
            direction = var.get(max(var))
            #print("maxd", direction)

            #news2 = string y (rows)
            #news1 = stringx x (columns)

            # find max value box
            if(direction == "up"):
                #print("up")

                #case 1: up
                # update score with maxscore
                dptable[i][j].score = maxscore
                # add - (char) to string1 and string y (char) to string2 
                dptable[i][j].string1 = dptable[i-1][j].string1 + "-"
                dptable[i][j].string2 = dptable[i-1][j].string2 + news2[i]

                # print(dptable[i][j].string1)
                # print(dptable[i][j].string2)
                # print(dptable[i][j].score)
            elif(direction == "diagonal"):
                #print("diagonal")

                #case 3: diagonal
                # update score with maxscore
                dptable[i][j].score = maxscore
                # add string x (char) to string1 and string y (char) to string2
                dptable[i][j].string1 = dptable[i-1][j-1].string1 + news1[j]
                dptable[i][j].string2 = dptable[i-1][j-1].string2 + news2[i]

                # print(dptable[i][j].string1)
                # print(dptable[i][j].string2)
                # print(dptable[i][j].score)
            else:
                 #print("left")
                 
                 #case 2: left
                 # update score with maxscore
                 dptable[i][j].score = maxscore
                 # add string x (char) to string1 and - (char) to string2
                 dptable[i][j].string1 = dptable[i][j-1].string1 + news1[j]
                 dptable[i][j].string2 = dptable[i][j-1].string2 + "-"
                 
                #  print(dptable[i][j].string1)
                #  print(dptable[i][j].string2)
                #  print(dptable[i][j].score)

            #print("END OF ITERATION")

    # print(dptable[length2-1][length1-1].string1, dptable[length2-1][length1-1].string2, 
    # dptable[length2-1][length1-1].score)
    
    return dptable[length2-1][length1-1]




def main():
    # get text file command line argument
    infile = sys.argv[1]

    # open text file for reading
    txtfile = open(infile, "r")

    # read string1
    string1 = txtfile.readline().rstrip()
    # read string2
    string2 = txtfile.readline().rstrip()

    # read in scoring matrix
    smatrix = []
    for x in txtfile:
        lines = x.rstrip("\n").split(" ")
        smatrix.append(lines)

    #print(smatrix)

    # find the correct sequence
    lastbox = sequence(smatrix, string1, string2)

    # print out contents of answer
    print("x:", " ".join(lastbox.string1)) 
    print("y:", " ".join(lastbox.string2))
    print("Score:", lastbox.score)

if __name__ == "__main__":
    main()

