RealFrequency=[8.2, 1.5, 2.8, 4.3, 12.7,
   2.2, 2.0, 6.1 ,7, 2, 8, 4,
   2.4, 6.7, 7.5, 1.9, 0.1, 6.0,
   6.3, 9.1, 2.8, 1, 2.3, 0.1, 2, 0.1]

def shift(l, n):
    t=list(l[n:] + l[:n])
    return t

encoded = '''ohwphehfdswxuhgohwphehsxwwrghdwkldpfrqwhqwliwkdwvwkhzdbbrxzdqwlwloovdbwkholjkwry
huwkhuhlvqwpruqlqjloovdblwvwkhuhiohfwlrqriwkhprrqloovdbwkdwvrxqglvqwwkhodunulqjl
qjlqwkhvnblzdqwwrvwdbpruhwkdqlzdqwwrjrfrphghdwkdqgzhofrphmxolhwzdqwvlwwklvzdbkrz
duhbrxpboryhohwvwdonlwvqrwgdboljkwu'''

alfaString = 'abcdefghijklmnopqrstuvwxyz'
