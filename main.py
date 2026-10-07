import sys

from Bio import SeqIO
from Bio.Seq import Seq

from utilidades import comp
from replicacion_dna import replicar
from transcripcion import transcribir
from traduccion import traducir

RUTA = "ncbi_dataset/data/rna.fna"
EJEMPLO = "ATGGCCAAATTTGGGCCCTAAGG"


def cargar_secuencia(arg):
    """Lee un FASTA con Bio.SeqIO (solo el primer registro) o una secuencia directa."""
    try:
        registro = next(SeqIO.parse(arg, "fasta"))
        return str(registro.seq).upper()
    except (FileNotFoundError, StopIteration):
        return arg.upper()


arg = sys.argv[1] if len(sys.argv) > 1 else RUTA
adn = cargar_secuencia(arg) if len(sys.argv) > 1 or arg == RUTA else EJEMPLO
if not adn or set(adn) - set("ACGT"):
    sys.exit("La secuencia debe contener solo A, C, G y T.")

print(f"ADN de partida: {len(adn)} pb")
lider = replicar(adn)                   # ADN -> ADN
arnm = transcribir(comp(lider))         # ADN -> ARN
traducir(arnm)                          # ARN -> proteina