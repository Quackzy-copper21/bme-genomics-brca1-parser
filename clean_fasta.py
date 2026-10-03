# clean_fasta.py

'''
Rewrite the "data/real_brca1.fasta" file to contain only the first transcript and discard the rest.
'''

with open("data/real_brca1.fasta", "r") as file:
    lines = file.readlines()

# Collect lines starting from line 0 until the second header ('>') appears
single_transcript_lines = [lines[0]]
for line in lines[1:]:
    if line.startswith(">"):
        break  # Stop when transcript #2 starts
    single_transcript_lines.append(line)

# Overwrite the fasta file with only the first transcript
with open("data/real_brca1.fasta", "w") as file:
    file.writelines(single_transcript_lines)

print("data/real_brca1.fasta successfully updated to a single transcript!")