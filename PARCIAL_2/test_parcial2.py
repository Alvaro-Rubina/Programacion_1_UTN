import pytest
import funciones

# Prueba contador de secuencias horizontales ---------------------------------------------------------------------

@pytest.mark.parametrize("dna, seqs_counter",[
    # En caso de que 2 secuencias de ADN contengan 4 o mas letras iguales
    (["AAAAAA", "CTGATG", "TTTTTT", "CACAGT", "TTCACC", "ATTGAT"], 2),
    # En caso de que el ADN no contenga secuencias de letras iguales
    (["ATCGTA", "TTAGCT", "CCCTAG", "GGATTA", "CCATGT", "CCTATT"], 0),
    # En caso de que todas las secuencias del ADN contengan 4 o mas letras iguales
    (["AAAAAA", "TTTTAG", "CCCCCC", "GGGGCA", "AAAAAA", "ACCCCG"], 6),
    # En caso de que 1 secuencia de ADN contengan 4 o mas iguales
    (["AAAAAA", "CTGATG", "TTTCGA", "CACAGT", "TTCACC", "ATTGAT"], 1),
    ])
def test_horizontal_counting(dna, seqs_counter):
    assert funciones.horizontal_counting(dna) == seqs_counter



# Prueba contador de secuencias verticales -----------------------------------------------------------------------


@pytest.mark.parametrize("dna, seqs_counter",[
    # 2 secuencias, 4 o mas letras iguales
    (["ATGCTA", "ATCCTC", "ATAACC", "ATTGGG", "ATCACG", "ATGGTC"], 2),
    # Sin secuencias de letras iguales
    (["ATCGTA", "TTAGCT", "CCCTAG", "GGATTA", "CCATGT", "CCAATT"], 0),
    # todas las secuencias, 4 o mas letras iguales
    (["CCCCCC", "CCCCCC", "CCCCCC", "CCCCCC", "CCCCCC", "CCCCCC"], 6),
    # 1 secuencia, 4 o mas letras iguales 
    (["AAAAAT", "CTGATT", "TTTCGT", "CACAGT", "TTCACT", "ATTGAT"], 1),
    ])
def test_vertical_counting(dna, seqs_counter):
    assert funciones.vertical_counting(dna) == seqs_counter



# Prueba contador de secuencias diagonales Izquierda a derecha ----------------------------------------------------
@pytest.mark.parametrize("dna, seqs_counter",[
    # 0 secs
    (["ATGACC", "GGTAAA", "CTGACT", "TTACTT", "CACTTG", "AATCAG"], 0),
    # Diagonal principal
    (["GTACGT", "TCGTAG", "TGAGGC", "CAGATT", "CAGTAG", "TTTACA"], 1),
    # 1 sec Arriba de la diagonal
    (["GGACGT", "TCGTAG", "TGAGGC", "CAGAGT", "CAGTGC", "TTTACA"], 1),
    (["GGTCGT", "TCATAG", "TGAGTC", "CAGAGT", "CAGTGC", "TTTACA"], 1),
    # 1 sec Abajo de la diagonal
    (["TACGTT", "TGTTAC", "CAGTTC", "GGACGT", "CACATC", "TTACAG"], 1),
    (["TACGTT", "AGTTAC", "CAGTTC", "GCTCGT", "CACCTC", "TTACTG"], 1),
    # 3 secs (1 de la diagonal principal y 2 abajo)
    (["ATCGTT", "AAGACC", "AAACTG", "TAAATC", "GAAATT", "ATCAGC"], 3),
    # 5 secs 
    (["AAAGTT", "AAAACC", "AAAAAG", "TAAAAA", "GAAATT", "ATCAGC"], 5),
    ])
def test_diagonal_counting(dna, seqs_counter):
    assert funciones.diagonal_counting(dna) == seqs_counter


# Prueba contador de secuencias diagonales Izquierda a derecha ----------------------------------------------------
@pytest.mark.parametrize("dna, seqs_counter",[
    (["ATCGTT", "TCCGTA", "GGCTCA", "CATTAG", "ACAATC", "GGCGTC"], 1),
    (["ATCGTT", "TCGGTA", "GGCTCA", "GATTAG", "ACAATC", "GGAGTC"], 3),
    (["ATCGTT", "TCGATA", "GGATCA", "GATCAG", "ACCATC", "GCAGTC"], 5),
    (["ACTAAG", "GCTTCC", "TTAGTA", "CGAATG", "GATTAC", "CAACTG"], 0),
    ])
def test_diagonal_counting(dna, seqs_counter):
    assert funciones.diagonal_counting(dna) == seqs_counter
