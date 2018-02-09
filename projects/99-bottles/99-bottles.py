"""99 Bottles

From: https://github.com/jorgegonzalez/beginner-projects#99-bottles
Python Version: Python 2.7.12
"""

def beerCountdown():
  """Print several lines of beer countdowns"""
  for i in range(99, -1, -1):
    if i > 2:
      print('{0} bottles of beer on the wall, {0} bottles of beer.'.format(i))
      print('Take one down and pass it around, ' + str(i-1) + ' bottles of beer on the wall.')
    elif i == 2:
      print('{0} bottles of beer on the wall, {0} bottles of beer.'.format(i))
      print('Take one down and pass it around, ' + str(i-1) + ' bottle of beer on the wall.')
    elif i == 1:
      print('1 bottle of beer on the wall, 1 bottle of beer.')
      print('Take one down and pass it around, no more bottles of beer on the wall.')
    elif i == 0:
      print('No more bottles of beer on the wall, no more bottles of beer.')
      print('Go to the store and buy some more, 99 bottles of beer on the wall.')
    else :
      print('I think you have a drinking problem')

    print(''); # Empty line for readability

beerCountdown()
