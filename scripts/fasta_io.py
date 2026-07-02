"""
fasta_io.py
-----------
Reading and writing FASTA files using BioPython's SeqRecord and SeqIO.

FASTA is the standard file format for storing biological sequences.
This script shows how to:
1. Build a SeqRecord (a sequence + its metadata: id, description, etc.)
2. Write it to a .fasta file
3. Read it back and print its contents

Author: Al_amin
"""

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def write_fasta(filename: str) -> None:
    """Create a SeqRecord and write it out as a FASTA file."""
    record = SeqRecord(
        Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"),
        id="example_001",
        description="Toy sequence for practicing FASTA I/O"
    )
    SeqIO.write(record, filename, "fasta")
    print(f"Wrote FASTA file: {filename}")


def read_fasta(filename: str) -> None:
    """Read a FASTA file and print each record's details."""
    for record in SeqIO.parse(filename, "fasta"):
        print(f"ID:          {record.id}")
        print(f"Description: {record.description}")
        print(f"Sequence:    {record.seq}")
        print(f"Length:      {len(record.seq)} bp")


if __name__ == "__main__":
    fasta_file = "example.fasta"
    write_fasta(fasta_file)
    print("\n--- Reading it back ---\n")
    read_fasta(fasta_file)
