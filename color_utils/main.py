from color_utils import lib
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",type=str, required=True, help="Path to base16 color scheme")
    args = parser.parse_args()
    
    base16 = lib.Base16(args.file)
    
    base16.print()
        
if __name__ == "__main__":
    main()