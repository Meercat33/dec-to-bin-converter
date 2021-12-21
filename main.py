def binary(number):
  digit = number % 2
  return str(digit)

def run():  #recursive run func
  nums = []
  try:
    num = int(input("What number would you like to convert? "))
    while num > 0:
      nums.append(binary(num))
      num//=2
    length = ''.join(nums)
    stringlength=len(length)
    reversedString=length[stringlength::-1] #reverses binary number string 
    print("Your number in binary is: " + reversedString)
    print(" ")
    print(" ")
  except Exception as e:
    print(e)
  run()
run()
