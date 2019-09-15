import pretty_print as pt
def calculate_cube(x):
     return x**3
def calculate_square(x):
     return x**2
    
def main():
  sq=calculate_square(2)
  cub=calculate_cube(4)
  pt.simple_print(sq)
  pt.pro_print(cub)
main()  