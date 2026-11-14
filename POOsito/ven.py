#PROGRAMA EN PYTHON PARA 2 CONJUNTOS
def main():
    from matplotlib import pyplot as plt          #librerias para graficar conjuntos
    from matplotlib_venn import venn2             #librerias para diagramas de Venn 2 conjuntos

    A = {1,2,3,5,7}                                #define los elementos del conjunto A
    B = {1,2,3,4}                                  #define los elementos del conjunto B

    resultado1 = (A ^ B) - (A & B)                 #conjunto problema, EJEMPLO (A⊕B)-(A∩B)
    print(f"conjunto del problema a resolver= {resultado1}")

    #DIAGRAMA DE VENN DE 2 CONJUNTOS
    NombreDiagrama = venn2([A, B], set_labels=('A', 'B'))          #dibuja el diagrama usando los conjuntos reales

    NombreDiagrama.get_label_by_id("11").set_text(str(A & B))      #región 11 = intersección A∩B
    NombreDiagrama.get_label_by_id("10").set_text(str(A - B))      #región 10 = solo A (A-B)
    NombreDiagrama.get_label_by_id("01").set_text(str(B - A))      #región 01 = solo B (B-A)

    NombreDiagrama.get_patch_by_id("11").set_color("#ffcc00")      #colorea la región 11 (el color se aplica al parche, no al texto)

    plt.show()                                                     #muestra el diagrama de Venn de 2 conjuntos A y B

main()