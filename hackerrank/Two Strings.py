# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def twoStrings(s1, s2):
    for x in s1:
        if x in s2:
            return 'YES'
    return 'NO'
