# Tuples can be used to store data but can not be changed.
our_tuple = 1,2,3,"A","B","C"
print(our_tuple)
our_tuple = (1,2,3,"A","B","C")
print(our_tuple)

A = [1, 2, 3]
A = tuple(A)
print(A)

(A, B, C,) = 1, 2, 3
print(A)
G,H,J = "789"
print(G)
print(J, H)