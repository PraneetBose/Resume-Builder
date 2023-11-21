import json

RESUME_FILE = 'resume.json'

def load_resume():
    try:
        with open(RESUME_FILE, 'r') as file:
            resume = json.load(file)
    except FileNotFoundError:
        resume = {
            'personal_info': {},
            'education': [],
            'experience': [],
            'skills': [],
        }
    return resume

def save_resume(resume):
    with open(RESUME_FILE, 'w') as file:
        json.dump(resume, file, indent=2)

def display_resume(resume):
    print("\n=== Personal Information ===")
    for key, value in resume['personal_info'].items():
        print(f"{key.capitalize()}: {value}")

    print("\n=== Education ===")
    for entry in resume['education']:
        print(f"{entry['degree']} in {entry['field']} ({entry['year']})")

    print("\n=== Experience ===")
    for entry in resume['experience']:
        print(f"{entry['title']} at {entry['company']} ({entry['year']})")

    print("\n=== Skills ===")
    print(', '.join(resume['skills']))

def update_personal_info(resume):
    print("\n=== Personal Information ===")
    for key in ['name', 'email', 'phone', 'address']:
        value = input(f"Enter {key.capitalize()}: ")
        resume['personal_info'][key] = value

def add_education(resume):
    print("\n=== Add Education ===")
    degree = input("Enter degree: ")
    field = input("Enter field of study: ")
    year = input("Enter graduation year: ")

    entry = {'degree': degree, 'field': field, 'year': year}
    resume['education'].append(entry)

def add_experience(resume):
    print("\n=== Add Experience ===")
    title = input("Enter job title: ")
    company = input("Enter company: ")
    year = input("Enter year: ")

    entry = {'title': title, 'company': company, 'year': year}
    resume['experience'].append(entry)

def add_skills(resume):
    print("\n=== Add Skills ===")
    skills = input("Enter skills (comma-separated): ").split(',')
    resume['skills'].extend([skill.strip() for skill in skills])

def main():
    print("Virtual Resume Builder")

    resume = load_resume()

    while True:
        print("\n1. Display Resume")
        print("2. Update Personal Information")
        print("3. Add Education")
        print("4. Add Experience")
        print("5. Add Skills")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_resume(resume)
        elif choice == '2':
            update_personal_info(resume)
            save_resume(resume)
        elif choice == '3':
            add_education(resume)
            save_resume(resume)
        elif choice == '4':
            add_experience(resume)
            save_resume(resume)
        elif choice == '5':
            add_skills(resume)
            save_resume(resume)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
