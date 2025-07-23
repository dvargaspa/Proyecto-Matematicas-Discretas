from abc import ABC, abstractmethod
import itertools

# Clase base para todas las fórmulas lógicas (a operador b)
class Formula(ABC):
    @abstractmethod
    # Devuelve la fórmula en formato LaTeX
    def to_latex(self) -> str: 
        pass

    @abstractmethod
    # Evalúa la fórmula dado un diccionario de valores de verdad
    def evaluate(self, valuation: dict) -> bool:
        pass

    @abstractmethod
    # Agrupa todas las variables dentro de la fórmula
    def collect_variables(self) -> set:
        pass

    @abstractmethod
    # Agrupa las subfórmulas
    def get_subformulas(self) -> set:
        pass

class Variable(Formula):
    def __init__(self, name):
        self.name = name

    def to_latex(self):
        return self.name

    def evaluate(self, valuation):
        return valuation[self.name]

    def collect_variables(self):
        return {self.name}

    def get_subformulas(self):
        return set()

class Not(Formula):
    def __init__(self, operand):
        self.operand = operand
    # operand representa la subfórmula sobre la que se aplica el operador lógico, e.j. para ¬p, el operando almacenado es p

    def to_latex(self):
        operand_str = self.operand.to_latex() 
        if isinstance(self.operand, (And, Or, Implies, Iff)):
            return f"\\neg ({operand_str})"
        return f"\\neg {operand_str}"

    def evaluate(self, valuation):
        return not self.operand.evaluate(valuation)

    def collect_variables(self):
        return self.operand.collect_variables()

    def get_subformulas(self):
        sub = {self}
        sub.update(self.operand.get_subformulas())
        return sub

