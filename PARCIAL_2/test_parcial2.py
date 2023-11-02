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
    # En caso de que 2 secuencias de ADN contengan 4 o mas letras iguales
    (["ATGCTA", "ATCCTC", "ATAACC", "ATTGGG", "ATCACG", "ATGGTC"], 2),
    # En caso de que el ADN no contenga secuencias de letras iguales
    (["ATCGTA", "TTAGCT", "CCCTAG", "GGATTA", "CCATGT", "CCAATT"], 0),
    # En caso de que todas las secuencias del ADN contengan 4 o mas letras iguales
    (["CCCCCC", "CCCCCC", "CCCCCC", "CCCCCC", "CCCCCC", "CCCCCC"], 6),
    # En caso de que 1 secuencia de ADN contengan 4 o mas letras iguales (la ultima letra de cada string)
    (["AAAAAT", "CTGATT", "TTTCGT", "CACAGT", "TTCACT", "ATTGAT"], 1),
    ])
def test_vertical_counting(dna, seqs_counter):
    assert funciones.vertical_counting(dna) == seqs_counter

"""

# Prueba contador de secuencias diagonales -----------------------------------------------------------------------
