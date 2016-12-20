
questions = open('data/parsed_questions.txt').read()
questions = questions.splitlines()
questions_only = list(filter(lambda x: x.endswith('?'), questions))
questions_only

import pymarkovchain
mc = pymarkovchain.MarkovChain()
mc.generateDatabase('\n'.join(questions_only))
mc.generateString()
