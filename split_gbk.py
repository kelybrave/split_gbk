import os
import sys
from Bio import SeqIO

#useage
#python split_gbk.py gbk_path

def split_gbk(input_file):
    base_name = os.path.splitext(input_file)[0]
    
    # Create output folder
    output_folder = base_name
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    # Read in GBK file using SeqIO
    records = SeqIO.parse(input_file, "genbank")
    
    scaffold_dict = {}
    for record in records:
        scaffold_id = record.id
        scaffold_dict[scaffold_id] = record
    
    for scaffold_id, record in scaffold_dict.items():
        output_file = os.path.join(output_folder, scaffold_id + ".gbk")
        SeqIO.write(record, output_file, "genbank")

split_gbk(sys.argv[1])
