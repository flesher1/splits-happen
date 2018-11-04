import re

def score_line(line):
    if not check_string(line):
        print "invalid input"
        return -1
    line = list(line)
    score = 0
    frame = 0.0

    for index, item in enumerate(line):
        if(item == "/"):
            # if spare, remove the previous score and add 10 plus next roll
            frame += .5
            score += get_value(item)
            score += get_value(line[index+1])
            score -= get_value(line[index-1])
            # prevents re-adding extra rolls
            if frame > 9:
                break
        elif(item == "X" and frame < 9):
            frame += 1
            score += get_value(item)
            # if next frame results in a spare, only add 10, else next 2 rolls
            if(line[index+2] != "/"):
                score += get_value(line[index+1])
            score += get_value(line[index+2])
        else:
            frame += .5
            score += get_value(item)

    return score

# used to convert a given role into an integer value
def get_value(item):
    if(item == "/"):
        return 10
    elif(item == "X"):
        return 10
    elif(item == "-"):
        return 0
    else:
        return int(item)

# basic input validation for valid characters
def check_string(line):
    search=re.compile(r'[^X0-9/-]').search
    return not bool(search(line))
