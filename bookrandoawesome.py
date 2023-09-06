import random





f = open('text.tex', 'w')
f.write('\\documentclass[a4paper]{article} \n\\usepackage{pdfpages} \n\\usepackage{hyperref} \n\\usepackage{float} \n\\title{Haribook} \n\\author{VProf. Dr. Harish Ravi} \n\\begin{document} \n\\maketitle \n\\includepdf[pages={')
booklen=340
a=range(booklen)
s=random.sample(a,random.randint(45,55))
print(s)

dd=str(s)
f.write(dd[1:len(dd)-1])


f.write('}]{HarishBook} \n\\includepdf[pages=-]{C19dotHR} \n\\includepdf[pages=-]{HIR10cadotHR2} \n\\includepdf[pages={')



print()
booklen=1000
a=range(booklen)
s=random.sample(a,random.randint(22,28))
print(s)
dd=str(s)
f.write(dd[1:len(dd)-1])
f.write('}]{Doc1dotHR31} \n\\end{document}')

        
f.close()

import os

os.system('pdflatex text.tex')
