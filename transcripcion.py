from utilidades import comp, arn, ver


def transcribir(molde):
    print("\n--- 2. TRANSCRIPCION ---")
    print("[ARN polimerasa] lee el molde 3'->5' y sintetiza el ARNm 5'->3' (A-U, T-A, G-C, C-G)")
    arnm = arn(comp(molde))
    ver("Molde ADN (3'->5')", molde)
    ver("ARNm (5'->3')", arnm)
    return arnm