class And(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_latex(self):
        left_str = self.left.to_latex()
        right_str = self.right.to_latex()
        return f"({left_str} \\land {right_str})"

    def evaluate(self, valuation):
        return self.left.evaluate(valuation) and self.right.evaluate(valuation)

    def collect_variables(self):
        return self.left.collect_variables().union(self.right.collect_variables())

    def get_subformulas(self):
        sub = {self}
        sub.update(self.left.get_subformulas())
        sub.update(self.right.get_subformulas())
        return sub

class Or(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_latex(self):
        left_str = self.left.to_latex()
        right_str = self.right.to_latex()
        return f"({left_str} \\lor {right_str})"

    def evaluate(self, valuation):
        return self.left.evaluate(valuation) or self.right.evaluate(valuation)

    def collect_variables(self):
        return self.left.collect_variables().union(self.right.collect_variables())

    def get_subformulas(self):
        sub = {self}
        sub.update(self.left.get_subformulas())
        sub.update(self.right.get_subformulas())
        return sub

class Implies(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_latex(self):
        left_str = self.left.to_latex()
        right_str = self.right.to_latex()
        return f"({left_str} \\rightarrow {right_str})"

    def evaluate(self, valuation):
        return (not self.left.evaluate(valuation)) or self.right.evaluate(valuation)

    def collect_variables(self):
        return self.left.collect_variables().union(self.right.collect_variables())

    def get_subformulas(self):
        sub = {self}
        sub.update(self.left.get_subformulas())
        sub.update(self.right.get_subformulas())
        return sub

class Iff(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_latex(self):
        left_str = self.left.to_latex()
        right_str = self.right.to_latex()
        return f"({left_str} \\leftrightarrow {right_str})"

    def evaluate(self, valuation):
        return self.left.evaluate(valuation) == self.right.evaluate(valuation)

    def collect_variables(self):
        return self.left.collect_variables().union(self.right.collect_variables())

    def get_subformulas(self):
        sub = {self}
        sub.update(self.left.get_subformulas())
        sub.update(self.right.get_subformulas())
        return sub

# Funcion para extraer subfórmulas (a operador b)
def separate_subformulas(formula: Formula):
    subformulas = formula.get_subformulas()
    return sorted([f for f in subformulas if not isinstance(f, Variable)],
                  key=lambda f: len(f.to_latex()))

# Funcion para construir la tabla de verdad con pasos intermedios tomando la instancia Formula
def tabla_verdad(formula: Formula):
    # Extrae y ordena alfabéticamente todas las variables atómicas de la fórmula
    variables = sorted(formula.collect_variables())
    subformulas = separate_subformulas(formula)

    # Filtrar subfórmulas repetidas
    unique_subformulas = []
    used_formulas = set()
    for sub in subformulas:
        latex = sub.to_latex()
        if latex not in used_formulas:
            used_formulas.add(latex)
            unique_subformulas.append(sub)

    # Genera todas las posibles combinaciones de valores de verdad
    combinations = list(itertools.product([False, True], repeat=len(variables)))

    # Crea la primera fila con las variables y las subfórmulas
    encabezado = variables + [f.to_latex() for f in unique_subformulas]
    tabla = [encabezado]


    # Evalua cada fila de la tabla
    for combination in combinations:
        evaluate = dict(zip(variables, combination))
        fila = ["V" if evaluate[v] else "F" for v in variables]

        evaluations = []
        for sub in unique_subformulas:
            val = "V" if sub.evaluate(evaluate) else "F"
            evaluations.append(val)

        tabla.append(fila + evaluations)

    return tabla

# Funcion para convertir la tabla a LaTeX
def tabla_verdad_a_latex(tabla):
    columnas = len(tabla[0])
    latex = ["\\["]
    latex.append(f"\\begin{{array}}{{{'c|' * (columnas - 1)}c}}")
    latex.append(" \\hline")
    for fila in tabla:
        latex.append(" & ".join(fila) + r" \\")
    latex.append(" \\hline")
    latex.append("\\end{array}")
    latex.append("\\]")
    return "\n".join(latex)

# Convierte un string de texto en LaTeX a un objeto Formula
def latex_string_to_formula(s):
    s = s.strip()

    # Quitar paréntesis innecesarios
    while s.startswith('(') and s.endswith(')') and matching_parens(s):
        s = s[1:-1].strip()
        
    # Recorre los operadores lógicos en orden de prioridad (precedencia y parentesis)
    for op, cls in [("\\leftrightarrow", Iff), ("\\rightarrow", Implies), ("\\lor", Or), ("\\land", And)]:
    
            # Buscar el operador fuera de paréntesis
        op_pos = find_main_operator(s, op)
        if op_pos != -1:
            left = s[:op_pos].strip()
            right = s[op_pos + len(op):].strip()
            return cls(latex_string_to_formula(left), latex_string_to_formula(right))
    
    
    # Para la negación
    if s.startswith("\\neg"):
        return Not(latex_string_to_formula(s[4:].strip()))

    # Crea un objeto Variable 's' si nada aplica
    return Variable(s)

def find_main_operator(s, op):
    """Encuentra la posición del operador principal (fuera de paréntesis)"""
    paren_count = 0
    i = 0
    while i <= len(s) - len(op):
        if s[i] == '(':
            paren_count += 1
        elif s[i] == ')':
            paren_count -= 1
        elif paren_count == 0 and s[i:i+len(op)] == op:
            return i
        i += 1
    return -1

# Verifica si los paréntesis están correctamente cerrados
def matching_parens(s):
    count = 0
    for i, ch in enumerate(s):
        if ch == '(': count += 1
        elif ch == ')': count -= 1
        if count == 0 and i != len(s) - 1:
            return False
    return count == 0

# Funciones para transformación a Forma Normal Disyuntiva (FND)
def eliminate_implications(formula):
    if isinstance(formula, Variable):
        return formula
    elif isinstance(formula, Not):
        return Not(eliminate_implications(formula.operand))
    elif isinstance(formula, And):
        return And(eliminate_implications(formula.left), eliminate_implications(formula.right))
    elif isinstance(formula, Or):
        return Or(eliminate_implications(formula.left), eliminate_implications(formula.right))
    elif isinstance(formula, Implies):
        # A → B ≡ ¬A ∨ B
        left = eliminate_implications(formula.left)
        right = eliminate_implications(formula.right)
        return Or(Not(left), right)
    elif isinstance(formula, Iff):
        # A ↔ B ≡ (A → B) ∧ (B → A)
        left = eliminate_implications(formula.left)
        right = eliminate_implications(formula.right)
        return And(
            Or(Not(left), right),
            Or(Not(right), left)
        )
    return formula


# Mueve las negaciones recursivamente hasta que solo estén aplicadas a una sola variable
def move_negations_inward(formula):
    if isinstance(formula, Variable):
        return formula
    elif isinstance(formula, Not):
        op = formula.operand
        if isinstance(op, Variable):
            return formula
        elif isinstance(op, Not):
            # Eliminar doble negación: ¬¬A ≡ A
            return move_negations_inward(op.operand)
      # Leyes de Morgan
        elif isinstance(op, And):
            # ¬(A ∧ B) ≡ ¬A ∨ ¬B
            return Or(
                move_negations_inward(Not(op.left)),
                move_negations_inward(Not(op.right))
            )
        elif isinstance(op, Or):
            # ¬(A ∨ B) ≡ ¬A ∧ ¬B
            return And(
                move_negations_inward(Not(op.left)),
                move_negations_inward(Not(op.right))
            )
        elif isinstance(op, (Implies, Iff)):
            return Not(move_negations_inward(op))
        else:
            return formula
    elif isinstance(formula, And):
        return And(move_negations_inward(formula.left), move_negations_inward(formula.right))
    elif isinstance(formula, Or):
        return Or(move_negations_inward(formula.left), move_negations_inward(formula.right))
    return formula


# Distribuye disyunciones sobre conjunciones para obtener la FND
def distribute_or_over_and(formula):
    if isinstance(formula, Variable):
        return formula
    elif isinstance(formula, Not):
        return Not(distribute_or_over_and(formula.operand))
    elif isinstance(formula, And):
        return And(
            distribute_or_over_and(formula.left),
            distribute_or_over_and(formula.right)
        )
    elif isinstance(formula, Or):
        left = distribute_or_over_and(formula.left)
        right = distribute_or_over_and(formula.right)

        if isinstance(left, And):
            # (A ∧ B) ∨ C = (A ∨ C) ∧ (B ∨ C)
            return And(
                distribute_or_over_and(Or(left.left, right)),
                distribute_or_over_and(Or(left.right, right))
            )
        elif isinstance(right, And):
            # A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C)
            return And(
                distribute_or_over_and(Or(left, right.left)),
                distribute_or_over_and(Or(left, right.right))
            )
        else:
            return Or(left, right)
    return formula

# Aplica las 3 funciones de transformación
def to_fnd(formula):
    sin_implicaciones = eliminate_implications(formula)
    negaciones_internas = move_negations_inward(sin_implicaciones)
    return distribute_or_over_and(negaciones_internas)

# Función para simplificar la fórmula
def simplify_formula(formula):
    # Se transforma en FND
    fnd = to_fnd(formula)

    # Eliminacion de términos redundantes
    if isinstance(fnd, And) or isinstance(fnd, Or):
        # Eliminar duplicados en conjunciones/disyunciones
        if isinstance(fnd, And):
            # Si ambos lados son iguales, devolver uno
            if fnd.left.to_latex() == fnd.right.to_latex():
                return fnd.left
        elif isinstance(fnd, Or):
            if fnd.left.to_latex() == fnd.right.to_latex():
                return fnd.left

    return fnd

def main():
    print("=== Opciones de Análisis ===")
    print("1. Solo Tabla de Verdad Original")
    print("2. Solo Forma Normal Disyuntiva")
    print("3. Análisis Completo")

    opcion = input("Selecciona una opción (1/2/3): ").strip()
    expr = input("Ingresa la fórmula en formato LaTeX e.g. ((p \\rightarrow q) \\leftrightarrow (\\neg q \\lor r)): ").strip()

    formula_original = latex_string_to_formula(expr)

    if opcion == "1":
        print("\n Tabla de Verdad (Original):")
        print(tabla_verdad_a_latex(tabla_verdad(formula_original)))

    elif opcion == "2":
        formula_fnd = to_fnd(formula_original)
        print("\n Fórmula en Forma Normal Disyuntiva (FND):")
        print(formula_fnd.to_latex())

    elif opcion == "3":
        print("\n Fórmula Original:", formula_original.to_latex())
        print("\n Tabla de Verdad (Original):")
        print(tabla_verdad_a_latex(tabla_verdad(formula_original)))

        formula_fnd = to_fnd(formula_original)
        print("\n Fórmula en Forma Normal Disyuntiva (FND):")
        print(formula_fnd.to_latex())

        formula_simplificada = simplify_formula(formula_fnd)
        if formula_simplificada.to_latex() != formula_fnd.to_latex():
            print("\n Fórmula Simplificada:")
            print(formula_simplificada.to_latex())

        print("\n Tabla de Verdad (FND):")
        print(tabla_verdad_a_latex(tabla_verdad(formula_simplificada)))

    else:
        print("Opción no válida. Intenta con 1, 2 o 3.")

if __name__ == "__main__":
    main()


    
