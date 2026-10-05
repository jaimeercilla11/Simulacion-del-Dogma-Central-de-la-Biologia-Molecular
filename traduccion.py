from utilidades import CODONES


def traducir(arnm):
    print("\n--- 3. TRADUCCION ---")
    i = arnm.find("AUG")
    if i < 0:
        return print("No hay codon de inicio AUG.")
    print(f"[Ribosoma] empieza en el AUG (posicion {i}); [ARNt] aporta cada aminoacido")
    prot = ""
    for j in range(i, len(arnm) - 2, 3):
        codon = arnm[j:j + 3]
        aa = CODONES[codon.replace("U", "T")]
        if len(prot) < 6 or aa == "*":
            anticodon = codon.translate(str.maketrans("ACGU", "UGCA"))
            print(f"  {codon}  anticodon {anticodon}  ->  {'STOP' if aa == '*' else aa}")
        if aa == "*":
            break
        prot += aa
    print(f"\nProteina ({len(prot)} aminoacidos):")
    for k in range(0, len(prot), 60):
        print("  " + prot[k:k + 60])