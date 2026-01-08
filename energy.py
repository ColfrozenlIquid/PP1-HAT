def energy_wh(power_watts, time_seconds):
    """Return energy in watt-hours."""
    return (power_watts * time_seconds) / 3600

# Example assumptions
llm_energy_per_prompt = 0.3  # Wh (your value)
prompts_per_form = 100

# Classical NLP parameters
cpu_power = 20  # watts
ner_time_per_field = 0.02  # seconds

# Rule-based system parameters
rule_time_per_field = 0.005  # seconds

# Calculations
llm_total = llm_energy_per_prompt * prompts_per_form
nlp_total = energy_wh(cpu_power, ner_time_per_field) * prompts_per_form
rule_total = energy_wh(cpu_power, rule_time_per_field) * prompts_per_form

print("Energy per 10-field form:")
print(f"LLM: {llm_total:.3f} Wh")
print(f"Classical NLP: {nlp_total:.6f} Wh")
print(f"Rule-based: {rule_total:.6f} Wh")
print("\nRelative multipliers (LLM / other):")
print(f"vs NLP: {llm_total / nlp_total:.0f} ×")
print(f"vs Rule-based: {llm_total / rule_total:.0f} ×")