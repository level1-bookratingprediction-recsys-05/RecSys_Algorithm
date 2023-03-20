def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion += (len(participant) - len(completion)) * [None] # participant와 같은 길이가 되도록 None으로 채움
    for p, c in zip(participant, completion):
        if p != c:
            return p
