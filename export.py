import scadnano as sc
import sys

def main():
    design = sc.DNADesign(helices=[], strands=[], grid=sc.square)
    return design

if __name__ == '__main__':
    print (len(sys.argv))
    if len(sys.argv) != 3:
        print("Usage: python export.py inputFileName outputFileName, results in outputFileName.json")
        
    name = sys.argv[1]

    design = main()
    origami = design.from_scadnano_file(name)
    origami.export_cadnano_v2('.', sys.argv[2])

    
