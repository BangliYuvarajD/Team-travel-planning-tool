#Team Travel Planning Tool
class TravelPlan:
    def _init_(self, destination, start_date, end_date):
        self.destination = destination
        self.start_date = start_date 
        self.end_date = end_date
        self.team_members = []
 
    def add_team_member(self, name):
        self.team_members.append(name)
  
    def view_plan(self):
        print(f"Destination: {self.destination}")
        print(f"Start Date: {self.start_date}") 
        print(f"End Date: {self.end_date}")
        print(f"Team Members: {', '.join(self.team_members)}")

    def update_plan(self, destination=None, start_date=None, end_date=None):
        if destination:
            self.destination = destination
        if start_date:
            self.start_date = start_date
        if end_date:
            self.end_date = end_date

    def update_team_member(self, index, name):
        if index < len(self.team_members):
            self.team_members[index] = name
        else:
            print("Invalid member index.")

    def delete_team_member(self, index):
        if index < len(self.team_members):
            del self.team_members[index]
        else:
            print("Invalid member index.")


def main():
    print("Team Travel Planning Tool")
    print("-------------------------")

    plans = {}

    while True:
        print("\nOptions:")
        print("1. Create Travel Plan")
        print("2. Add Team Member")
        print("3. View Travel Plan")
        print("4. Update Travel Plan")
        print("5. Update Team Member")
        print("6. Delete Team Member")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            plan_name = input("Enter plan name: ")
            destination = input("Enter destination: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")

            plans[plan_name] = TravelPlan(destination, start_date, end_date)
            print(f"Plan '{plan_name}' created successfully.")

        elif choice == "2":
            plan_name = input("Enter plan name: ")
            if plan_name in plans:
                name = input("Enter team member's name: ")
                plans[plan_name].add_team_member(name)
                print(f"Team member '{name}' added to plan '{plan_name}' successfully.")
            else:
                print(f"Plan '{plan_name}' does not exist.")

        elif choice == "3":
            plan_name = input("Enter plan name: ")
            if plan_name in plans:
                plans[plan_name].view_plan()
            else:
                print(f"Plan '{plan_name}' does not exist.")

        elif choice == "4":
            plan_name = input("Enter plan name: ")
            if plan_name in plans:
                destination = input("Enter new destination (press Enter to skip): ")
                start_date = input("Enter new start date (press Enter to skip): ")
                end_date = input("Enter new end date (press Enter to skip): ")

                plans[plan_name].update_plan(destination or None, start_date or None, end_date or None)
                print(f"Plan '{plan_name}' updated successfully.")
            else:
                print(f"Plan '{plan_name}' does not exist.")

        elif choice == "5":
            plan_name = input("Enter plan name: ")
            if plan_name in plans:
                plans[plan_name].view_plan()
                index = int(input("Enter team member index to update: ")) - 1
                name = input("Enter new team member's name: ")

                plans[plan_name].update_team_member(index, name)
                print(f"Team member updated successfully.")
            else:
                print(f"Plan '{plan_name}' does not exist.")

        elif choice == "6":
            plan_name = input("Enter plan name: ")
            if plan_name in plans:
                plans[plan_name].view_plan()
                index = int(input("Enter team member index to delete: ")) - 1

                plans[plan_name].delete_team_member(index)
                print(f"Team member deleted successfully.")
            else:
                print(f"Plan '{plan_name}' does not exist.")

        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose again.")


if _name_ == "_main_":
    main()
