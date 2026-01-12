def energy_wh(power_watts, time_seconds):
    """Return energy in watt-hours."""
    return (power_watts * time_seconds) / 3600

# Your actual use case: 10-field form, conversational filling
fields_per_form = 10

# LLM approach (your current system)
llm_energy_per_prompt = 1.82  # Wh
llm_interactions = fields_per_form * 2  # Ask question + interpret answer
llm_total = llm_energy_per_prompt * llm_interactions

# Small LLM alternative (requested)
small_llm_energy_per_prompt = 0.11  # Wh
small_llm_total = small_llm_energy_per_prompt * llm_interactions

# Classical NLP alternative (what you should be using)
cpu_power_nlp = 20  # watts
question_generation_time = 0.001  # Template lookup, trivial
answer_parsing_time = 0.02  # NER + validation
nlp_time_per_field = question_generation_time + answer_parsing_time
nlp_total = energy_wh(cpu_power_nlp, nlp_time_per_field * fields_per_form)

# Rule-based + simple NLP hybrid (optimal approach)
cpu_power_hybrid = 15  # watts
hybrid_time_per_field = 0.005  # Mostly rule-based with light NLP
hybrid_total = energy_wh(cpu_power_hybrid, hybrid_time_per_field * fields_per_form)

print("Energy per 10-field form (conversational filling):")
print(f"LLM (current):             {llm_total:.2f} Wh")
print(f"Small LLM (0.11 Wh/prompt): {small_llm_total:.2f} Wh")
print(f"Classical NLP:              {nlp_total:.4f} Wh")
print(f"Rule-based + light NLP:     {hybrid_total:.5f} Wh")

print("\nYour system uses:")
print(f"LLM / NLP:          {llm_total / nlp_total:.0f}× more energy")
print(f"LLM / hybrid:       {llm_total / hybrid_total:.0f}× more energy")
print(f"Small LLM / NLP: {small_llm_total / nlp_total:.0f}× more energy")
print(f"Small LLM / hybrid: {small_llm_total / hybrid_total:.0f}× more energy")

def energy_to_laptop_time(energy_Wh, laptop_power_W=30):
    """
    Convert energy in watt-hours into a human-friendly usage duration 
    for a reference device (e.g., laptop).
    """
    hours = energy_Wh / laptop_power_W
    seconds = hours * 3600

    if seconds < 60:
        return f"{seconds:.1f} seconds"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f} minutes"
    else:
        return f"{hours:.2f} hours"


# Your original values
llm_energy = llm_total
small_llm_energy = small_llm_total
nlp_energy = nlp_total
hybrid_energy = hybrid_total

print("Human-scale analogies (Laptop ~50W):")
print(f"LLM:        enough energy to run a laptop for {energy_to_laptop_time(llm_energy)}")
print(f"Small LLM:  enough energy to run a laptop for {energy_to_laptop_time(small_llm_energy)}")
print(f"NLP:        enough energy to run a laptop for {energy_to_laptop_time(nlp_energy)}")
print(f"Hybrid:     enough energy to run a laptop for {energy_to_laptop_time(hybrid_energy)}")
