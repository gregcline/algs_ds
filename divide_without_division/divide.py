def find_middle(upper, lower):
    return (upper + lower) >> 1


def divide(numer, denom):
    upper = numer
    lower = 1
    middle = find_middle(upper, lower)
    possible = middle * denom
    remainder = numer - possible
    """
    while the remainder is > the denominator or remainder < 0:
      set the middle to lower + upper >> 1
      remainder = multiply the middle by the denominator and subtract it from the numerator
      if middle * denom > numer:
        set upper to middle
      elif middle * denom < numer:
        set lower to middle
      else:
        return (middle, 0)
    return (middle, remainder)
    """

    while remainder > denom or remainder < 0:
        if possible > numer:
            upper = middle
            middle = find_middle(upper, lower)
            possible = middle * denom
            remainder = numer - possible
        elif possible < numer:
            lower = middle
            middle = find_middle(upper, lower)
            possible = middle * denom
            remainder = numer - possible
        else:
            return (middle, numer - possible)

    return (middle, numer - possible)


print(divide(31, 5))
print(divide(75, 25))
print(divide(900, 72))


