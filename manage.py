import utils
import sys

if len(sys.argv) <= 1:
    print('''Usage:
	Rebuild site: python manage.py build
	Create new page: python manage.py new''')
    exit(1)

print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
	print("Build was specified")
	utils.main()
elif command == "new":
	print("New page was specified")
	utils.new_file_creation()
else:
	print("Please specify ’build’ or ’new’")
	print('''Usage:
	Rebuild site: python manage.py build
	Create new page: python manage.py new''')