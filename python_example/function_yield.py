def test(a, b):
	yield a
	yield b

r1 = test("a","b")
print(r1)
