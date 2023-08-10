# Open the input file in read mode and the output file in write mode
with open("c_ab.rf", "r") as infile, open("c_abc.rf", "w") as outfile:
    lines = infile.readlines()

    was_n_monomer = False

    for i, line in enumerate(lines):
        # If the previous line was "N_monomer"
        if was_n_monomer:
            # Increment the current line's integer value by 1
            incremented_value = int(line.strip()) + 1
            outfile.write(f"                   {incremented_value}\n")
            was_n_monomer = False
            continue

        # Check for the "N_monomer" line
        if "N_monomer" in line:
            was_n_monomer = True

        # Write the current line as-is to the output file
        outfile.write(line)

        # After line 15, add the column of zeros
        if i == 14:
            # Number of lines with data after line 15
            data_length = len(lines) - 15

            # Add a column of zeros after each line
            for j in range(data_length):
                data_line = lines[15 + j].rstrip() + "       0.000000000\n"
                outfile.write(data_line)
            break

print("File processing completed!")
