block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "paragraph_code"
block_type_quote = "paragraph_quote"
block_type_unordered_list = "paragraph_unordered"
block_type_ordered_list = "paragraph_ordered"


def markdown_to_blocks(markdown):
    split_lines = markdown.split("\n\n")
    blocks = []
    for line in split_lines:
        if line == "":
            continue
        line = line.strip()
        blocks.append(line)
    return blocks


def block_to_block_types(markdown):
    for i in range(0, 6):  # Is it a heading?
        if markdown[i] == "#":
            continue
        elif markdown[i] == " ":
            return block_type_heading  # not returning the heading level atm. Should I?
        else:
            break

    if markdown.find('```') == 0 and markdown.find('```', 3) == len(markdown)-3:
        return block_type_code

    split_markdown = markdown.split('\n')

    if markdown.startswith("> "):
        for line in split_markdown:
            if not line.startswith("> "):
                return block_type_paragraph
        return block_type_quote

    if markdown.startswith("* "):
        for line in split_markdown:
            if line[0] != '*':
                return block_type_paragraph
        return block_type_unordered_list

    if markdown.startswith("- "):
        for line in split_markdown:
            if line[0] != '-':
                return block_type_paragraph
        return block_type_unordered_list

    if markdown.startswith("1. "):
        list_val = 1
        for line in split_markdown:
            if line.find(f"{list_val}. ") != 0:
                return block_type_paragraph
            list_val += 1
        return block_type_ordered_list

    return block_type_paragraph
