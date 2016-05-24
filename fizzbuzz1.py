for num in xrange(1,101):
    msg = ''
    print
    if num % 3 == 0:
        msg += 'Fizz'
    if num % 5 == 0:
        msg += 'Buzz'
    print msg or num
