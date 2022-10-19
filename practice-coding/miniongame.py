import sys

def minion_game(string):
    string = string.lower().strip()
    l = len(string)
    Kevin_score = 0
    Stuart_score = 0
    
    for i in range(l):
        if string[i] in "aeiou":
            Kevin_score += l-i
            
    if l%2 == 0:    
        Stuart_score = ((l+1)*l//2) - Kevin_score
    else:
        Stuart_score = ((l+1)*(l//2)+((l+1)/2)) - Kevin_score    
        
    if Stuart_score > Kevin_score:
        print(f"Stuart {Stuart_score}")
    elif Stuart_score < Kevin_score:
        print(f"Kevin {Kevin_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
