import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    position TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

conn.commit()

jobs = []


def add_job():
    company = input("Company name: ")
    position = input("Job position: ")

    print("\nChoose application status:")
    print("1. Applied")
    print("2. Interview")
    print("3. Rejected")
    print("4. Accepted")

    status_choice = input("Choose a status: ")

    statuses = {
        "1": "Applied",
        "2": "Interview",
        "3": "Rejected",
        "4": "Accepted"
    }

    status = statuses.get(status_choice, "Applied")

    cursor.execute(
        "INSERT INTO jobs (company, position, status) VALUES (?, ?, ?)",
        (company, position, status)
    )

    conn.commit()

    print("Job application added successfully!")

def view_jobs():
    cursor.execute("SELECT id, company, position, status FROM jobs")
    jobs_from_db = cursor.fetchall()

    if not jobs_from_db:
        print("No job applications yet.")
        return

    print("\nJob Applications:")

    for job in jobs_from_db:
        print(f"{job[0]}. {job[1]} - {job[2]} - {job[3]}")

while True:
    print("\n=== Job Application Tracker ===")
    print("1. Add Job Application")
    print("2. View Job Applications")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_job()
    elif choice == "2":
        view_jobs()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")