import os
import sys

from utilidades import comp
from replicacion_dna import replicar
from transcripcion import transcribir
from traduccion import traducir

RUTA = "ncbi_dataset/data/rna.fna"
EJEMPLO = "ATGGCCAAATTTGGGCCCTAAGG"

arg = sys.argv[1] if len(sys.argv) > 1 else RUTA
if os.path.isfile(arg):
    adn = ""
    for l in open(arg):                      # solo la primera secuencia del FASTA
        if l.startswith(">") and adn:
            break
        if not l.startswith(">"):
            adn += l.strip().upper()
else:
    adn = arg.upper() if len(sys.argv) > 1 else EJEMPLO
if not adn or set(adn) - set("ACGT"):
    sys.exit("La secuencia debe contener solo A, C, G y T.")

print(f"ADN de partida: {len(adn)} pb")
lider = replicar(adn)                   # ADN -> ADN
arnm = transcribir(comp(lider))         # ADN -> ARN
traducir(arnm)                          # ARN -> proteina