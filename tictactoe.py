from pprint import pprint as pp

file="TTTGAMES.txt"

score=0
ttt_lines=[]
with open(file, encoding='utf-8-sig') as ttt_rawfile:
    for line in ttt_rawfile:
        ttt_lines.append(line)
print(ttt_lines)
for line in ttt_lines:
    game = line.removesuffix('\n').split(' ')
    #print(game)
    if game[1] == 'X':
        if game[0]=='A':
            score+=4
        if game[0]=='B':
            score+=1
        if game[0]=='C':
            score+=7
    elif game[1] == 'Y':
        if game[0]=='A':
            score+=8
        if game[0]=='B':
            score+=5
        if game[0]=='C':
            score+=2
    elif game[1] == 'Z':
        if game[0]=='A':
            score+=3
        if game[0]=='B':
            score+=9
        if game[0]=='C':
            score+=6
print(score)

