import os
from firstPackageProject.lib import generate_image
import firstPackageProject.fib


def easy_task(first_task=True):
    def latex_table_from_2dlist(data):
        latex_code = str()
        if first_task:
            latex_code += "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\n\\usepackage{graphicx}\n\\graphicspath{ {" \
                          "./images/} }\n\\begin{document}\n\n"
        latex_code += '\\begin {tabular}{ '
        latex_code += 'l ' * len(data)
        latex_code += '}\n'
        for lst in data:
            for i, elem in enumerate(lst):
                if i != 0:
                    latex_code += '& '
                latex_code += str(elem) + ' '
            latex_code += '\\\\\n'
        latex_code += '\\end {tabular}'
        if first_task:
            latex_code += "\\end{document}"
        return latex_code

    return latex_table_from_2dlist([[1, 2, "123"], [3, 4, "aaa"], [4, "dafsdfas", 1], ["]qw]er]qwe]", 4432, "q"]])


def medium_task():
    generate_image(firstPackageProject.fib.__file__)
    latex_code = str()
    latex_code += "\\includegraphics{Graph.png}"

    return latex_code


res_code = str()
res_code += "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\n\\usepackage{graphicx}\n\\graphicspath{ {" \
            "./images/} }\n\\begin{document}\n\n"
res_code += easy_task(False) + '\n\n'
res_code += medium_task() + '\n\n'
res_code += "\\end{document}"

with open("latex_source.tex", "w") as f:
    f.write(res_code)

os.system('pdflatex latex_source.tex')
