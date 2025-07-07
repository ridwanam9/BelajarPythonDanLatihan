def is_contiguous(s, t):

    a = s.lower()
    b = t.lower()

    if b in a:
        return print("Yes")
    else:
        return print("No")
        

is_contiguous("halaman", "hal")
is_contiguous("voltage", "hal")
is_contiguous("level", "Vel")
is_contiguous("atcoder", "ace")