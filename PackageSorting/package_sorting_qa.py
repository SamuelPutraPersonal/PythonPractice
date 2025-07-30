class Package:
    def __init__(self, tracking_id, destination_zip_code, weight_kg):
        """
        Initializes a new Package object.
        """
        self.tracking_id = tracking_id
        self.destination_zip_code = destination_zip_code
        self.weight_kg = weight_kg
        self.scanned_status = False  # Default to not scanned
        self.sorted_status = False   # Default to not sorted
        print(f"Package {self.tracking_id} created for {self.destination_zip_code}.")

    def scan(self):
        """
        Marks the package as scanned.
        """
        if not self.scanned_status:
            self.scanned_status = True
            print(f"Package {self.tracking_id} scanned.")
        else:
            print(f"Package {self.tracking_id} already scanned.")

    def mark_as_sorted(self):
        """
        Marks the package as sorted.
        """
        if self.scanned_status and not self.sorted_status:
            self.sorted_status = True
            print(f"Package {self.tracking_id} marked as sorted.")
        elif not self.scanned_status:
            print(f"Cannot sort Package {self.tracking_id}: Not scanned yet!")
        else:
            print(f"Package {self.tracking_id} already sorted.")

    def get_info(self):
        """
        Returns a formatted string with package details.
        """
        return (f"Package ID: {self.tracking_id}\n"
                f"  Destination: {self.destination_zip_code}\n"
                f"  Weight: {self.weight_kg} kg\n"
                f"  Scanned: {self.scanned_status}\n"
                f"  Sorted: {self.sorted_status}")
        
class SortingMachine:
    def __init__(self, machine_id, capacity_per_hour):
        """
        Initializes a new SortingMachine object.
        """
        self.machine_id = machine_id
        self.capacity_per_hour = capacity_per_hour
        self.is_online = False
        self.packages_processed = 0
        print(f"Sorting Machine {self.machine_id} created (Capacity: {self.capacity_per_hour} pkgs/hr).")

    def go_online(self):
        """
        Sets the machine status to online.
        """
        if not self.is_online:
            self.is_online = True
            print(f"Machine {self.machine_id} is now ONLINE.")
        else:
            print(f"Machine {self.machine_id} is already online.")

    def go_offline(self):
        """
        Sets the machine status to offline.
        """
        if self.is_online:
            self.is_online = False
            print(f"Machine {self.machine_id} is now OFFLINE.")
        else:
            print(f"Machine {self.machine_id} is already offline.")

    def process_package(self, package):
        """
        Simulates scanning and sorting a package.
        Requires the machine to be online and the package to be unscanned.
        """
        if not self.is_online:
            print(f"Error: Machine {self.machine_id} is offline. Cannot process {package.tracking_id}.")
            return False

        if not isinstance(package, Package):
            print(f"Error: {package} is not a valid Package object.")
            return False

        if package.scanned_status and package.sorted_status:
            print(f"Package {package.tracking_id} already processed by Machine {self.machine_id}.")
            return True # Already done, consider it successful in this context

        # Step 1: Scan
        package.scan()
        if not package.scanned_status: # Should ideally be true after scan()
            print(f"Error: Package {package.tracking_id} failed to scan.")
            return False

        # Step 2: Sort
        print(f"Machine {self.machine_id} is sorting Package {package.tracking_id} to {package.destination_zip_code}...")
        package.mark_as_sorted()

        if package.sorted_status: # Check if sorting was successful
            self.packages_processed += 1
            print(f"Machine {self.machine_id} successfully processed {package.tracking_id}. Total processed: {self.packages_processed}")
            return True
        else:
            print(f"Machine {self.machine_id} failed to sort {package.tracking_id}.")
            return False
        

