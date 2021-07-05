import collections

def solution_sort(participant, completion):
    # answer = filter(lambda x: x not in completion, participant)
    
    """
    Solution 1. First, sort. Then, enumerate and find the last one.
    """
    participant.sort()
    completion.sort()
    
    for i, v in enumerate(participant):
        if i >= len(participant)-1:
            return participant[i]
        if v != completion[i]:
            return v

def solution_collections(participant, completion):
    """
    Solution 2. Use collections.Counter
    """
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer.keys())
    return list(answer.keys())[0]


def solution_zip(participant, completion):
    """
    Solution 3. Use zip()
    """
    answer = ''
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        if p!=c:
            return p

    return participant[-1]