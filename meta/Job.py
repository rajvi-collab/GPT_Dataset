class User:
    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role

class Job:
    def __init__(self, title, description, posted_by):
        self.title = title
        self.description = description
        self.posted_by = posted_by

class Application:
    def __init__(self, job, applied_by):
        self.job = job
        self.applied_by = applied_by

users = []
jobs = []
applications = []

def register_user():
    email = input("Enter email: ")
    password = input("Enter password: ")
    role = input("Enter role (applicant/recruiter): ")
    users.append(User(email, password, role))
    print("User registered successfully!")

def login_user():
    email = input("Enter email: ")
    password = input("Enter password: ")
    for user in users:
        if user.email == email and user.password == password:
            return user
    return None

def post_job(user):
    if user.role != 'recruiter':
        print("Only recruiters can post jobs.")
        return
    title = input("Enter job title: ")
    description = input("Enter job description: ")
    jobs.append(Job(title, description, user.email))
    print("Job posted successfully!")

def apply_job(user):
    if user.role != 'applicant':
        print("Only applicants can apply for jobs.")
        return
    for i, job in enumerate(jobs):
        print(f"{i+1}. {job.title}")
    choice = int(input("Enter job number to apply: ")) - 1
    if choice < 0 or choice >= len(jobs):
        print("Invalid choice.")
        return
    applications.append(Application(jobs[choice], user.email))
    print("Application submitted successfully!")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            user = login_user()
            if user:
                print("Logged in successfully!")
                while True:
                    print("1. Post Job")
                    print("2. Apply Job")
                    print("3. Logout")
                    choice = input("Enter choice: ")
                    if choice == '1':
                        post_job(user)
                    elif choice == '2':
                        apply_job(user)
                    elif choice == '3':
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Invalid credentials.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()