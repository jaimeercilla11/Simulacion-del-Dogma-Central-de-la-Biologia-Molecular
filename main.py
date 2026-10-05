import os
import sys

from utilidades import comp
from replicacion_dna import replicar
from transcripcion import transcribir
from traduccion import traducir

# Uso: python main.py [secuencia | fichero.fasta]
RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ncbi_dataset", "data", "gene.fna")
EJEMPLO = "ATGGCCAAATTTGGGCCCTAAGG"

arg = sys.argv[1] if len(sys.argv) > 1 else RUTA
if os.path.isfile(arg):
    adn = "".join(l.strip().upper() for l in open(arg) if not l.startswith(">"))
else:
    adn = arg.upper() if len(sys.argv) > 1 else EJEMPLO
if not adn or set(adn) - set("ACGT"):
    sys.exit("La secuencia debe contener solo A, C, G y T.")

print(f"ADN de partida: {len(adn)} pb")
lider = replicar(adn)                   # ADN -> ADN
arnm = transcribir(comp(lider))         # ADN -> ARN
traducir(arnm)                          # ARN -> proteina