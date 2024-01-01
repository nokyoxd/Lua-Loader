def rewrite_library(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    # Remove the spacing and reformat it
    content = content.replace('\n', ' ').replace('    ', ' ')
    rewritten_multi_line = f"local lib = (function() {content} end)()"

    with open(output_file, 'w') as f:
        f.write(f"{rewritten_multi_line}")

# Files
input_file = 'input.lua'  
output_file = 'output.lua'  

rewrite_library(input_file, output_file)
