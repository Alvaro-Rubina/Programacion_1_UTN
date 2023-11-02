import pytest
import funciones

# Prueba contador de secuencias horizontales ---------------------------------------------------------------------
"""
@pytest.mark.parametrize("dna, seqs_counter",[
    # En caso de que 2 secuencias de ADN contengan 4 o mas letras iguales
    (["AAAAAA", "CTGATG", "TTTTTT", "CACAGT", "TTCACC", "ATTGAT"], 2),
    # En caso de que el ADN no contenga secuencias de letras iguales
    (["ATCGTA", "TTAGCT", "CCCTAG", "GGATTA", "CCATGT", "CCTATT"], 0),
    # En caso de que todas las secuencias del ADN contengan 4 o mas letras iguales
    (["AAAAAA", "TTTTAG", "CCCCCC", "GGGGCA", "AAAAAA", "CCCCTG"], 6),
    # En caso de que 1 secuencia de ADN contengan 4 o mas iguales
    (["AAAAAA", "CTGATG", "TTTCGA", "CACAGT", "TTCACC", "ATTGAT"], 1),
    ])
def test_horizontal_counting(dna, seqs_counter):
    assert funciones.horizontal_counting(dna) == seqs_counter

"""

# Prueba contador de secuencias verticales -----------------------------------------------------------------------

"""
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

"""

# Prueba contador de secuencias diagonales -----------------------------------------------------------------------

@pytest.mark.parametrize("dna, seqs_counter",[
    (["ATGCGA", "CAGTTC", "TTATAT", "AGAAGG", "CCCCAA", "TCACTG"], 1),
    (["ATCGAT", "ATCGAT", "ATCGAT", "ATCGAT", "ATCGAT", "ATCGAT"], 0),
    (["ACGATT", "TACCGA", "CTATGC", "TCTAGG", "CGCTAT", "CACAGC"], 2),
    (["ACATGA", "TACACT", "GTACAG", "AGTACA", "TTGTGT", "CCAGTA"], 5)
    ])
def test_diagonal_counting(dna, seqs_counter):
    assert funciones.diagonal_counting(dna) == seqs_counter

