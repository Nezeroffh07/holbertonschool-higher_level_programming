#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Tuple-lara 0 əlavə edirik ki, element sayı az olsa xəta verməsin
    t_a = tuple_a + (0, 0)
    t_b = tuple_b + (0, 0)
    
    # İlk iki elementi toplayıb yeni tuple qaytarırıq
    return (t_a[0] + t_b[0], t_a[1] + t_b[1])
