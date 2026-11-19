# Q4. Tuples, sets and set operations
roll_tuple = (101, 102, 103, 104, 105)
print("Roll number tuple:", roll_tuple)
print("Tuple indexing:", roll_tuple[0])
print("Tuple slicing:", roll_tuple[1:4])
print("Tuple concatenation:", roll_tuple + (106, 107))
course_a = {101, 102, 103, 104}
course_b = {103, 104, 105, 106}
print("Course A:", course_a)
print("Course B:", course_b)
print("Union:", course_a | course_b)
print("Intersection:", course_a & course_b)
print("Difference A-B:", course_a - course_b)
print("Symmetric difference:", course_a ^ course_b)
print("A subset of B:", course_a.issubset(course_b))
print("A superset of B:", course_a.issuperset(course_b))
course_a.add(110)
course_a.discard(102)
print("Course A after add/remove:", course_a)
squares_even = {n ** 2 for n in range(1, 11) if n % 2 == 0}
print("Squares of even numbers 1-10:", squares_even)
