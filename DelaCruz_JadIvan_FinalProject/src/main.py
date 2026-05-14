from tracker import TrackerManager

def main():
    # Pathing relative to project root
    manager = TrackerManager('data/maintenance_log.json')
    
    while True:
        print("\n--- MAINTENANCE TRACKER ---")
        print("1. Add Task\n2. View All Tasks\n3. Search Asset\n4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            asset = input("Asset Name: ")
            detail = input("Maintenance Detail: ")
            date = input("Date (YYYY-MM-DD): ")
            manager.add_task(asset, detail, date)
            print("Task added successfully!")
            
        elif choice == '2':
            for i, task in enumerate(manager.tasks, 1):
                print(f"{i}. {task['date']} - {task['asset_name']}: {task['task_details']}")
                
        elif choice == '3':
            q = input("Enter Asset Name to search: ")
            results = manager.search_tasks(q)
            print(f"Found {len(results)} matches.")
            
        elif choice == '4':
            break

if __name__ == "__main__":
    main()