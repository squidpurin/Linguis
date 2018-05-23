import pickle

quiz = []

pickle.dump(f, open('userlist.p', "wb"))

pickle.dump(quiz, open('Quiz.p', "wb"))
