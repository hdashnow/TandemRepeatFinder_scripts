TandemRepeatFinder scripts
==========================
You can get TRF here: http://tandem.bu.edu/trf/trf.download.html

I'm using the Linux 64 version.

Sample Tandem Repeat Finder command:

trf my_sequence.fasta 2 7 7 80 10 6 6 -d  # This will find STRs with 1-6bp repeat units and at least 3 copies. It is a relatively low threshold, so you may want to do additional filtering.

output: my_sequence.fasta.2.7.7.80.10.6.6.dat
-d is required to produce the .dat file

Once you have .dat format you can process into txt or bed format:

TRFdat_to_txt.py
---------------
Usage: python TRFdat_to_txt.py [-h] --dat DAT --txt TXT

* Convert TRF dat file to space delimited text format
* Useful for reading into R e.g. read.table("my_sequence.fasta.2.7.7.80.10.6.6.txt", header=T, quote="\"")

Sample command:

python TRFdat_to_txt.py --dat my_sequence.fasta.2.7.7.80.10.6.6.dat --txt my_sequence.fasta.2.7.7.80.10.6.6.txt



TRFdat_to_bed.py
---------------
Usage: python TRFdat_to_bed.py [-h] --dat DAT --bed BED

* Convert TRF dat file to BED format (tab delmited genomic coordinates)
* Columns are: contig start   end repeat_motif
* Contig is the name of the sequence in the fasta record. This is often a chromsome name.

Sample command:

python TRFdat_to_bed.py --dat my_sequence.fasta.2.7.7.80.10.6.6.dat --bed my_sequence.fasta.2.7.7.80.10.6.6.bed



Note: 
Tested in Python version 2.6
