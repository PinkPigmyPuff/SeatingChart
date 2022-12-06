import random
import tensorflow as tf

print("TensorFlow version:", tf.__version__)

like = []
dislike = []

# example class of 20 students
people = ["Liam", "Olivia", "Noah", "Emma", "Oliver", "Charlotte", "Elijah", "Amelia", "James", "Ava", "William",
          "Sophia", "Benjamin", "Isabella", "Lucas", "Mia", "Henry", "Evelyn", "Theodore", "Harper"]
classSize = len(people)
group1 = []
group2 = []
group3 = []
group4 = []
group5 = []


def genClass():
    print('people: ' + str(people))

    # for every student, randomly generate how many students they have opionions on, and add an empty array to like/dislike
    for i in range(0, classSize):
        print('current student' + str(people[i]))
        likeNum = random.randint(0, 5)
        dislikeNum = random.randint(0, 5)
        like.append([])
        dislike.append([])
        dupelist = people.copy()

        # for every person the student has an opionion on,
        for j in range(0, likeNum):
            likes = random.randrange(0, len(dupelist))
            # print('this student wants to sit with: ' + str(dupelist[likes]))
            like[i].append(dupelist[likes])
            dupelist.pop(likes)
            # print('like array: ' + str(like))
            # print('duplelist' + str(dupelist))

        for j in range(0, dislikeNum):
            dislikes = random.randrange(0, len(dupelist))
            dislike[i].append(dupelist[dislikes])
            dupelist.pop(dislikes)

    print('\nLike: ' + str(like))
    print('\nDislike: ' + str(dislike))


# def cost():


# def arrange():


genClass()

