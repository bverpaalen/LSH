

def jaccard(user1=[1,2,3,4,5,6,7,8], user2=[5,6,7,8,9,10,11,12]):
    intersection = 0
    for i in range(len(user1)):
        if user1[i] in user2:
            intersection = intersection + 1

    union = list(set(user1) | set(user2))
    return round(intersection / len(union), 2)


def jaccard_sig(user1, user2):
    intersection = 0
    for i in range(len(user1)):
        if user1[i] == user2[i]:
            intersection = intersection + 1

    return round(intersection / len(user1), 2)


