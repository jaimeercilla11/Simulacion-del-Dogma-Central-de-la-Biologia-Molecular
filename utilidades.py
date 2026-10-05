# Codigo genetico (orden de bases T, C, A, G)
AA = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODONES = {a + b + c: AA[i] for i, (a, b, c) in
           enumerate((a, b, c) for a in "TCAG" for b in "TCAG" for c in "TCAG")}


def comp(s):
    return s.translate(str.maketrans("ACGT", "TGCA"))


def arn(s):
    return s.replace("T", "U")


def ver(titulo, s):
    print(f"  {titulo:<24}{s[:60]}{'...' if len(s) > 60 else ''}")