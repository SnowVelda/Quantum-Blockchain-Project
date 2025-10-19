def apply_constitutional_filter(simulation_result):
    """
    Applies constitutional principles to the simulation result.
    Returns True if the result is acceptable, False otherwise.
    """
    print(f"  [Constitutional Filter]: Applying safeguards to '{simulation_result}'...")
    if "paradox risk" in simulation_result.lower() or "highly unstable" in simulation_result.lower():
        print("  [Constitutional Filter]: Outcome rejected due to constitutional violation.")
        return False
    print("  [Constitutional Filter]: Outcome passes constitutional review.")
    return True
