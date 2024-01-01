def rewrite_file(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    content = content.replace('\n', ' ')

    with open(output_file, 'w') as f:
        f.write(content)

# Files
input_file = 'input.lua'  
output_file = 'output.lua'  

rewrite_file(input_file, output_file)
