def get_cats_info(path: str) -> list[dict]:
	"""
	Reads cats info from file and returns list of dictionaries
	path: str - path to file
	"""
	result = []
	# wrapping in try-except block to handle possible exceptions
	try:
		# open file in read mode
		with open(path, 'r') as file:
			lines = file.readlines()

		for line in lines:
			parts = line.split(',')
			if len(parts) != 3:
				raise Exception("File has invalid format")
			result.append({
				"id": parts[0],
				"name": parts[1],
				"age": int(parts[2])
			})
	# handle file not found exception
	except FileNotFoundError:
		print(f"File {path} not found")
	# handle all other exceptions
	except Exception as e:
		print(f"Error: {e}")
	
	return result

def main() -> None:
	cats = get_cats_info("cats_file.txt")
	print(cats)
	
if __name__ == "__main__":
	main()

