def add(a, b):
	return a + b

def mul(a, b, c):
	return a * b * c

collection = {
	"addition": add,
	"multiplication": mul
}

if __name__ == "__main__":
	func = input("Welche Funktion?")
	a = int(input("a"))
	b = int(input("b"))
	c = int(input("c"))

	print(collection[func](a, b, c))
