def main():
    from matplotlib import pyplot as plt
    from matplotlib_venn import venn2

    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    resultado1 = (A - B)

    print(f"conjunto del problema a resolver= {resultado1}")

    NombreDiagrama = venn2((1, 1, 1))
    NombreDiagrama.get_label_by_id("11").set_text("conjuntoregion11")
    NombreDiagrama.get_label_by_id("10").set_text("conjuntoregion10")
    NombreDiagrama.get_label_by_id("01").set_text("conjuntoregion01")

    plt.show()  # sin argumentos

main()