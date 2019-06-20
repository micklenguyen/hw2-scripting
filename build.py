top = open("templates/top.html").read()
bottom = open("templates/bottom.html").read()
index_html = open("content/index.html").read()
resume_html = open("content/resume.html").read()
about_html = open("content/about.html").read()

index = top + index_html + bottom
resume = top + resume_html + bottom
about = top + about_html + bottom


open("docs/index.html", "w+").write(index)
open("docs/resume.html", "w+").write(resume)
open("docs/about.html", "w+").write(about)