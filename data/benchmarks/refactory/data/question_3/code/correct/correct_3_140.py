def remove_extras(lst):
  output = []
  for i in lst:
    if i not in output:
      output.append(i)
  return output
