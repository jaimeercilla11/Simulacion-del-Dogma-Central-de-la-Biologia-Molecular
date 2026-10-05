from utilidades import comp, arn, ver


def replicar(A):
    print("\n--- 1. REPLICACION ---")
    print("[Topoisomerasa] alivia la tension; [Helicasa] abre la doble helice; [SSB] estabilizan las hebras.")
    B = comp(A)
    ver("Hebra A (5'->3')", A)
    ver("Hebra B (3'->5')", B)

    print("[Primasa] cebador + [ADN pol III] sintesis CONTINUA sobre B -> cadena LIDER")
    lider = comp(B)
    ver("Cebador ARN", arn(lider[:5]))
    ver("Cadena lider (5'->3')", lider)

    print("[Primasa] cebador por fragmento + [ADN pol III] sintesis DISCONTINUA sobre A -> REZAGADA")
    frag = [comp(A[i:i + 30])[::-1] for i in range(0, len(A), 30)]
    print(f"  {len(frag)} fragmentos de Okazaki. Fragmento 1: {arn(frag[0][:5])}[ARN]+{frag[0][5:]}[ADN]")
    print("[ADN pol I] elimina cebadores y rellena; [ADN ligasa] une los fragmentos")
    rezagada = "".join(reversed(frag))
    ver("Cadena rezagada (5'->3')", rezagada)

    ok = lider == A and rezagada == comp(A)[::-1]
    print("Hija 1 = A + rezagada | Hija 2 = B + lider -> identicas al original:", "OK" if ok else "ERROR")
    return lider