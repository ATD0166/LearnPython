morning_lessons = {'Java', 'Python', 'C#', 'Go', 'Rust', 'C'}
afternoon_lessons = {'C#', 'Java', 'Go', 'Rust', 'Lisp', 'C'}
afternoon_lessons_list = sorted(afternoon_lessons)

# 以下結果皆相同，但method可以輸入sequence，^不行
possible_courses = morning_lessons ^ afternoon_lessons
possible_courses = afternoon_lessons ^ morning_lessons
possible_courses = morning_lessons.symmetric_difference(afternoon_lessons)
# possible_courses = morning_lessons ^ afternoon_lessons_list
possible_courses = morning_lessons.symmetric_difference(afternoon_lessons_list)
print(possible_courses)
