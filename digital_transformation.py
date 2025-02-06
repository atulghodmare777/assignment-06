def compute_pattern_sum(x):
  """
  computes the sum of x+xx+xxx+xxxx for a given digit is x
  Args:
  x[int]: A single digit between 0 & 9
  Returns:
  int: The computed sum
  Raises:
  valueError: If the input is not a single digit (0-9)

  if not isinstance(x,int) or x<0 or x>9:
    raise value error("input must be single digit between 0 &9")

  x_str = str(x)
  total= sum(int(x_str *i) for i in range (1,5))
  return total

  try:
    result=compute_pattern_sum(3)
    print(result)
    except valueerror as e:
    print (-f "Error:{e}")
