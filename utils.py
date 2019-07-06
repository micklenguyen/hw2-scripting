def main():

	content_pages = auto_populate_content_files()

	for page in content_pages:
		filepath = page['filepath']
		output = page['output']
		title = page['title']

		# Read content of html pages
		content = open(filepath).read()
	
		# Invoke function to return finished_page (base.html with filled in content)
		finshed_page = apply_template(content, title, content_pages)
		write_html(output, finshed_page)



def auto_populate_content_files():

	import glob
	import os

	# Loop through files in the content/ directory and save paths as a list
	all_html_files = glob.glob("content/*.html")
	#print(all_html_files)

	# Loop through the all_html_files list, modify and extract file_name and name_only from the path
	pages = []
	for file_path in all_html_files:

		# Saving the path to a varaible (ex. content/resume.html)
		file_path = file_path

		# Removes the file path from the file name (ex. content/resume.html -> resume.html)
		file_name = os.path.basename(file_path)

		# Removes the file path from the file name (ex. content/resume.html -> resume.html)
		file_name = os.path.basename(file_path)
		#print(file_name)

		# Split the name from the file extention (ex. resume.html -> resume)
		name_only, extension = os.path.splitext(file_name)

		if name_only == 'index':
			name_only = 'bio'

		# Build a list with dicts of content information
		pages.append({
			"filepath": file_path,
			"title": name_only,
			"output": "docs/" + file_name,
			"filename": file_name
			})

	return pages



def apply_template(content, title, pages):

	from jinja2 import Template

	# Read base.html and save to template
	template_html = open("templates/base.html").read()
	new_template = Template(template_html)
	finished_page = new_template.render(
		title=title,
		content=content,
		pages=pages,
		)
	
	return finished_page



def write_html(output, finshed_page):

	# Writes complete html files
	open(output, "w+").write(finshed_page)


def write_html(output, finshed_page):

	# Writes complete html files
	open(output, "w+").write(finshed_page)


def new_file_creation():
	new_page_title = input("Please enter new page name: ")
	open('content/' + new_page_title + '.html', 'w+').write("""
	<hr class="m-0">
    <section class="resume-section p-3 p-lg-5 d-flex align-items-center" id="interests">
      <div class="w-100">
        <h2 class="mb-5">""" + new_page_title + """</h2>
        <p>Test Content</p>
      </div>

    </section>

  	</div>""")


if __name__ == "__main__":
	main()