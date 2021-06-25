import re

def solution(new_id):

    #except for lowercase letters, numbers, -,_,. remove all
    new_id = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    #. more than 2 times => exchange them to .
    new_id = re.sub('[\.\.]+', '.', new_id)
    # starting or ending with .  remove all 
    new_id = re.sub('^\.|\.$', '', new_id)
    # if string is empty => 'a'
    if new_id == '':
        new_id = 'a'
    # if . at the end, elements outside of range 15 remove all
    new_id = re.sub('\.$', '', new_id[:15])
    # while the length of string reaches to 3, add the last element to itself
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id