def add(a, b):
  if not a or not b:
    raise Exception("Need A or B for addition")
  return a+b

def test_function():
  assert add(1,2) == 3

if __name__ == "__main__":
  a = int(input("Enter Number 1: "))
  b = int(input("Enter Number 2: "))

  sum = add()
  print(f"Sum of {a} and {b} is {sum}")