from Bio.Align import PairwiseAligner
from Bio.Seq import Seq

# Create the aligner tool
aligner = PairwiseAligner()

# Two DNA sequences to compare
# Human AIRE gene fragment
seq1 = Seq("ATGGCGGCGGCGGCGGCGGCT")

# Chimpanzee AIRE gene fragment
seq2 = Seq("ATGGCGGCGGCGGCGGCGGCC")

print("Sequence 1 (Human AIRE):    ", seq1)
print("Sequence 2 (Chimp AIRE):    ", seq2)
print()

# Perform alignment
alignments = aligner.align(seq1, seq2)

# Show the best alignment
best = next(alignments)
print("Best Alignment:")
print(best)
print("Score:", best.score)