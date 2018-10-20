def jaccard(user1, user2):
    intersection = 0
    for i in range(len(user1)):
        if user1[i] == user2[i]:
            intersection = intersection + 1
    return round(intersection / len(user1), 2)
