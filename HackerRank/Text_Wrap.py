import textwrap

def wrap(string, max_width):
    
    wrapped_texts = textwrap.wrap(string, max_width)
    sentence = '\n'.join(wrapped_texts)
    return sentence

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)