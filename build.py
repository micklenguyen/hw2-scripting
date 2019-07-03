def main():

	for page in pages:
		filename = page['filename']
		output = page['output']
		title = page['title']

		# Read content of html pages
		content = open(filename).read()
	
		# Invoke function to return finished_page (base.html with filled in content)
		finshed_page = apply_template(content, title)
		write_html(output, finshed_page)


def apply_template(content, title):

	# Read base.html and save to template
	template = open("templates/base.html").read()

	template = template.replace("{{title}}", title)

	active = '>> '
	blank = ""
	if title == 'Bio':
		template = template.replace("{{active_bio}}", active)
		template = template.replace("{{active_resume}}", blank)
		template = template.replace("{{active_about}}", blank)
	elif title == 'Resume':
		template = template.replace("{{active_resume}}", active)
		template = template.replace("{{active_bio}}", blank)
		template = template.replace("{{active_about}}", blank)
	else:
		template = template.replace("{{active_about}}", active)
		template = template.replace("{{active_bio}}", blank)
		template = template.replace("{{active_resume}}", blank)

	# Replaces string tag with content from html files
	finshed_page = template.replace("{{content}}", content)
	return finshed_page


def write_html(output, finshed_page):

	# Writes complete html files
	open(output, "w+").write(finshed_page)


# Content pages list
pages = [
	{
	"filename": "content/index.html",
	"output": "docs/index.html",
	"title": "Bio",
	},
	{
	"filename": "content/resume.html",
	"output": "docs/resume.html",
	"title": "Resume",
	},
	{
	"filename": "content/about.html",
	"output": "docs/about.html",
	"title": "About",
	},
]



if __name__ == "__main__":
	main()