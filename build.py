def main(filename, output, title):

	# Read content of html pages
	content = open(filename).read()

	# Invoke function to return finished_page (base.html with filled in content)
	finshed_page = apply_template(content, title)
	write_html(output, finshed_page)


def apply_template(content, title):

	# Read base.html and save to template
	template = open("templates/base.html").read()

	template = template.replace("{{title}}", title)
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

	# for loop to loop through content on list and use variables to invoke main()
	for page in pages:
		filename = page['filename']
		output = page['output']
		title = page['title']

		main(filename, output, title)