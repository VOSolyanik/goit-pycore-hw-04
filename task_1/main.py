from pathlib import Path

def total_salary(path: str) -> (int, int):
	"""
	Reads salaries from file and returns total sum and average salary
	path: str - path to file
	"""
	result = (0, 0)
	# wrapping in try-except block to handle possible exceptions
	try:
		# open file in read mode
		with open(path, 'r') as file:
			lines = file.readlines()
		# check if file is empty
		if not lines:
			raise Exception("File is empty")
		
		total_salary = 0
		# iterate over each line and split by comma
		for line in lines:
			parts = line.split(',')
			# check if line has 2 parts, one is name and other is salary
			if len(parts) != 2:
				raise Exception("File has invalid format")

			total_salary += int(parts[1])
		# calculate average salary
		avg_salary = total_salary / len(lines)
		result = (total_salary, avg_salary)
	# handle file not found exception
	except FileNotFoundError:
		print(f"File {path} not found")
	# handle all other exceptions
	except Exception as e:
		print(f"Error: {e}")
	 
	return result

def main() -> None:
	total, average = total_salary("salary_file.txt")
	print(f"Total salaries sum: {total}, Average salary: {average}")
	
if __name__ == "__main__":
	main()