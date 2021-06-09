
def main():
    angstrom_factor = 0.5291772492424242424242424242424242424
    inp_file_name = input("Podaj nazwę pliku .inp: ")
    with open(inp_file_name) as inp_file:
        lines = inp_file.readlines()
        number_of_atoms = int(lines[0])
        lines.pop(0)
        output_list = [str(number_of_atoms),""]
        for atom in lines:
            atom_line = atom.split()
            name_of_atom = atom_line[0]
            x = "{:.3f}".format(float(atom_line[1])*angstrom_factor)
            y = "{:.3f}".format(float(atom_line[2])*angstrom_factor)
            z = "{:.3f}".format(float(atom_line[3])*angstrom_factor)
            output_list.append("".join([name_of_atom + " " + x + " " + y +" " + z]))
        with open(inp_file_name[0:-4]+".xyz","w") as xyz_file:
            for line in output_list:
                xyz_file.write(line+"\n")
            



if __name__ == "__main__":
    main()
