import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys())[0])
solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])