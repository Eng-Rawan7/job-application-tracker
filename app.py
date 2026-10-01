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

    job = {
        "company": company,
        "position": position,
        "status": status
    }

    jobs.append(job)
    print("Job application added successfully!")

    jobs.append(job)
    print("Job application added successfully!")


def view_jobs():
    if not jobs:
        print("No job applications yet.")
        return

    print("\nJob Applications:")

    for i, job in enumerate(jobs, start=1):
       print(f"{i}. {job['company']} - {job['position']} - {job['status']}")

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