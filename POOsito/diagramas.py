#import matplotlib.pyplot as plt
#from matplotlib_venn import venn2

# venn2 recibe una tupla: (solo A, solo B, intersección A y B)
#venn2(subsets=(10, 8, 3), set_labels=('Conjunto A', 'Conjunto B'))

#plt.title("Diagrama de Venn")
#plt.show()


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Conjuntos
A = [1, 4, 3]
B = [2, 3]

# Posiciones en el eje Y para cada conjunto
pos_A = {val: i for i, val in enumerate(reversed(A))}
pos_B = {val: i for i, val in enumerate(reversed(B))}

# Ajustar altura según el conjunto más grande
alto = max(len(A), len(B))

fig, ax = plt.subplots(figsize=(6, 6))

# Coordenadas X de cada columna
x_A, x_B = 0, 3
radio = 0.25

# Dibujar nodos de A
for val, y in pos_A.items():
    y_pos = y + (alto - len(A)) / 2
    circle = plt.Circle((x_A, y_pos), radio, color='#85B7EB', ec='black', zorder=2)
    ax.add_patch(circle)
    ax.text(x_A, y_pos, str(val), ha='center', va='center', fontsize=12, zorder=3)

# Dibujar nodos de B
for val, y in pos_B.items():
    y_pos = y + (alto - len(B)) / 2
    circle = plt.Circle((x_B, y_pos), radio, color='#5DCAA5', ec='black', zorder=2)
    ax.add_patch(circle)
    ax.text(x_B, y_pos, str(val), ha='center', va='center', fontsize=12, zorder=3)

# Dibujar flechas de cada elemento de A hacia cada elemento de B
for a_val, ya in pos_A.items():
    ya_pos = ya + (alto - len(A)) / 2
    for b_val, yb in pos_B.items():
        yb_pos = yb + (alto - len(B)) / 2
        ax.annotate(
            "",
            xy=(x_B - radio, yb_pos), xytext=(x_A + radio, ya_pos),
            arrowprops=dict(arrowstyle="->", color="gray", lw=1)
        )

# Etiquetas de los conjuntos
ax.text(x_A, alto, "Conjunto A", ha='center', fontsize=13, fontweight='bold')
ax.text(x_B, alto, "Conjunto B", ha='center', fontsize=13, fontweight='bold')

ax.set_xlim(-1, 4)
ax.set_ylim(-1, alto + 1)
ax.axis('off')
ax.set_aspect('equal')

plt.title(f"Diagrama sagital de A × B\nA = {A}, B = {B}", fontsize=12)
plt.tight_layout()
plt.show()