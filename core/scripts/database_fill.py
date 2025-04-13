from core.models import Location

places = [
    {
        "id": 1,
        "name": "Holy Moly",
        "position": [49.84009711830377, 24.032622815547313],
        "accessibility": {
            "ramps": False,
            "tactileElements": False,
            "adaptedToilets": True,
            "wideEntrance": True,
            "visualImpairmentFriendly": False,
            "wheelchairAccessible": True,
        },
    },
    {
        "id": 2,
        "name": "Кінотеатр Планета Кіно (Forum Lviv)",
        "position": [49.85000749290983, 24.0223520122525],
        "accessibility": {
            "ramps": True,
            "tactileElements": True,
            "adaptedToilets": True,
            "wideEntrance": True,
            "visualImpairmentFriendly": True,
            "wheelchairAccessible": True,
        },
    },
    {
        "id": 3,
        "name": "Ribs Restaurant \"At Arsenal\"",
        "position": [49.84154820968541, 24.035267897124676],
        "accessibility": {
            "ramps": False,
            "tactileElements": False,
            "adaptedToilets": False,
            "wideEntrance": False,
            "visualImpairmentFriendly": False,
            "wheelchairAccessible": False,
        },
    },
    {
        "id": 4,
        "name": "McDonald`s",
        "position": [49.8430001825941, 24.026156815915172],
        "accessibility": {
            "ramps": True,
            "tactileElements": True,
            "adaptedToilets": False,
            "wideEntrance": True,
            "visualImpairmentFriendly": True,
            "wheelchairAccessible": False,
        },
    },
    {
        "id": 5,
        "name": "Good Fried",
        "position": [49.84391025591689, 24.030751806141733],
        "accessibility": {
            "ramps": False,
            "tactileElements": True,
            "adaptedToilets": False,
            "wideEntrance": True,
            "visualImpairmentFriendly": True,
            "wheelchairAccessible": True,
        },
    },
    {
        "id": 6,
        "name": "Вірменка",
        "position": [49.843277005392395, 24.031906235775306],
        "accessibility": {
            "ramps": True,
            "tactileElements": True,
            "adaptedToilets": True,
            "wideEntrance": True,
            "visualImpairmentFriendly": True,
            "wheelchairAccessible": True,
        },
    },
    {
        "id": 7,
        "name": "Lviv Handmade Chocolate",
        "position": [49.84123676738078, 24.03309118513618],
        "accessibility": {
            "ramps": False,
            "tactileElements": False,
            "adaptedToilets": False,
            "wideEntrance": False,
            "visualImpairmentFriendly": True,
            "wheelchairAccessible": False,
        },
    },
]

for place in places:
    Location.objects.update_or_create(
        id=place["id"],
        defaults={
            "name": place["name"],
            "latitude": place["position"][0],
            "longitude": place["position"][1],
            "description": "",
            "image_url": "",
            "ramps": place["accessibility"]["ramps"],
            "tactile_elements": place["accessibility"]["tactileElements"],
            "adapted_toilets": place["accessibility"]["adaptedToilets"],
            "wide_entrance": place["accessibility"]["wideEntrance"],
            "visual_impairment_friendly": place["accessibility"]["visualImpairmentFriendly"],
            "wheelchair_accessible": place["accessibility"]["wheelchairAccessible"],
        }
    )

print("✅ Locations inserted successfully.")
