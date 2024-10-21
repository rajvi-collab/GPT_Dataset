jobs = {}
applications = {}


def add_job(job_id, title, description, location, salary):
    jobs[job_id] = {
        'title': title,
        'description': description,
        'location': location,
        'salary': salary
    }

def list_jobs():
    for job_id, job in jobs.items():
        print(f"Job ID: {job_id}")
        print(f"Title: {job['title']}")
        print(f"Description: {job['description']}")
        print(f"Location: {job['location']}")
        print(f"Salary: {job['salary']}")
        print("-" * 20)


def apply_for_job(job_id, applicant_name, resume, cover_letter):
    if job_id not in jobs:
        print("Job ID not found.")
        return

    if job_id not in applications:
        applications[job_id] = []

    applications[job_id].append({
        'applicant_name': applicant_name,
        'resume': resume,
        'cover_letter': cover_letter
    })

def list_applications(job_id):
    if job_id not in applications:
        print("No applications for this job.")
        return

    for application in applications[job_id]:
        print(f"Applicant Name: {application['applicant_name']}")
        print(f"Resume: {application['resume']}")
        print(f"Cover Letter: {application['cover_letter']}")
        print("-" * 20)


def main():
    while True:
        print("1. Add Job")
        print("2. List Jobs")
        print("3. Apply for Job")
        print("4. List Applications")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            job_id = input("Enter Job ID: ")
            title = input("Enter Job Title: ")
            description = input("Enter Job Description: ")
            location = input("Enter Job Location: ")
            salary = input("Enter Job Salary: ")
            add_job(job_id, title, description, location, salary)
        elif choice == '2':
            list_jobs()
        elif choice == '3':
            job_id = input("Enter Job ID: ")
            applicant_name = input("Enter Applicant Name: ")
            resume = input("Enter Resume: ")
            cover_letter = input("Enter Cover Letter: ")
            apply_for_job(job_id, applicant_name, resume, cover_letter)
        elif choice == '4':
            job_id = input("Enter Job ID: ")
            list_applications(job_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
