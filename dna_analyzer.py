
def read_fasta(file_path):
    """Read one DNA sequence from a FASTA file."""

    header = None
    sequence_parts = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            # Ignore empty lines
            if not line:
                continue

            # A line starting with > is the FASTA header
            if line.startswith(">"):
                if header is not None:
                    raise ValueError(
                        "This version supports one FASTA sequence only."
                    )

                header = line[1:].strip()

                if not header:
                    raise ValueError("FASTA header is empty.")

            else:
                if header is None:
                    raise ValueError(
                        "DNA sequence found before the FASTA header."
                    )

                sequence_parts.append(line)

    if header is None:
        raise ValueError("No FASTA header found.")

    sequence = "".join(sequence_parts).upper()

    if not sequence:
        raise ValueError("No DNA sequence found in the file.")

    return header, sequence


def analyze_sequence(sequence):
    """Analyse a DNA sequence."""

    # Clean the sequence
    sequence = "".join(sequence.split()).upper()

    # Valid DNA bases
    valid_bases = set("ATGC")

    if not sequence:
        print("Error: No DNA sequence entered.")
        return

    if not set(sequence).issubset(valid_bases):
        print("Error: Invalid DNA sequence.")
        print("Only A, T, G and C are allowed.")
        return

    print("\nValid DNA sequence!")

    # Calculate sequence length
    length = len(sequence)
    print("DNA sequence:", sequence)
    print("Sequence length:", length)

    # Count each base
    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    print("\nNucleotide counts:")
    print("A:", a_count)
    print("T:", t_count)
    print("G:", g_count)
    print("C:", c_count)

    # Calculate GC and AT content
    gc_content = ((g_count + c_count) / length) * 100
    at_content = ((a_count + t_count) / length) * 100

    print("\nGC content:", round(gc_content, 2), "%")
    print("AT content:", round(at_content, 2), "%")

    # Generate complement
    complement_table = str.maketrans("ATGC", "TACG")
    complement = sequence.translate(complement_table)

    print("Complement:", complement)

    # Reverse the sequence
    reverse_sequence = sequence[::-1]
    print("Reverse sequence:", reverse_sequence)

    # Generate reverse complement
    reverse_complement = complement[::-1]
    print("Reverse complement:", reverse_complement)

    # DNA to RNA transcription
    rna_sequence = sequence.replace("T", "U")
    print("RNA sequence:", rna_sequence)


# Main program
print("DNA Sequence Analysis")
print("1. Enter DNA sequence manually")
print("2. Read DNA sequence from FASTA file")

choice = input("Choose option 1 or 2: ").strip()

try:
    if choice == "1":
        sequence = input("Enter a DNA sequence: ")
        analyze_sequence(sequence)

    elif choice == "2":
        file_path = "data/sample.fasta"
        header, sequence = read_fasta(file_path)

        print("FASTA header:", header)
        analyze_sequence(sequence)

    else:
        print("Invalid choice. Please choose 1 or 2.")

except (OSError, ValueError) as error:
    print("Error:", error)
