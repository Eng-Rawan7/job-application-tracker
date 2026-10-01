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

def update_status():
    cursor.execute("SELECT id, company, position, status FROM jobs")
    jobs_from_db = cursor.fetchall()

    if not jobs_from_db:
        print("No job applications yet.")
        return

    print("\nJob Applications:")

    for job in jobs_from_db:
        print(f"{job[0]}. {job[1]} - {job[2]} - {job[3]}")

    job_id = input("\nEnter the job ID to update: ")

    print("\nChoose new status:")
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

    new_status = statuses.get(status_choice)

    if new_status is None:
        print("Invalid status.")
        return

    cursor.execute(
        "UPDATE jobs SET status = ? WHERE id = ?",
        (new_status, job_id)
    )

    conn.commit()

    print("Application status updated successfully!")

def delete_job():
    cursor.execute("SELECT id, company, position, status FROM jobs")
    jobs_from_db = cursor.fetchall()

    if not jobs_from_db:
        print("No job applications yet.")
        return

    print("\nJob Applications:")

    for job in jobs_from_db:
        print(f"{job[0]}. {job[1]} - {job[2]} - {job[3]}")

    job_id = input("\nEnter the job ID to delete: ")

    cursor.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()

    print("Job application deleted successfully!")

def search_jobs():
    search_term = input("Enter company or position: ")

    cursor.execute(
        "SELECT id, company, position, status FROM jobs WHERE company LIKE ? OR position LIKE ?",
        (f"%{search_term}%", f"%{search_term}%")
    )

    jobs_found = cursor.fetchall()

    if not jobs_found:
        print("No matching job applications found.")
        return

    print("\nSearch Results:")

    for job in jobs_found:
        print(f"{job[0]}. {job[1]} - {job[2]} - {job[3]}")

while True:
    print("\n=== Job Application Tracker ===")
    print("1. Add Job Application")
    print("2. View Job Applications")
    print("3. Update Application Status")
    print("4. Delete Job Application")
    print("5. Search Job Applications")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_job()
    elif choice == "2":
        view_jobs()
    elif choice == "3":
        update_status()
    elif choice == "4":
        delete_job()
    elif choice == "5":
        search_jobs()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")