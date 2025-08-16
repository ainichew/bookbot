def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def num_words(filepath):
	text = get_book_text(filepath)
	words = text.split()
	return len(words) 

def char_count(filepath):
    text = get_book_text(filepath)
    lower_text = text.lower()
    dict = {}
    for char in lower_text:
       if char not in dict:
            dict[char] = 1
       else:
            dict[char] += 1
    return dict

def sort_on(items):
    return items["num"]

def sort_dict(filepath):
    dict = char_count(filepath)
    list = []
    for char, num in dict.items():
        if char.isalpha():
            list.append({"char": char, "num": num})
        else:
            pass 
        
      #list = [{"char": char, "num": num} for char, num in dict.items()]
    list.sort(reverse=True, key=sort_on)
    return list

   