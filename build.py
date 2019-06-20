top = open("templates/top.html").read
bottom = open("templates/bottom.html").read
index_html = open("templates/index.html").read
resume_html = open("templates/resume.html").read
about_html = open("templates/about.html").read

index = top + index_html + bottom
resume = top + resume_html + bottom
about = top + about_html + bottom


open("docs/index.html", "w+").write(index)
open("docs/resume.html", "w+").write(resume)
open("docs/about.html", "w+").write(about)