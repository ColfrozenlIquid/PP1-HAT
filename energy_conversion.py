def energy_to_laptop_time(energy_Wh, laptop_power_W=50):
    """
    Convert energy in watt-hours into a human-friendly usage duration 
    for a reference device (e.g., laptop).
    """
    hours = energy_Wh / laptop_power_W
    seconds = hours * 3600

    # Format into human-friendly unit
    if seconds < 60:
        return f"{seconds:.1f} seconds"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f} minutes"
    else:
        return f"{hours:.2f} hours"


# Your original values
llm_energy = llm_total        # ≈ 36 Wh in your example
nlp_energy = nlp_total        # ≈ 0.006 Wh
hybrid_energy = hybrid_total  # ≈ 0.001 Wh

print("Human-scale analogies (Laptop ~50W):")
print(f"LLM:    enough energy to run a laptop for {energy_to_laptop_time(llm_energy)}")
print(f"NLP:    enough energy to run a laptop for {energy_to_laptop_time(nlp_energy)}")
print(f"Hybrid: enough energy to run a laptop for {energy_to_laptop_time(hybrid_energy)}")
