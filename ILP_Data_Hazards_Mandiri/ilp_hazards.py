from dataclasses import dataclass

@dataclass
class Instruction:
    label: str
    reads: set
    writes: set
    text: str

def find_dependencies(instructions):
    """Buat edge (instruksi sumber, tujuan, jenis hazard) dari urutan instruksi."""
    edges = []
    for i, older in enumerate(instructions):
        for newer in instructions[i + 1:]:
            for reg in sorted(older.writes & newer.reads):
                edges.append((older.label, newer.label, f"RAW ({reg})"))
            for reg in sorted(older.reads & newer.writes):
                edges.append((older.label, newer.label, f"WAR ({reg})"))
            for reg in sorted(older.writes & newer.writes):
                edges.append((older.label, newer.label, f"WAW ({reg})"))
    return edges

CASES = {
    "RAW": [
        Instruction("I1", {"R2", "R3"}, {"R1"}, "I1: ADD R1, R2, R3"),
        Instruction("I2", {"R1", "R5"}, {"R4"}, "I2: ADD R4, R1, R5"),
    ],
    "WAR": [
        Instruction("I1", {"R2", "R3"}, {"R1"}, "I1: ADD R1, R2, R3"),
        Instruction("I2", {"R4", "R5"}, {"R2"}, "I2: ADD R2, R4, R5"),
    ],
    "WAW": [
        Instruction("I1", {"R2", "R3"}, {"R1"}, "I1: ADD R1, R2, R3"),
        Instruction("I2", {"R4", "R5"}, {"R1"}, "I2: ADD R1, R4, R5"),
    ],
}

def main():
    for hazard, instructions in CASES.items():
        print("=" * 55)
        print(f"HAZARD {hazard}")
        for inst in instructions:
            print(inst.text)
        for src, dst, kind in find_dependencies(instructions):
            print(f"Dependency graph: {src} ---- {kind} ----> {dst}")
        if hazard == "RAW":
            print("Analisis: I2 membutuhkan nilai R1 yang dihasilkan I1.")
        elif hazard == "WAR":
            print("Analisis: I1 harus membaca R2 sebelum I2 menimpa R2.")
        else:
            print("Analisis: urutan penulisan R1 perlu dipertahankan.")

if __name__ == "__main__":
    main()
