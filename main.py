from scipy.constants import angstrom


def main():
    inp_file_name = input("Podaj nazwę pliku .inp: ")
    with open(inp_file_name,r) as file:
        lines = file.readlines()
        number_of_atoms = lines[0]

    pass


if __name__ == "__main__":
    main()
