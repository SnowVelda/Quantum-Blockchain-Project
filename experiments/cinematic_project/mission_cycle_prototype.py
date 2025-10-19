import os
import datetime
from quantum_simulation import run_quantum_simulation
from constitutional_filter import apply_constitutional_filter

# Define file paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
MISSION_LOG_PATH = os.path.join(PROJECT_ROOT, 'mission_log.txt') # New log for missions

def log_mission_event(event_type, message):
    """Logs mission events to a dedicated mission log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{event_type}] {message}"
    with open(MISSION_LOG_PATH, 'a') as f:
        f.write(log_entry + '\n')
    print(log_entry)

def simulate_stability_check(simulation_result):
    """Mocks a stability check based on simulation result."""
    print(f"  [Stability Check]: Assessing stability for '{simulation_result}'...")
    if "stable" in simulation_result.lower() or "optimal" in simulation_result.lower():
        return True, "Stability confirmed."
    return False, "Stability uncertain, proceed with caution."

def main():
    print("--- Echo Prime Mission Cycle Prototype ---")
    print("This prototype simulates a single mission cycle.")
    print("Type 'exit' to quit.")

    while True:
        user_request = input("\nUser Input (Desired Temporal Destination/Action): ")
        if user_request.lower() == 'exit':
            break

        log_mission_event("USER_INPUT", user_request)

        # 1. Quantum Simulation
        simulation_result = run_quantum_simulation(user_request)
        log_mission_event("QUANTUM_SIMULATION", simulation_result)

        # 2. Constitutional Filter
        if not apply_constitutional_filter(simulation_result):
            log_mission_event("MISSION_ABORTED", "Constitutional filter rejected the outcome.")
            print("Mission aborted: Constitutional safeguards triggered.")
            continue

        # 3. Stability Check
        stability_ok, stability_message = simulate_stability_check(simulation_result)
        log_mission_event("STABILITY_CHECK", stability_message)

        if not stability_ok:
            log_mission_event("MISSION_WARNING", "Temporal jump might be unstable.")
            print("Warning: Temporal jump might be unstable.")
            # Decide whether to proceed or not based on severity
            if "uncertain" in stability_message.lower():
                proceed = input("Proceed with potentially unstable jump? (yes/no): ").lower()
                if proceed != 'yes':
                    log_mission_event("MISSION_ABORTED", "User chose not to proceed with unstable jump.")
                    print("Mission aborted by user.")
                    continue

        # 4. Temporal Jump Result
        temporal_jump_result = f"Successfully initiated temporal jump to a timeline with: {simulation_result}"
        log_mission_event("TEMPORAL_JUMP", temporal_jump_result)
        print(f"\nEcho Prime: {temporal_jump_result}")
        print("Mission cycle complete.")

if __name__ == "__main__":
    main()
