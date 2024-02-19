# Regression test: https://github.com/astral-sh/ruff/issues/6895
# First we test, broadly, that various kinds of assignments are now
# rejected by the parser. e.g., `5 = 3`, `5 += 3`, `(5): int = 3`.

5 = 3

5 += 3

(5): int = 3

# Now we exhaustively test all possible cases where assignment can fail.
x or y = 42
(x := 5) = 42
x + y = 42
-x = 42
(lambda _: 1) = 42
a if b else c = 42
{"a": 5} = 42
{a} = 42
[x for x in xs] = 42
{x for x in xs} = 42
{x: x * 2 for x in xs} = 42
(x for x in xs) = 42
await x = 42
(yield x) = 42
(yield from xs) = 42
a < b < c = 42
foo() = 42

# N.B. It looks like the parser can't generate a top-level
# FormattedValue, where as the official Python AST permits
# representing a single f-string containing just a variable as a
# FormattedValue directly.
#
# Bottom line is that because of this, this test is (at present)
# duplicative with the `fstring` test. That is, in theory these tests
# could fail independently, but in practice their failure or success
# is coupled.
#
# See: https://docs.python.org/3/library/ast.html#ast.FormattedValue
f"{quux}" = 42
f"{foo} and {bar}" = 42

"foo" = 42
b"foo" = 42
123 = 42
True = 42
None = 42
... = 42
*foo() = 42
[x, foo(), y] = [42, 42, 42]
[[a, b], [[42]], d] = [[1, 2], [[3]], 4]
(x, foo(), y) = (42, 42, 42)