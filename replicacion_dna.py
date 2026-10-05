from utilidades import comp, arn, ver


def replicar(A):
    print("\n1. REPLICACION")
    print("  Topoisomerasa y helicasa abren la doble helice; las SSB estabilizan las hebras")
    B = comp(A)
    ver("Hebra A (5'->3')", A)
    ver("Hebra B (3'->5')", B)

    lider = comp(B)
    print("  Cadena lider: primasa pone un cebador y ADN pol III sintetiza de forma continua")
    ver("Lider (5'->3')", lider)

    frag = [comp(A[i:i + 30])[::-1] for i in range(0, len(A), 30)]
    print(f"  Cadena rezagada: {len(frag)} fragmentos de Okazaki (un cebador y ADN pol III por fragmento)")
    print(f"  Ej. fragmento 1: {arn(frag[0][:5])}[ARN]+{frag[0][5:]}[ADN]")
    print("  ADN pol I quita los cebadores y ADN ligasa une los fragmentos")
    rezagada = "".join(reversed(frag))
    ver("Rezagada (5'->3')", rezagada)

    ok = lider == A and rezagada == comp(A)[::-1]
    print("  Moleculas hijas (hebra parental + nueva) identicas al original:", "OK" if ok else "ERROR")
    return lider