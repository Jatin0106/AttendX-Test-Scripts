
def test_mark_attendance():
    student_id = "23IT125"
    attendance_status = "Present"

    attendance_marked = bool(student_id) and (
        attendance_status in ["Present", "Absent"]
    )

    assert attendance_marked is True
    print("PASS: Attendance marking test")


def test_missing_student_id():
    student_id = ""
    attendance_status = "Present"

    attendance_marked = bool(student_id) and (
        attendance_status in ["Present", "Absent"]
    )

    assert attendance_marked is False
    print("PASS: Missing student ID rejected")


if __name__ == "__main__":
    test_mark_attendance()
    test_missing_student_id()