class QAEngineer:
    def __init__(self, name, employee_id):
        """
        Initializes a new QAEngineer object.
        """
        self.name = name
        self.employee_id = employee_id
        self.tests_run = 0
        print(f"QA Engineer {self.name} (ID: {self.employee_id}) ready for testing.")

    def run_test_case(self, machine, package, expected_outcome_sorted=True):
        """
        Runs a test case on the sorting machine with a specific package.
        expected_outcome_sorted: True if the package is expected to be sorted, False otherwise.
        """
        print(f"\n--- TEST CASE #{self.tests_run + 1} initiated by {self.name} ---")
        print(f"Testing Package {package.tracking_id} on Machine {machine.machine_id}.")
        print(f"Initial Package Status:\n{package.get_info()}")
        print(f"Machine {machine.machine_id} Status: {'Online' if machine.is_online else 'Offline'}")

        self.tests_run += 1
        test_passed = False

        # Simulate the processing
        machine_processed = machine.process_package(package)

        # Verify results
        actual_sorted_status = package.sorted_status

        if expected_outcome_sorted:
            if machine_processed and actual_sorted_status:
                print(f"RESULT: SUCCESS - Package {package.tracking_id} was sorted as expected.")
                test_passed = True
            else:
                print(f"RESULT: FAILED - Package {package.tracking_id} was NOT sorted as expected.")
        else: # Expected not sorted
            if not actual_sorted_status:
                print(f"RESULT: SUCCESS - Package {package.tracking_id} was NOT sorted as expected.")
                test_passed = True
            else:
                print(f"RESULT: FAILED - Package {package.tracking_id} was sorted, but was NOT expected to be.")

        print(f"Final Package Status:\n{package.get_info()}")
        print(f"--- TEST CASE #{self.tests_run} {'PASSED' if test_passed else 'FAILED'} ---\n")
        return test_passed

# --- Setup Entities ---
print("--- Setting up QA Environment ---")
main_sorter = SortingMachine("S-ALPHA-001", 1000)
backup_sorter = SortingMachine("S-BETA-002", 500)

qa_alex = QAEngineer("Alex QA", "EMP001")
qa_ben = QAEngineer("Ben QA", "EMP002")

package_A = Package("PVN12345", "1000AB", 2.5)
package_B = Package("PVN67890", "2000CD", 0.8)
package_C = Package("PVN54321", "3000EF", 15.0) # Heavy package
package_D = Package("PVN98765", "4000GH", 1.2) # To test offline scenario

print("\n" + "="*50 + "\n")

# --- Test Scenarios ---

# Scenario 1: Basic successful sort
print("Scenario 1: Basic successful sort on main machine")
main_sorter.go_online()
qa_alex.run_test_case(main_sorter, package_A, expected_outcome_sorted=True)

print("\n" + "="*50 + "\n")

# Scenario 2: Try to sort an already sorted package (should show as already processed)
print("Scenario 2: Attempt to sort an already sorted package")
qa_alex.run_test_case(main_sorter, package_A, expected_outcome_sorted=True) # Still expects sorted, but logic handles 'already sorted'

print("\n" + "="*50 + "\n")

# Scenario 3: Test a package on an offline machine
print("Scenario 3: Attempt to sort package on an OFFLINE machine")
qa_ben.run_test_case(backup_sorter, package_D, expected_outcome_sorted=False) # Expect it NOT to be sorted

print("\n" + "="*50 + "\n")

# Scenario 4: Bring backup machine online and sort package D
print("Scenario 4: Bring backup machine online and process package D")
backup_sorter.go_online()
qa_ben.run_test_case(backup_sorter, package_D, expected_outcome_sorted=True)

print("\n" + "="*50 + "\n")

# Scenario 5: Check processed count
print("Scenario 5: Check processed package counts")
print(f"Main Sorter {main_sorter.machine_id} processed: {main_sorter.packages_processed} packages.")
print(f"Backup Sorter {backup_sorter.machine_id} processed: {backup_sorter.packages_processed} packages.")

print("\n" + "="*50 + "\n")

# Scenario 6: Create and test a new package
print("Scenario 6: New package, new test")
package_E = Package("PVN11223", "5000IJ", 0.5)
qa_alex.run_test_case(main_sorter, package_E, expected_outcome_sorted=True)


print("\n--- Final Statuses ---")
print(package_A.get_info())
print("---")
print(package_D.get_info())
print("---")
print(package_E.get_info())