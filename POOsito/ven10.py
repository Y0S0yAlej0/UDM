def main():
    from matplotlib import pyplot as plt
    from matplotlib_venn import venn2

    a = {4,5,2,1}
    b = {1,7,4,6.5}

    resultado = (a-b)&(b|a)

    diagrama = venn2([a,b])

    diagrama.get_label_by_id("11").set_text(str(a&b))
    diagrama.get_label_by_id("10").set_text(str(a-b))
    diagrama.get_label_by_id("01").set_text(str(b-a))

    plt.show()

main()