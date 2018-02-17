"""Magic 8 Ball

From: https://github.com/jorgegonzalez/beginner-projects#magic-8-ball
Python Version: Python 2.7.12
"""

from time import sleep
from random import randint

def answerQuestion():
  """Print out a random answer to any question"""
  answers = [
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    'Reply hazy try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'
  ]

  print('Hmmmm...')

  sleep(2)

  print('The Magic 8 Ball says: ' + answers[randint(0, len(answers) - 1)])

def getQuestion():
  """Lie to the user"""
  print('Connected to cloud-based Magic 8 Ball.')
  print('Type "quit" to quit.')

  while True:
    question = raw_input('What is your question?\n')

    if question == 'quit':
      break;
    else:
      answerQuestion()


getQuestion()
