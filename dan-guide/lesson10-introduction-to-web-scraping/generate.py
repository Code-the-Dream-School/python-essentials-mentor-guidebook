import json
import random

cities_and_states = [
    ("New York", "NY"),
    ("Los Angeles", "CA"),
    ("Chicago", "IL"),
    ("Houston", "TX"),
    ("Phoenix", "AZ"),
    ("San Francisco", "CA"),
    ("Miami", "FL"),
    ("Dallas", "TX"),
    ("Boston", "MA"),
    ("Seattle", "WA"),
    ("Denver", "CO"),
    ("Austin", "TX"),
    ("San Diego", "CA"),
    ("Las Vegas", "NV"),
    ("Orlando", "FL"),
    ("Atlanta", "GA"),
    ("Washington", "DC"),
    ("Portland", "OR"),
    ("Detroit", "MI"),
    ("Philadelphia", "PA"),
    ("Clarksville", "TN")
]


def generate_listing(id):
    price = f"${random.randint(300000, 1000000):,}"
    beds = random.randint(2, 6)
    baths = random.randint(2, 5)
    sqft = f"{random.randint(1500, 4000):,}"
    city, state = random.choice(cities_and_states)
    address = f"{random.randint(1000, 5000)} {random.choice(['Maple', 'Pine', 'Oak', 'Elm', 'Cedar'])} St, {city}, {state} {random.randint(10000, 99999)}"
    description = "Super cool house. Buy this sweet home and never disappoint your friends/family again!"
    
    # Random features
    features = [
        "Close to public transport",
        "Well-maintained backyard",
        "Modern kitchen with new appliances",
        "Swimming pool",
        "Ocean view",
        "Large garage",
        "Gated community",
        "Pet-friendly",
        "Walking distance to parks",
        "Recently renovated"
    ]

    selected_features = random.sample(features, random.randint(2, 4))

    image = f"/real-estate-{random.randint(1, 5)}.jpg"
    
    return {
        "id": id,
        "price": price,
        "beds": beds,
        "baths": baths,
        "sqft": sqft,
        "address": address,
        "image": image,
        "description": description,
        "features": selected_features
    }

listings = [generate_listing(i + 1) for i in range(100)]

output_file = r"C:\Users\Dan\Desktop\ctd_py\python_homework\wk9\wk9_website\data\listings.json"
with open(output_file, "w") as f:
    json.dump(listings, f, indent=4)

print(f"100 listings generated and saved to {output_file}")
