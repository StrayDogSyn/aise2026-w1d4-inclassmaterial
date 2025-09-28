from typing import Dict, List, Tuple

db = {
    "students": {
        "s1": {"name": "Ana", "major": "CS", "gpa": 3.4, "courses": ["C101", "M101"]},
        "s2": {"name": "Ben", "major": "Math", "gpa": 3.8, "courses": ["M101", "H101"]},
        "s3": {"name": "Cara", "major": "CS", "gpa": 2.9, "courses": ["C101", "W201"]},
        "s4": {"name": "Dan", "major": "Physics", "gpa": 3.5, "courses": ["P101", "M101"]},
        "s5": {"name": "Eva", "major": "CS", "gpa": 3.7, "courses": ["C101", "W201"]},
        "s6": {"name": "Fay", "major": "Math", "gpa": 3.2, "courses": ["M101", "W201"]},
        "s7": {"name": "Gus", "major": "Hum", "gpa": 3.1, "courses": ["H101", "W201"]},
        "s8": {"name": "Hana", "major": "Physics", "gpa": 3.9, "courses": ["P101", "C101"]},
    },
    "courses": {
        "C101": {"title": "Intro to CS", "credits": 4, "department": "CS"},
        "M101": {"title": "Calculus I", "credits": 4, "department": "Math"},
        "W201": {"title": "Writing", "credits": 3, "department": "Hum"},
        "P101": {"title": "Physics I", "credits": 4, "department": "Physics"},
        "H101": {"title": "History", "credits": 3, "department": "Hum"},
    },
}


def get_students_by_major(db: Dict, major: str) -> List[Tuple[str, str]]:
    """
    Return a list of (student_id, name) for students matching the major.
    Can use a list comprehension.
    """
    return []


def get_courses_by_department(db: Dict, department: str) -> Dict[str, str]:
    """
    Return a dict mapping course_id -> title for courses in a department.
    Can use a dict comprehension.
    """
    Return {}


def delete_course(db: Dict, course_id: str) -> bool:
    """
    Delete a course and remove it from all student enrollment lists.
    Can use a list comprehension to rebuild each affected enrollment list.
    """
    return False


def compute_stats(db: Dict, top_n: int = 2) -> Dict:
    """
    Compute statistics:
      total_students: int
      total_courses: int
      enrollment_by_course: Dict[course_id, count]
      avg_gpa_by_major: Dict[major, average_gpa]
      top_students: List[(student_id, gpa)] length up to top_n
    Can use comprehensions and sorting where natural.
    """
    return {}


if __name__ == "__main__":
    print(get_students_by_major(db, "CS"))
    # Expected: [('s1', 'Ana'), ('s3', 'Cara')]

    print(get_courses_by_department(db, "Math"))
    # Expected: {'M101': 'Calculus I'}

    print(delete_course(db, "M101"))
    # Expected: True

    print(sorted(db["courses"].keys()))
    # Expected: ['C101', 'W201']

    print(db["students"]["s1"]["courses"], db["students"]["s2"]["courses"], db["students"]["s3"]["courses"])
    # Expected: ['C101'] [] []

    print(compute_stats(db, top_n=2))
    # Expected: {'total_students': 3, 'total_courses': 2, 'enrollment_by_course': {'C101': 1, 'W201': 0}, 'avg_gpa_by_major': {'CS': 3.15, 'Math': 3.8}, 'top_students': [('s2', 3.8), ('s1', 3.4)]}
