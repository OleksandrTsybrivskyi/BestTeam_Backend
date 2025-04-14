from core.models import Location

places = [
    {
        "id": 1,
        "name": "Holy Moly",
        "position": [49.84009711830377, 24.032622815547313],
        "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_qDwGWNbo8CaqKh5n4Rxh9u98OfRpwIuSOg&s",
        "description": "Holy Moly is a popular restaurant in Lviv, known for its vibrant atmosphere and delicious food. It offers a diverse menu with a focus on fresh ingredients and unique flavors. The restaurant is designed to provide a comfortable dining experience for all guests.",
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
        "name": "Cinema at Forum Lviv Planeta Kino (Forum Lviv)",
        "position": [49.85000749290983, 24.0223520122525],
        "description": "Cinema at Forum Lviv Planeta Kino is a modern cinema complex located in the Forum Lviv shopping center. It features multiple screens, comfortable seating, and a wide selection of movies, making it a popular destination for film enthusiasts.",
        "image_url":"https://dynamic-media-cdn.tripadvisor.com/media/photo-o/09/6f/7f/99/planeta-kino-with-4dx.jpg?w=900&h=500&s=1",
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
        "description": "Ribs Restaurant \"At Arsenal\" is a cozy eatery in Lviv, specializing in delicious ribs and grilled dishes. The restaurant offers a warm atmosphere and a variety of options for meat lovers.",
        "image_url":"https://namori.com.ua/img/service/27b99358cfa75d8abfa7d3d75ff15d35/2-desc-5e5a27f7be31b.jpg",
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
        "description": "McDonald's is a well-known fast-food chain offering a variety of burgers, fries, and beverages. The restaurant is designed to provide a quick and convenient dining experience for all guests.",
        "image_url":"https://logos-download.com/wp-content/uploads/2016/03/McDonalds_Logo_2018.png",
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
        "name": "Good Friend",
        "position": [49.84391025591689, 24.030751806141733],
        "description": "Good Friend is a cozy cafe in Lviv, known for its friendly atmosphere and delicious coffee. It offers a variety of pastries and snacks, making it a great place to relax and enjoy a treat.",
        "image_url":"https://goodfriend.net.ua/wp-content/uploads/2023/04/IMG_5944-2-2-scaled-e1681218652731.jpg.pagespeed.ce.8cjq_Td38n.jpg",
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
        "name": "Virmenka",
        "position": [49.843277005392395, 24.031906235775306],
        "description": "Virmenka is a cozy cafe in Lviv, known for its warm atmosphere and delicious coffee. It offers a variety of pastries and snacks, making it a great place to relax and enjoy a treat.",
        "image_url":"https://virmenka.com.ua/files/img/1about/image1-3.jpg.pagespeed.ce.2HrfDL7YVE.jpg",
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
        "description": "Lviv Handmade Chocolate is a charming cafe and chocolate shop in Lviv, offering a wide range of handmade chocolates and desserts. The cozy atmosphere and friendly staff make it a perfect spot for chocolate lovers.",
        "image_url":"https://lviv.travel/image/locations/62/6b/48/626b48e67187d03d49876c78d315f0199f6bc737_1552654397.jpg?crop=1600%2C773%2C0%2C3",
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
            "description": place["description"],
            "image_url": place["image_url"],
            "ramps": place["accessibility"]["ramps"],
            "tactile_elements": place["accessibility"]["tactileElements"],
            "adapted_toilets": place["accessibility"]["adaptedToilets"],
            "wide_entrance": place["accessibility"]["wideEntrance"],
            "visual_impairment_friendly": place["accessibility"]["visualImpairmentFriendly"],
            "wheelchair_accessible": place["accessibility"]["wheelchairAccessible"],
        }
    )

print("✅ Locations inserted successfully.")
