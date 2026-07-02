# BioPython Journey 🧬

A hands-on learning project applying Python and BioPython to real molecular biology questions — bridging my background in molecular biology and stem cell research with practical bioinformatics/programming skills.

## About Me

I'm a Research Assistant at the University of Helsinki's Department of Skin and Dermatology. My work connects to the **APECED project** and the **AIRE gene**, which motivated me to learn BioPython for hands-on sequence analysis rather than treating programming as an abstract skill.

## What's in this repo

| Script | What it covers |
|---|---|
| [`scripts/dna_operations.py`](scripts/dna_operations.py) | Core molecular biology operations with `Seq` objects: complement, reverse complement, transcription (DNA → RNA), and translation (RNA → Protein) |
| [`scripts/fasta_io.py`](scripts/fasta_io.py) | Reading and writing FASTA files using `SeqRecord` and `SeqIO` — the standard format for storing and sharing biological sequences |
| [`scripts/ncbi_aire_search.py`](scripts/ncbi_aire_search.py) | Querying NCBI's Entrez database for the human **AIRE gene**, tying the learning directly to my research context |

## Skills demonstrated

- Python fundamentals (variables, strings, functions)
- BioPython `Seq`, `SeqRecord`, and `SeqIO` objects
- DNA → RNA → Protein workflows (the central dogma, in code)
- FASTA file parsing and generation
- Querying NCBI databases programmatically via Entrez

## Roadmap

- [x] DNA/RNA/protein operations
- [x] FASTA file read/write
- [x] NCBI Entrez search for AIRE gene records
- [ ] Fetch and parse full AIRE gene sequence data (`Entrez.efetch`)
- [ ] Sequence alignment and comparison
- [ ] Basic variant/mutation analysis relevant to APECED research

## Why this matters

This isn't just a coding exercise — it's the beginning of building tools I can use directly in dermatology/autoimmunity research, and a foundation for growing into bioinformatics and computational biology more broadly.

---
*Learning in progress — this repo is updated as I complete new modules.*
