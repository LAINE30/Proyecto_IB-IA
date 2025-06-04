# 🔍 Proyecto 2 - Rompecabezas Lógico usando Lógica Proposicional

## 📅 Fecha de entrega: 4 de junio de 2025  
## 👥 Integrantes del grupo:
- Jonathan 
- Wellington 
- Josue 
- Liam 
- Mateo 

---

## 🧠 Descripción del Proyecto

Este proyecto tiene como objetivo implementar un sistema de resolución de rompecabezas mediante **lógica proposicional**. El sistema determina quién entre tres sospechosos (Alice, Bob, Charlie) es culpable de dopaje, usando las declaraciones dadas por cada uno. Se sabe que **una afirmación es falsa y dos son verdaderas**.

---

## 🔧 Herramientas utilizadas

- Lenguaje: **Python 3.x**
- Librería de lógica: `sympy.logic.boolalg` *(se eligió esta para obtener un bono adicional)*
- Opcional: `matplotlib`, `numpy`, `pandas` para visualización y análisis (no necesarios para el problema base)

---

## 🧩 Problema Propuesto

### ❓ ¿Quién es culpable de dopaje?

Sospechosos:
- Alice
- Bob
- Charlie

Declaraciones:
- **Alice**: "Bob o Charlie tomaron drogas, pero no ambos."
- **Bob**: "Alice o Charlie tomaron drogas, pero no ambos."
- **Charlie**: "Alice o Bob tomaron drogas, pero no ambos."

**Nota:** Se sabe que 2 afirmaciones son verdaderas y 1 es falsa. El sistema determina quién es culpable bajo esta restricción.

---

## 💡 Metodología

1. Se formularon las proposiciones lógicas correspondientes a cada afirmación.
2. Se utilizaron conectores lógicos (`Or`, `And`, `Not`, `Xor`) para modelar las oraciones.
3. Se generaron combinaciones posibles de culpabilidad y se evaluaron bajo la condición: "2 verdaderas, 1 falsa".
4. Se filtró la combinación que cumplía con las reglas para obtener la solución final.

---

## 📂 Estructura del Proyecto


---

## ▶️ Ejecución

Para ejecutar el proyecto:

```bash
python3 main.py

pip install sympy
