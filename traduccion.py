from Bio.Seq import Seq
from utilidades import CODONES


def traducir(arnm):
    print("\n3. TRADUCCION")
    i = arnm.find("AUG")
    if i < 0:
        return print("  No hay codon de inicio AUG.")
    print(f"  Ribosoma inicia en el AUG (posicion {i}); los ARNt aportan los aminoacidos")

    codones, prot, parada = [], "", None
    for j in range(i, len(arnm) - 2, 3):
        c = arnm[j:j + 3]
        aa = CODONES[c.replace("U", "T")]
        if aa == "*":
            parada = c
            break
        codones.append(c)
        prot += aa
    print("  Codones:     " + " ".join(codones[:8]) + " ...")
    print("  Aminoacidos: " + " ".join(f"{a:<3}" for a in prot[:8]) + " ...")
    print(f"  Parada: {parada}" if parada else "  (sin codon de parada)")
    print(f"\n  Proteina ({len(prot)} aminoacidos):")
    for k in range(0, len(prot), 60):
        print("  " + prot[k:k + 60])

    tramo = arnm[i:]
    tramo = tramo[:len(tramo) - len(tramo) % 3]
    referencia = str(Seq(tramo).translate(to_stop=True))
    print(f"\n  Validacion con Biopython (Seq.translate): {'OK, coincide' if referencia == prot else 'DIFERENTE'}")
    return prot