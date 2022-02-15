import sys
from firstPackageProject.lib import generate_image
import firstPackageProject.fib


def easy_task():

    def latex_table_from_2dlist(data):
        latex_code = str()
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
res_code += easy_task() + '\n\n' + medium_task() + '\n\n'
res_code += "\\end{document}"
print(res_code)
