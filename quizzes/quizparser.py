def parseToQuizzes(fn):
    f = open(fn, "r")
    quizzes = []
    for line in f:
        line = line.strip()
        if line == '#':
            #quizzes.append(quiz)
        elif len(line) < 10:
            #quiz = Quiz(quizname)
        else:
            e = line.split('%')
            qname = e[0]
            question = e[2]
            if e[3] != 'none':
                if e[1] == 'MultipleChoice':
                    options = e[4].split(',')
                    answer = e[5]
                    #s = Question(qname, e[1], question, answer, Options(options), e[3])
                elif e[1] == 'TrueFalse':
                    options = ['True', 'False']
                    answer = e[4]
                    #s = Question(qname, e[1], question, answer, questionImage = e[3])
                else:
                    answer = e[4]
                    #s = Question(qname, e[1], question, answer, questionImage = e[3])
            else:
                if e[1] == 'MultipleChoice':
                    options = e[4].split(',')
                    answer = e[5]
                    #s = Question(qname, e[1], question, answer, Options(options))
                elif e[1] == 'TrueFalse':
                    options = ['True', 'False']
                    answer = e[4]
                    #s = Question(qname, e[1], question, answer)
                else:
                    answer = e[4]
                    #s = Question(qname, e[1], question, answer)
            #quiz.addQuestion(s)
    return quizzes

parseToQuizzes("q1.txt")
