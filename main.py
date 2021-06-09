import math
typical_bonds_lengths = [["C", "H", 1.09], ["C", "C", 1.54], ["C", "C", 1.34], ["C", "C", 1.20], ["C", "F", 1.33], [
    "C", "Cl", 1.77], ["C", "Br", 1.93], ["C", "I", 2.14], ["O", "H", 0.96], ["C", "O", 1.43], ["C", "O", 1.23]]


def main():
    angstrom_factor = 0.5291772492424242424242424242424242424
    inp_file_name = input("Podaj nazwę pliku .inp: ")
    with open(inp_file_name, "r") as inp_file:
        lines = inp_file.readlines()
        number_of_atoms = int(lines[0])
        lines.pop(0)
        output_list = [str(number_of_atoms), ""]
        for atom in lines:
            atom_line = atom.split()
            name_of_atom = atom_line[0]
            x = "{:.3f}".format(float(atom_line[1])*angstrom_factor)
            y = "{:.3f}".format(float(atom_line[2])*angstrom_factor)
            z = "{:.3f}".format(float(atom_line[3])*angstrom_factor)
            output_list.append(
                "".join([name_of_atom + " " + x + " " + y + " " + z]))
        with open(inp_file_name[0:-4]+".xyz", "w") as xyz_file:
            for line in output_list:
                xyz_file.write(line+"\n")
    with open(inp_file_name[0:-4]+".xyz", "r") as xyz_file:
        lines = xyz_file.readlines()
        lines.pop(0)
        lines.pop(0)
        list_of_atoms = []
        output_bonds = []
        for atom in lines:
            atom_line = atom.split()
            name_of_atom = atom_line[0]
            x = float(atom_line[1])
            y = float(atom_line[2])
            z = float(atom_line[3])
            list_of_atoms.append([name_of_atom, x, y, z])
        for first_iterator, first_atom in enumerate(list_of_atoms, start=1):
            for second_iterator, second_atom in enumerate(list_of_atoms, start=1):
                if first_iterator < second_iterator:
                    d = math.sqrt(pow((first_atom[1]-second_atom[1]),2)+pow((first_atom[2]-second_atom[2]),2)+pow((first_atom[3]-second_atom[3]),2))
                    if d != 0:
                        for bond in typical_bonds_lengths:
                            if abs(d-bond[2]) <= 0.12 and (first_atom[0] == bond[0] or first_atom[0] == bond[1]) and (second_atom[0] == bond[0] or second_atom[0] == bond[1]):
                                output_bonds.append([first_iterator,second_iterator])
                                break
                                
        with open("bonds-"+inp_file_name[0:-4]+".out", "w") as bonds_file:
            for bond in output_bonds:
                bonds_file.write("".join([str(bond[0])+" : "+str(bond[1])])+"\n")



if __name__ == "__main__":
    main()
