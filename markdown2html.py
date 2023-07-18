

"""
markdown2html.py

Converts a Markdown file to HTML, supporting various syntax elements.

Usage: ./markdown2html.py <input_file> <output_file>

Supported Syntax:
- Headings: Syntax: # Heading level 1
- Unordered List: Syntax: - List item
- Ordered List: Syntax: * List item
- Paragraph: Plain text

Custom Syntax:
- **Bold**: Renders as <b>Bold</b>
- __Emphasis__: Renders as <em>Emphasis</em>
- [[Text]]: Renders as MD5 hash of the text (lowercase)
- ((Text)): Removes all occurrences of the letter 'c' (case insensitive) from the text

Requirements:
- Ubuntu 18.04 LTS
- Python 3 (version 3.7 or higher)
- PEP 8 style (version 1.7.*)
- Executable files
"""

# import sys
# import os.path
# import hashlib

# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
#         sys.exit(1)

#     input_file = sys.argv[1]
#     output_file = sys.argv[2]

#     if not os.path.isfile(input_file):
#         sys.stderr.write("Missing " + input_file + "\n")
#         sys.exit(1)

#     with open(input_file, 'r') as file:
#         lines = file.readlines()

#     output_lines = []
#     inside_list = False
#     inside_paragraph = False
#     for line in lines:
#         line = line.rstrip('\n')
#         if line.startswith("#"):
#             if inside_paragraph:
#                 output_lines.append("</p>")
#                 inside_paragraph = False
#             heading_level = min(line.count("#"), 6)  # Limit heading level to 6
#             heading_text = line.strip("# ")
#             output_lines.append("<h{0}>{1}</h{0}>".format(heading_level, heading_text))
#         elif line.startswith("-"):
#             if not inside_list:
#                 if inside_paragraph:
#                     output_lines.append("</p>")
#                     inside_paragraph = False
#                 output_lines.append("<ul>")
#                 inside_list = True
#             line = "<li>" + line.strip("- ") + "</li>"
#         elif line.strip() == "":
#             if inside_list:
#                 output_lines.append("</ul>")
#                 inside_list = False
#             if inside_paragraph:
#                 output_lines.append("</p>")
#                 inside_paragraph = False
#         else:
#             if not inside_paragraph:
#                 if inside_list:
#                     output_lines.append("</ul>")
#                     inside_list = False
#                 output_lines.append("<p>")
#                 inside_paragraph = True

#             # Custom syntax replacements
#             line = line.replace("**", "<b>").replace("__", "<em>")
#             line = line.replace("**", "</b>").replace("__", "</em>")
#             line = line.replace("[[", "").replace("]]", "")
#             line = line.replace("((", "").replace("))", "").replace("c", "").replace("C", "")
#             line = line.strip()

#             # Check if the line is private
#             if "private" in line.lower():
#                 line = hashlib.md5(line.encode()).hexdigest().lower()

#             output_lines.append(line)

#     if inside_list:
#         output_lines.append("</ul>")
#     if inside_paragraph:
#         output_lines.append("</p>")

#     with open(output_file, 'w') as file:
#         file.write("\n".join(output_lines))

#     sys.exit(0)


#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import sys
import os
import re

def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    # Check that the Markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    with open(input_file, encoding="utf-8") as f:
        html_lines = []
        for line in f:
            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                html_lines.append(line.rstrip())

    # Write the HTML output to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))

if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(input_file, output_file)

    # Exit with a successful status code
    sys.exit(0)

