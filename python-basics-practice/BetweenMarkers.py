def between_markers(text,begin,end) :
    if begin in text:
        begin_index = text.find(begin) + len(begin)
    else:
        begin_index = 0
    if end in text :
        end_index = text.find(end)
    else:
        end_index = len(text)

    
    return text[begin_index:end_index]


text = "What is <hidden>value</hidden>?"
print(between_markers(text, "<hidden>", "</hidden>"))
