from logic import *

# Definir símbolos para cada acusado
# Definimos los símbolos para cada acusado y su estado de inocencia o culpabilidad
GzIno = Symbol("Gonzalez es inocente")
GzCul = Symbol("Gonzalez es culpable")

GmIno = Symbol("Gomez es inocente")
GmCul = Symbol("Gomez es culpable")

GrIno = Symbol("Gutierrez es inocente")
GrCul = Symbol("Gutierrez es culpable")

# Base de conocimiento: una persona no puede ser inocente y culpable a la vez 
# y al menos uno de ellos debe ser culpable.


knowledge = And(
    Or(GzIno, GzCul),
    Not(And(GzIno, GzCul)),

    Or(GmIno, GmCul),
    Not(And(GmIno, GmCul)),

    Or(GrIno, GrCul),
    Not(And(GrIno, GrCul))
)

# Declaraciones
#
# Gonzalez: "Gomez es culpable y Gutierrez es inocente."
knowledge = And(knowledge,
    Implication(GzIno, And(GmCul, GrIno)),
    Implication(GzCul, Not(And(GmCul, GrIno)))
)

# Gomez: "Gonzalez es culpable solo si Gutierrez también lo es."
knowledge = And(knowledge,
    Implication(GmIno, Implication(GzCul, GrCul)),
    Implication(GmCul, Not(Implication(GzCul, GrCul)))
)

# Gutierrez: "Yo soy inocente, pero al menos uno de los otros es culpable."
knowledge = And(knowledge,
    Implication(GrIno, And(GrIno, Or(GzCul, GmCul))),
    Implication(GrCul, Not(And(GrIno, Or(GzCul, GmCul))))
)

# Verificación de modelos
#es la estructura que verifica si un modelo cumple con las cláusulas de conocimiento
def main():
    symbols = [GzIno, GzCul, GmIno, GmCul, GrIno, GrCul]

    print("Resultado del caso de fraude fiscal:")
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"    {symbol}")

# Este código es un ejemplo de cómo se puede usar la lógica proposicional para resolver un caso de fraude fiscal.
# y determinar la culpabilidad de los acusados basándose en sus declaraciones.
#llama a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
