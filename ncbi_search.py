from Bio import Entrez, SeqIO

# Always tell NCBI who you are
Entrez.email = "alaminbrand@gmail.com"

# Search for human AIRE gene
print("Searching NCBI database...")
search = Entrez.esearch(db="nucleotide", term="AIRE gene Homo sapiens mRNA NM_000383", retmax=5)
record = Entrez.read(search)
search.close()

# Take the first result ID
first_id = record["IdList"][0]
print("Downloading sequence ID:", first_id)

# Download the actual sequence
handle = Entrez.efetch(db="nucleotide", id=first_id, rettype="fasta", retmode="text")
sequence = SeqIO.read(handle, "fasta")
handle.close()

# Save it to your computer as a FASTA file
with open("AIRE_gene.fasta", "w") as output_file:
    SeqIO.write(sequence, output_file, "fasta")

print("AIRE gene saved to your computer!")
print("File name: AIRE_gene.fasta")
print("Length:", len(sequence.seq), "bases")