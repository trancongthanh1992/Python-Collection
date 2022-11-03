#         *            !    * Start ->  ! End
#         01234567891234    Positive Range

#         !            *    * End <-  ! Start
#         01234567891234    Negative Range
parrot = "Norwegian Blue" # 0 -> 13 => 14 elements in range.

#
print(parrot)
# 3 => w
print(parrot[3]) 
# 13 => e
print(parrot[13]) 
# IndexError: string index out of range
# print(parrot[14]) 



#         *            !    * Start ->  ! End
#         01234567891234    Positive Range
print(50 * "*" + "Positive" + 50 * "*")
print()
print(parrot[3])    # parrot[3 - 14]    => -11
print(parrot[4])    # parrot[4 - 14]    => -10
print(parrot[9])    # parrot[9 - 14]    => -5
print(parrot[3])    # parrot[3 - 14]    => -11
print(parrot[6])    # parrot[6 - 14]    => -8
print(parrot[8])    # parrot[8 - 14]    => -6


#         !            *    * End <-  ! Start
#         01234567891234    Negative Range
print(50 * "*" + "Negative" + 50 * "*")

# Formulate = positive start - length of range

print(parrot[-11])  # 3 - 14
print(parrot[-10])  # 3 - 14
print(parrot[-5])   # 3 - 14
print(parrot[-11])  # 3 - 14
print(parrot[-8])   # 3 - 14
print(parrot[-6])   # 8 - 14


print(50 * "*" + "Slice Positive" + 50 * "*")
# parrot = "Norwegian Blue" # 0 -> 13 => 14 elements in range.
# [start index : reach number of element] = swift range start index..<end index ==> not include end index.
print(parrot[:])
print(parrot[0:6])      # Norweg
print(parrot[:6])       # Norweg
print(parrot[:7-1])     # Norweg
print()

print(parrot[0:9])      # Norwegian
print(parrot[:9])       # Norwegian
print()

print(parrot[10:])      # Blue
print(parrot[11-1:])    # Blue
print()

print(parrot[:6] + parrot[6:])



# parrot = "Norwegian Blue" # 0 -> 13 => 14 elements in range.
parrot = "Norwegian Blue" # 0 -> 13 => 14 elements in range.
print(50 * "*" + "Slice Negative" + 50 * "*")

print(parrot[0:6])      # Norweg

# [start - 14 : 14] == [10 - 14 : 14]
print(parrot[-4:14])    # Blue

# [start - 14 :  14] == [10 - 14 : 12 - 14]
print(parrot[-4:-2])    # Blue

# [start - 14 :  14] == [10 - 14 : 12 - 14]
print(parrot[-4:12])    # Blue

print(parrot[-14:-8])   # Norweg
print(parrot[0:-8])     # Norweg