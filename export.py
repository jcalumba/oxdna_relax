import scadnano as sc
import sys

def main():
    design = sc.DNADesign(helices=[], strands=[], grid=sc.square)
    return design

if __name__ == '__main__':
    print (len(sys.argv))
    if len(sys.argv) != 2:
        print("Usage: python export.py filename, results in export.json")
        
    name = sys.argv[1]

    design = main()
    origami = design.from_cadnano_v2('.', name)
    origami.export_cadnano_v2()
    design.write_scadnano_file()
    