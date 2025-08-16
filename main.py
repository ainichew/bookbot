import sys
from stats import num_words, char_count, sort_on, sort_dict

def main(filepath):
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_words(filepath)} total words")
	print("--------- Character Count -------")
	for dict in sort_dict(filepath):
		print(f"{dict['char']}: {dict['num']}")
	print("============= END ===============")
	
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
main(sys.argv[1])
