from Bio.Seq import Seq

AA = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODONES = {a + b + c: AA[i] for i, (a, b, c) in
           enumerate((a, b, c) for a in "TCAG" for b in "TCAG" for c in "TCAG")}


def comp(s):
    """Complementaria de ADN, sin invertir (misma orientacion, para alinear hebras)."""
    return str(Seq(s).complement())


def arn(s):
    """ADN -> ARN (T -> U)."""
    return str(Seq(s).transcribe())


def ver(titulo, s):
    print(f"  {titulo:<20}{s[:60]}{'...' if len(s) > 60 else ''}")