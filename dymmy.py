def compute_pakshatithi4mdegree(deg):
    # Normalize degrees to be within the range [0, 360)
    normalized_deg = deg % 360

    # Determine the paksha (waxing or waning)
    if normalized_deg < 180:
        paksha = "shukla"
    else:
        paksha = "krishna"

    # Determine the tithi
    tithi = ((normalized_deg % 180) // 12) + 1

    return paksha, tithi

# Example usage:
degrees = 135
paksha, tithi = compute_pakshatithi4mdegree(degrees)
print(f"For {degrees} degrees: Paksha - {paksha.capitalize()}, Tithi - {tithi}")
