def print_weights_nicely(weights: dict):
    longest_pillar = max(len(pillar) for pillar in weights) + 1
    print("\nPillar Ratings:")
    for pillar, weight in weights.items():
        formatted_pillar = pillar.replace('_', ' ').title()
        print(f"{formatted_pillar:<{longest_pillar}}: {weight * 100:.0f}%")