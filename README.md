# Práctica 1: Simulación del Dogma Central de la Biología Molecular

**Autores:** Jaime Ercilla Martín, Javier Bolivar Garcia-Izquierdo

---

## Descripción del Proyecto
Este simulador en Python modela el flujo integrado de la información genética desde el ADN hasta la síntesis de una proteína, cumpliendo con los tres procesos clave del dogma central (ADN → ADN, ADN → ARN y ARN → proteína):

1. **Replicación del ADN:** Apertura de la doble hélice (topoisomerasa, helicasa y proteínas SSB), formación de la cadena líder continua y de la cadena rezagada discontinua mediante fragmentos de Okazaki con cebadores de ARN (primasa y ADN polimerasa III). Después, la ADN polimerasa I elimina los cebadores y la ADN ligasa une los fragmentos. Al final se comprueba que las dos moléculas hijas (hebra parental + hebra nueva) son idénticas al ADN original.
2. **Transcripción:** La ARN polimerasa lee la hebra molde (3'→5') y sintetiza el ARNm (5'→3') con las reglas de complementariedad A-U, T-A, G-C y C-G.
3. **Traducción:** El ribosoma lee el ARNm en codones a partir del codón de inicio (AUG) hasta el codón de parada, usando el código genético con codones de ARN. Se muestran los primeros codones con su aminoácido, la proteína completa, y se valida el resultado comparándolo con `Bio.Seq.Seq.translate()` de Biopython.

## Estructura del proyecto

| Archivo | Contenido |
|---|---|
| `main.py` | Punto de entrada: carga la secuencia y encadena los tres procesos. |
| `main.ipynb` | Notebook con la simulación explicada paso a paso (enzimas, reglas de complementariedad) y la salida ya ejecutada. |
| `replicacion_dna.py` | Replicación: enzimas, cadena líder, fragmentos de Okazaki y comprobación de las hijas. |
| `transcripcion.py` | Transcripción de la hebra molde a ARNm. |
| `traduccion.py` | Traducción del ARNm a proteína. |
| `utilidades.py` | Código genético y funciones de complementariedad y formato de salida. |
| `ncbi_dataset/` | Datos descargados de NCBI (secuencia en `data/rna.fna`). |

## Datos Utilizados
Se ha utilizado la secuencia del ARNm del gen de la **insulina humana** (*INS*, *Homo sapiens*), obtenida de la base de datos NCBI Gene (`ncbi_dataset/data/rna.fna`, escrita con T como en el ADN), con una longitud de 465 nucleótidos. La traducción empieza en el primer AUG, tras la región 5' no traducida, y da la preproinsulina, de 110 aminoácidos.

Si el archivo contiene varias secuencias (variantes de transcrito), el programa usa solo la primera. Si no se encuentra `rna.fna`, el programa usa una secuencia de ejemplo corta (el resultado en ese caso no corresponde al gen completo).

## Dependencias
Solo se usa [Biopython](https://biopython.org/) (para leer el FASTA y como validación de la traducción):
```bash
pip install -r requirements.txt
```

## Ejecución
Desde la carpeta del proyecto:

```bash
python main.py
```

También se puede indicar otra secuencia, directamente o desde un archivo FASTA:

```bash
python main.py ATGGCCAAATTTGGGCCCTAAGG
python main.py mi_secuencia.fasta
```

La secuencia debe contener solo A, C, G y T.

Para ver la simulación explicada etapa por etapa, abre `main.ipynb` (requiere Jupyter: `pip install notebook`) desde la misma carpeta que los archivos `.py`.

## Simplificaciones del modelo
- Los cebadores de ARN tienen 5 nt y son complementarios al molde. Los fragmentos de Okazaki tienen un tamaño fijo de 30 nt.
- La transcripción parte directamente de la hebra molde, sin promotor ni terminador.
- La secuencia de partida es un ARNm ya procesado, por lo que no se modelan intrones ni el procesamiento del ARNm (caperuza, poliadenilación).
- La traducción termina en la preproinsulina; no se modela el corte posterior que da la insulina madura.