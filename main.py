from stats import report
import sys

#main
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    report(sys.argv[1])


main()