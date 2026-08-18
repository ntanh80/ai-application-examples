import csv
import sys
from pathlib import Path

CSV_COLUMNS = ["MSSV", "HoTen", "DiemGK", "DiemCK"]


def read_students_from_csv(csv_path):
    """Read student records from a CSV file."""
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    students = []
    with csv_path.open(newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        if reader.fieldnames is None:
            raise ValueError("CSV file has no header row.")

        missing_columns = [col for col in CSV_COLUMNS if col not in reader.fieldnames]
        if missing_columns:
            raise ValueError(f"CSV is missing required columns: {', '.join(missing_columns)}")

        for row in reader:
            try:
                diem_gk = float(row.get("DiemGK", "0").strip() or 0)
                diem_ck = float(row.get("DiemCK", "0").strip() or 0)
            except ValueError:
                continue

            students.append({
                "MSSV": row.get("MSSV", "").strip(),
                "HoTen": row.get("HoTen", "").strip(),
                "DiemGK": diem_gk,
                "DiemCK": diem_ck,
                "DiemTB": round((diem_gk + diem_ck) / 2.0, 2),
            })

    return students


def get_students_with_average_at_least(students, threshold=5.0):
    """Return students whose average score is at least the threshold."""
    return [student for student in students if student["DiemTB"] >= threshold]


def print_students(students):
    """Print student records in a simple table format."""
    if not students:
        print("No students found with average >= 5.0.")
        return

    print(f"{'MSSV':<12}{'HoTen':<30}{'DiemGK':>8}{'DiemCK':>8}{'DiemTB':>8}")
    print("-" * 66)
    for student in students:
        print(f"{student['MSSV']:<12}{student['HoTen']:<30}{student['DiemGK']:>8.2f}{student['DiemCK']:>8.2f}{student['DiemTB']:>8.2f}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python Sinh code tu comment.py <path_to_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    try:
        students = read_students_from_csv(csv_path)
        passed_students = get_students_with_average_at_least(students, threshold=5.0)
        print_students(passed_students)
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
