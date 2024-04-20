def get_available_commands() -> list[str]:
	"""
	Returns list of available commands
	"""
	return ["phone", "add", "change", "all"]

def get_commands_handler(contacts: dict):
	"""
	contacts: dict - contacts dictionary
	"""
	def handler(command: str, *args: list[str]) -> str:
		"""
		Handles user commands
		command: str - user command
		args: list[str] - command arguments
		"""
		match command:
			case "phone":
				if len(args) < 1:
					return "Contact name is required"
				return __get_phone(args[0], contacts)
			case "add":
				if len(args) < 2:
					return "Contact name and phone are required"
				return __add_contact(args[0], args[1], contacts)
			case "change":
				if len(args) < 2:
					return "Contact name and phone are required"
				return __change_contact(args[0], args[1], contacts)
			case "all":
				return __get_all_contacts(contacts)
			case _:
				return "Invalid command."
			
	return handler

def __get_phone(name: str, contacts: dict) -> str:
	"""
	Returns phone number for contact
	name: str - command arguments
	contacts: dict - contacts dictionary
	"""
	if name not in contacts:
		return f"Contact {name} not found"
	
	return contacts[name]

def __add_contact(name: str, phone: str, contacts: dict) -> str:
	"""
	Adds contact to contacts dictionary
	name: str - contact name
	phone: str - contact phone
	contacts: dict - contacts dictionary
	"""
	contacts[name] = phone
	return f"Contact {name} added"

def __change_contact(name: str, phone: str, contacts: dict) -> str:
	"""
	Changes contact phone
	name: str - contact name
	phone: str - new contact phone
	contacts: dict - contacts dictionary
	"""
	if name not in contacts:
		return f"Contact {name} not found"
	
	contacts[name] = phone
	return f"Contact {name} phone changed"

def __get_all_contacts(contacts: dict) -> str:
	"""
	Returns all contacts
	contacts: dict - contacts dictionary
	"""
	if not contacts:
		return "No contacts found"
	
	return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])