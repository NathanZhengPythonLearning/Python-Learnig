#%%
num=123
print(f'{num=:#x} {num=:#b} {num=:#o}')
print(f'{num=:#X} {num=:#%} {num=:#E}')
print(f'{num=:#E} {num=:#F} {num=:#G}')
print(f'{num=:#n} {num=:#f} {num=:#d}')
print(f'{num=!s:#s} {num=:#f} {num=:#d}')

# The '#' option is only valid for integers, and only for binary, octal, or hexadecimal output. If present, it specifies that the output will be prefixed by '0b', '0o', or '0x', respectively.

#%%
# https://docs.python.org/2/library/string.html#format-specification-mini-language
# format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
# fill        ::=  <any character>
# align       ::=  "<" | ">" | "=" | "^"
# sign        ::=  "+" | "-" | " "
# width       ::=  integer
# precision   ::=  integer
# type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
# The '#' option is only valid for integers, and only for binary, octal, or hexadecimal output. If present, it specifies that the output will be prefixed by '0b', '0o', or '0x', respectively.
# When no explicit alignment is given, preceding the width field by a zero ('0') character enables sign-aware zero-padding for numeric types. This is equivalent to a fill character of '0' with an alignment type of '='.

# https://docs.python.org/3/library/string.html
# replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
# field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
# arg_name          ::=  [identifier | digit+]
# attribute_name    ::=  identifier
# element_index     ::=  digit+ | index_string
# index_string      ::=  <any source character except "]"> +
# conversion        ::=  "r" | "s" | "a"
# format_spec       ::=  <described in the next section>

# !r (repr), !s (str) and !a (ascii)

#%%
a=-1234567890.0947 # width=1+10+1+4, precision=4
print(f'{a=}')
print(f'{a=:@<+#015,.4f}')
print(f'{a=:@<+#015,.1f}')
print(f'{a=:@<+#20.4f}\n')

print(f'{a=:@>+#25,.6f}')
print(f'{a=:@>+#025,.6f}')
print(f'{a=:@^+#025,.6f}')
print(f'{a=:@=+#025,.6f}')
print(f'{a=:@=#025,.6f}')
print(f'{a=:@^#025,.6f}')
print(f'{a=:@^#025,.6f}\n')

print(f'{a=:^#025,.2f}')
print(f'{a=:<#025,.2f}')
print(f'{a=:>#025,.2f}')
# %%
