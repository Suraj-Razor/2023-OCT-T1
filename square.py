#define sum_of_squares = 0
# define sum = 0
# define i = 1
sum_of_square = 0
sum = 0
# i = 1
# while is i <= 100?
  # sum_of_squares = sum_of_squares + i*1
  # sum = sum + i
  # i =  i + 1
# while i <= 100:
#   sum_of_square += i*i
#   sum += i
#   i += 1

for i in range(1,101):
  sum_of_square += i * i
  sum += i

# square_of_sum = sum * sum
#diff square_of_sum - sum_of_square
# display diff
square_of_sum = sum ** 2
diff = square_of_sum - sum_of_square
print(diff)