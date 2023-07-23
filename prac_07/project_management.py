"""
Estimated time taken: 220 minutes
Actual time taken: ~300 minutes
"""

import datetime
from project import Project


def main():
    projects = []
    filename = "projects.txt"  # Change this filename if needed

    # Load projects from the data file
    projects = load_projects(filename)

    choice = ""
    while choice != "Q":
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").strip().lower()

        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)

        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            start_date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yy): "), "%d/%m/%Y").date()
            filter_projects_by_date(projects, start_date)

        elif choice == 'a':
            add_new_project(projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            break

        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if lines and lines[0].strip() == "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage":  # Check if the first line is the header
                lines = lines[1:]  # Skip the header line
            for line in lines:
                project_data = line.strip().split("\t")  # Use tabs ("\t") as the separator
                if len(project_data) == 5:  # Ensure all fields are present
                    name = project_data[0]
                    start_date = datetime.datetime.strptime(project_data[1], "%d/%m/%Y").date()
                    priority = int(project_data[2])
                    estimate = float(project_data[3])
                    completion = int(project_data[4])
                    projects.append(Project(name, start_date, priority, estimate, completion))
                else:
                    print(f"Error reading project data: {line.strip()}")
    except FileNotFoundError:
        print("File not found. Starting with an empty project list.")
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as file:
        for project in projects:
            file.write(f"{project.name},{project.start_date.strftime('%d/%m/%Y')},{project.priority},"
                       f"{project.estimate},{project.completion}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(" ", project)
    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):    # Decided to use the lambda function for
        print(" ", project)                                                 # sorting to make easier.


def filter_projects_by_date(projects, start_date):
    filtered_projects = [project for project in projects if project.start_date > start_date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(" ", project)


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, estimate, completion))
    print("New project added.")


def update_project(projects):
    print("Choose a project to update:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    if 0 <= choice < len(projects):
        project = projects[choice]
        new_completion = input("New Percentage (leave blank to retain existing value): ")
        new_priority = input("New Priority (leave blank to retain existing value): ")

        if new_completion:
            project.completion = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)
        print("Project updated.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()

