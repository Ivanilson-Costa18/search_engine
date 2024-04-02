from app.utils import build_inverted_index

documents = [
    {
        "title": "Spaghetti Carbonara",
        "content": "1. Cook spaghetti according to package instructions. In a separate pan, cook diced pancetta until crispy. Mix cooked spaghetti with beaten eggs, grated Parmesan cheese, and cooked pancetta. Serve immediately with additional cheese and black pepper."
    },
    {
        "title": "Chicken Alfredo",
        "content": "1. Cook fettuccine according to package instructions. In a pan, cook diced chicken until no longer pink. Add heavy cream and Parmesan cheese to the pan, simmer until thickened. Toss cooked fettuccine with the sauce. Serve hot."
    },
    {
        "title": "Vegetable Stir-Fry",
        "content": "1. Heat oil in a wok or skillet. Add chopped vegetables (such as bell peppers, broccoli, carrots, and snap peas) and stir-fry until tender-crisp. Season with soy sauce, garlic, and ginger. Serve over cooked rice or noodles."
    },
    {
        "title": "Football News",
        "content": "Latest updates, scores, and highlights from the world of football."
    },
    {
        "title": "Movie Reviews",
        "content": "Reviews, ratings, and news about the latest movies and upcoming releases."
    },
    {
        "title": "Celebrity Gossip",
        "content": "Get the latest scoop on celebrities, Hollywood news, and entertainment gossip."
    },
    {
        "title": "Tech News",
        "content": "Stay updated with the latest in technology news, gadgets, and innovations."
    },
    {
        "title": "World News",
        "content": "Breaking news, analysis, and coverage from around the globe."
    },
    {
        "title": "Weather Updates",
        "content": "Current weather conditions, forecasts, and alerts for your area."
    },
    {
        "title": "Health Tips",
        "content": "Advice, tips, and information to maintain a healthy lifestyle."
    },
    {
        "title": "Travel Destinations",
        "content": "Explore the best travel destinations, attractions, and vacation ideas."
    },
    {
        "title": "Financial News",
        "content": "Latest updates, trends, and analysis from the world of finance and business."
    },
    {
        "title": "Recipes for Healthy Living",
        "content": "Discover nutritious and delicious recipes to help you lead a healthy lifestyle."
    },
    {
        "title": "Basketball Scores",
        "content": "Find out the latest scores, standings, and updates from the world of basketball."
    },
    {
        "title": "Book Reviews",
        "content": "Get recommendations and reviews for the best books across various genres."
    },
    {
        "title": "Fitness Workouts",
        "content": "Workout routines, tips, and exercises to help you stay fit and active."
    },
    {
        "title": "Entertainment News",
        "content": "Stay informed about the latest in entertainment news, celebrity interviews, and more."
    },
    {
        "title": "Science Discoveries",
        "content": "Explore groundbreaking discoveries and research in the field of science."
    },
    {
        "title": "Fashion Trends",
        "content": "Get the latest updates on fashion trends, styles, and runway collections."
    },
    {
        "title": "Home Decor Ideas",
        "content": "Discover inspiration and ideas for decorating your home in style."
    },
    {
        "title": "Personal Finance Tips",
        "content": "Learn strategies for managing your finances, budgeting, and investing wisely."
    },
    {
        "title": "Gardening Advice",
        "content": "Tips, tricks, and advice for cultivating a beautiful and productive garden."
    },
    {
        "title": "DIY Projects",
        "content": "Step-by-step guides and ideas for fun and creative DIY projects."
    },
    {
        "title": "Parenting Tips",
        "content": "Helpful advice and tips for raising happy, healthy children."
    },
    {
        "title": "Car Reviews",
        "content": "Reviews, ratings, and insights on the latest car models and trends."
    },
    {
        "title": "Music Reviews",
        "content": "Discover new music releases, album reviews, and artist interviews."
    },
    {
        "title": "Yoga Practice",
        "content": "Guided yoga routines and poses for relaxation, flexibility, and strength."
    },
    {
        "title": "Healthy Snack Ideas",
        "content": "Nutritious and tasty snack ideas to satisfy your cravings and fuel your day."
    },
    {
        "title": "Pet Care Tips",
        "content": "Advice on caring for your beloved pets, including nutrition, grooming, and training."
    },
    {
        "title": "Home Cooking Recipes",
        "content": "Delicious and easy-to-make recipes for home-cooked meals the whole family will love."
    },
    {
        "title": "Space Exploration News",
        "content": "Stay updated on the latest news and discoveries from space exploration missions."
    },
    {
        "title": "Job Search Advice",
        "content": "Tips, resources, and strategies to help you find and land your dream job."
    },
    {
        "title": "Healthy Eating Habits",
        "content": "Learn about the principles of healthy eating and how to develop good dietary habits."
    },
    {
        "title": "DIY Home Improvement",
        "content": "Projects, tips, and tutorials for improving your home's appearance and functionality."
    },
    {
        "title": "Gaming News",
        "content": "Latest updates, reviews, and insights from the world of video games and gaming culture."
    },
    {
        "title": "Self-Care Practices",
        "content": "Discover self-care routines and practices to promote mental, emotional, and physical well-being."
    },
    {
        "title": "Travel Guides",
        "content": "Comprehensive guides to popular travel destinations, attractions, and activities."
    },
    {
        "title": "Financial Planning Advice",
        "content": "Strategies and tips for effective financial planning, saving, and investing for the future."
    },
    {
        "title": "Healthy Dessert Recipes",
        "content": "Indulgent yet nutritious dessert recipes to satisfy your sweet tooth guilt-free."
    },
    {
        "title": "Cocktail Recipes",
        "content": "Craft cocktail recipes for every occasion, from classic favorites to creative concoctions."
    },
    {
        "title": "Home Workout Tips",
        "content": "Tips, routines, and exercises for effective workouts you can do from the comfort of your home."
    },
    {
        "title": "DIY Beauty Hacks",
        "content": "Simple and budget-friendly beauty hacks for skincare, makeup, and haircare."
    },
    {
        "title": "Mindfulness Meditation",
        "content": "Guided meditations and practices for cultivating mindfulness and inner peace."
    },
    {
        "title": "Healthy Breakfast Ideas",
        "content": "Quick and nutritious breakfast ideas to start your day off right."
    },
    {
        "title": "Photography Tips",
        "content": "Techniques, tutorials, and advice for improving your photography skills."
    },
    {
        "title": "Travel Photography Inspiration",
        "content": "Stunning travel photography to inspire your next adventure."
    },
    {
        "title": "Home Organization Hacks",
        "content": "Creative solutions and tips for organizing your home and decluttering your space."
    },
    {
        "title": "Nature Photography",
        "content": "Breathtaking images of nature's beauty captured by talented photographers."
    },
    {
        "title": "DIY Home Decor Projects",
        "content": "Unique and stylish DIY home decor projects to personalize your living space."
    },
    {
        "title": "Healthy Lunch Recipes",
        "content": "Nutritious and satisfying lunch recipes to fuel your day and keep you energized."
    },
    {
        "title": "Financial Literacy Resources",
        "content": "Educational resources and tools to improve your financial literacy and money management skills."
    },
    {
        "title": "Pet Adoption Tips",
        "content": "Advice and guidance for adopting and caring for a new pet."
    },
    {
        "title": "Family-Friendly Activities",
        "content": "Fun and engaging activities for the whole family to enjoy together."
    },
    {
        "title": "Healthy Smoothie Recipes",
        "content": "Delicious and nutritious smoothie recipes for a refreshing and energizing boost."
    },
    {
        "title": "DIY Crafts",
        "content": "Creative and inspiring DIY craft projects for all skill levels."
    },
    {
        "title": "Home Gardening Tips",
        "content": "Helpful tips and advice for successful home gardening and plant care."
    },
    {
        "title": "Budget Travel Tips",
        "content": "Strategies and advice for traveling on a budget without sacrificing experiences."
    },
    {
        "title": "Home Office Ideas",
        "content": "Inspiring ideas and tips for creating a functional and stylish home office space."
    },
    {
        "title": "Financial Planning for Retirement",
        "content": "Guidance and resources for planning and preparing for a secure retirement."
    },
    {
        "title": "DIY Hair Care Recipes",
        "content": "Natural and homemade hair care recipes for healthier, more vibrant hair."
    },
    {
        "title": "Stress Management Techniques",
        "content": "Effective strategies and techniques for managing stress and promoting relaxation."
    },
    {
        "title": "Healthy Dinner Recipes",
        "content": "Wholesome and delicious dinner recipes to enjoy with family and friends."
    },
    {
        "title": "Outdoor Adventure Ideas",
        "content": "Exciting and adventurous outdoor activities to explore and enjoy nature."
    },
    {
        "title": "Investing Strategies",
        "content": "Insights, tips, and strategies for successful investing and wealth building."
    },
    {
        "title": "DIY Home Renovation Projects",
        "content": "Project ideas and tips for renovating and remodeling your home."
    },
    {
        "title": "Family Meal Planning",
        "content": "Helpful tips and resources for planning nutritious and budget-friendly family meals."
    },
    {
        "title": "Green Living Tips",
        "content": "Practical advice and tips for adopting eco-friendly and sustainable living habits."
    },
    {
        "title": "Personal Development Resources",
        "content": "Tools and resources for personal growth, self-improvement, and achieving goals."
    },
    {
        "title": "DIY Skincare Recipes",
        "content": "Natural and homemade skincare recipes for healthier, glowing skin."
    },
    {
        "title": "Gourmet Cooking Techniques",
        "content": "Masterful techniques and tips for elevating your culinary skills and creating gourmet dishes."
    },
    {
        "title": "Productivity Hacks",
        "content": "Strategies and techniques for maximizing productivity and efficiency in daily life."
    },
    {
        "title": "Home Exercise Routines",
        "content": "Effective and convenient home exercise routines for staying active and fit."
    },
    {
        "title": "Personal Finance Education",
        "content": "Educational resources and guides to help you improve your financial literacy."
    },
    {
        "title": "DIY Home Cleaning Solutions",
        "content": "Natural and homemade cleaning solutions for a clean and healthy home."
    },
    {
        "title": "Healthy Baking Recipes",
        "content": "Wholesome and delicious baking recipes for guilt-free treats."
    },
    {
        "title": "Parenting Advice",
        "content": "Practical tips and advice for navigating the joys and challenges of parenthood."
    },
    {
        "title": "Hiking Trails",
        "content": "Discover scenic hiking trails and outdoor adventures in your area."
    },
    {
        "title": "Money-Saving Tips",
        "content": "Smart strategies and tips for saving money and managing your finances wisely."
    },
    {
        "title": "Home Improvement Projects",
        "content": "Inspiring ideas and DIY projects for enhancing your home's appearance and functionality."
    },
    {
        "title": "Cooking Techniques",
        "content": "Essential techniques and tips for mastering the art of cooking."
    },
    {
        "title": "DIY Beauty Products",
        "content": "Homemade beauty products and remedies for natural skincare and haircare."
    },
    {
        "title": "Personal Growth Strategies",
        "content": "Strategies and resources for achieving personal growth and self-improvement."
    },
    {
        "title": "Nutrition Education",
        "content": "Information and resources to help you make informed decisions about nutrition and healthy eating."
    },
    {
        "title": "Home Decorating Ideas",
        "content": "Inspiring ideas and tips for decorating your home with style and personality."
    },
    {
        "title": "Parenting Strategies",
        "content": "Effective parenting strategies and techniques for raising happy, healthy children."
    },
    {
        "title": "Healthy Meal Planning",
        "content": "Tips and resources for planning and preparing nutritious meals for you and your family."
    },
    {
        "title": "Travel Photography Tips",
        "content": "Expert tips and techniques for capturing stunning travel photos."
    },
    {
        "title": "Home Gardening Ideas",
        "content": "Creative ideas and tips for designing and maintaining a beautiful garden."
    },
    {
        "title": "DIY Home Decor Ideas",
        "content": "Creative and budget-friendly ideas for decorating your home."
    },
    {
        "title": "Stress Relief Techniques",
        "content": "Relaxation techniques and strategies for reducing stress and promoting well-being."
    },
    {
        "title": "Healthy Snack Recipes",
        "content": "Nutritious and satisfying snack recipes for guilt-free munching."
    },
    {
        "title": "Personal Finance Tips and Tricks",
        "content": "Practical tips and tricks for managing your finances and achieving financial goals."
    },
    {
        "title": "DIY Skincare Tips",
        "content": "Expert tips and tricks for maintaining healthy, radiant skin with DIY skincare."
    },
    {
        "title": "Home Renovation Ideas",
        "content": "Inspiring ideas and tips for renovating and remodeling your home."
    },
    {
        "title": "Parenting Resources",
        "content": "Useful resources and tools for parents navigating the challenges of raising children."
    },
    {
        "title": "Budget Travel Ideas",
        "content": "Budget-friendly travel ideas and tips for exploring new destinations without breaking the bank."
    },
    {
        "title": "Home Workout Ideas",
        "content": "Creative and effective workout ideas for staying fit and active at home."
    },
    {
        "title": "Financial Planning Strategies",
        "content": "Strategies and techniques for effective financial planning and wealth management."
    },
    {
        "title": "DIY Hair Care Tips",
        "content": "Expert tips and tricks for healthy, beautiful hair with DIY hair care."
    },
    {
        "title": "Mindfulness Practices",
        "content": "Practical mindfulness practices and techniques for living with intention and awareness."
    },
    {
        "title": "Healthy Breakfast Recipes",
        "content": "Delicious and nutritious breakfast recipes to start your day off right."
    },
    {
        "title": "Photography Techniques",
        "content": "Tips, tricks, and techniques for capturing stunning photographs."
    },
    {
        "title": "Spaghetti Carbonara",
        "content": "1. Cook spaghetti according to package instructions. In a separate pan, cook diced pancetta until crispy. Mix cooked spaghetti with beaten eggs, grated Parmesan cheese, and cooked pancetta. Serve immediately with additional cheese and black pepper."
    },
    {
        "title": "Chicken Alfredo",
        "content": "1. Cook fettuccine according to package instructions. In a pan, cook diced chicken until no longer pink. Add heavy cream and Parmesan cheese to the pan, simmer until thickened. Toss cooked fettuccine with the sauce. Serve hot."
    },
    {
        "title": "Vegetable Stir-Fry",
        "content": "1. Heat oil in a wok or skillet. Add chopped vegetables (such as bell peppers, broccoli, carrots, and snap peas) and stir-fry until tender-crisp. Season with soy sauce, garlic, and ginger. Serve over cooked rice or noodles."
    },
    {
        "title": "Classic Caesar Salad",
        "content": "1. In a large salad bowl, combine torn romaine lettuce leaves, Caesar dressing, grated Parmesan cheese, and croutons. Toss until well coated. Serve immediately as a side dish or topped with grilled chicken for a main course."
    },
    {
        "title": "Margherita Pizza",
        "content": "1. Preheat your oven to 475°F (245°C). Roll out pizza dough and place it on a baking sheet. Spread pizza sauce over the dough, then top with slices of fresh mozzarella cheese and fresh basil leaves. Bake for 10-12 minutes until the crust is golden and the cheese is bubbly."
    },
    {
        "title": "Beef Tacos",
        "content": "1. Cook ground beef in a skillet over medium heat until browned. Season with taco seasoning. Serve beef in taco shells with shredded lettuce, diced tomatoes, shredded cheese, and salsa. Optional toppings include sour cream and guacamole."
    },
    {
        "title": "Chicken Caesar Wrap",
        "content": "1. Lay a tortilla flat. Spread Caesar dressing over the tortilla. Add slices of grilled chicken, romaine lettuce, grated Parmesan cheese, and croutons. Roll up the tortilla tightly. Serve immediately or wrap in foil for later."
    },
    {
        "title": "Pasta Primavera",
        "content": "1. Cook pasta according to package instructions. In a skillet, sauté mixed vegetables (such as bell peppers, zucchini, cherry tomatoes, and mushrooms) in olive oil until tender. Toss cooked pasta with the vegetables and a splash of pasta water. Season with salt, pepper, and grated Parmesan cheese."
    },
    {
        "title": "Caprese Salad",
        "content": "1. Arrange alternating slices of ripe tomatoes and fresh mozzarella cheese on a plate. Tuck fresh basil leaves in between the slices. Drizzle with balsamic glaze and extra virgin olive oil. Season with salt and pepper to taste."
    },
    {
        "title": "Vegetable Lasagna",
        "content": "1. Preheat your oven to 375°F (190°C). Layer cooked lasagna noodles with marinara sauce, a mixture of ricotta cheese and spinach, and slices of roasted vegetables (such as zucchini, eggplant, and bell peppers). Repeat the layers until the baking dish is full. Top with mozzarella cheese and bake for 30-35 minutes until bubbly."
    },
    {
        "title": "Classic Beef Burger",
        "content": "1. Preheat your grill to medium-high heat. Form ground beef into patties and season with salt and pepper. Grill for about 4-5 minutes per side, or until desired doneness. Serve on toasted hamburger buns with lettuce, tomato, onion, and your favorite condiments."
    },
    {
        "title": "Pesto Pasta",
        "content": "1. Cook pasta according to package instructions. In a blender or food processor, blend together fresh basil leaves, pine nuts, garlic, Parmesan cheese, and olive oil until smooth. Toss cooked pasta with pesto sauce and cherry tomatoes. Serve with extra Parmesan cheese."
    },
    {
        "title": "Mushroom Risotto",
        "content": "1. In a saucepan, heat chicken or vegetable broth until simmering. In a separate pan, sauté diced onions and minced garlic in olive oil until softened. Add Arborio rice and cook for a few minutes until translucent. Gradually add the simmering broth, stirring frequently, until the rice is creamy and cooked through. Stir in sautéed mushrooms, grated Parmesan cheese, and chopped parsley. Serve hot."
    },
    {
        "title": "Fettuccine Alfredo",
        "content": "1. Cook fettuccine according to package instructions. In a saucepan, melt butter over medium heat. Add heavy cream and bring to a simmer. Stir in grated Parmesan cheese until melted and smooth. Toss cooked fettuccine with the Alfredo sauce. Serve hot, garnished with chopped parsley."
    },
    {
        "title": "Garlic Shrimp Scampi",
        "content": "1. In a skillet, heat olive oil over medium heat. Add minced garlic and cook until fragrant. Add shrimp and cook until pink and opaque. Season with salt, pepper, and red pepper flakes. Stir in white wine and lemon juice. Serve shrimp over cooked spaghetti or linguine, garnished with chopped parsley."
    },
    {
        "title": "Beef Stir-Fry",
        "content": "1. In a wok or skillet, heat oil over high heat. Add thinly sliced beef and stir-fry until browned. Remove beef from the pan. Add sliced bell peppers, onions, and broccoli florets to the pan. Stir-fry until tender-crisp. Return beef to the pan and add soy sauce, garlic, and ginger. Cook for a few more minutes until heated through. Serve hot over cooked rice."
    },
    {
        "title": "Teriyaki Chicken",
        "content": "1. Marinate chicken breasts in teriyaki sauce for at least 30 minutes. Grill or broil chicken until cooked through. Serve hot, drizzled with extra teriyaki sauce and garnished with chopped green onions and sesame seeds. Serve with steamed rice and vegetables."
    },
    {
        "title": "Baked Salmon",
        "content": "1. Preheat your oven to 375°F (190°C). Place salmon fillets on a baking sheet lined with parchment paper. Drizzle with olive oil and season with salt, pepper, and lemon zest. Bake for 12-15 minutes, or until the salmon is cooked through and flakes easily with a fork. Serve hot, garnished with fresh herbs and lemon wedges."
    },
    {
        "title": "Margarita Cocktail",
        "content": "1. Rub the rim of a glass with a lime wedge, then dip it in salt to coat. Fill the glass with ice cubes. In a shaker, combine tequila, lime juice, and triple sec. Shake well and pour over the ice. Garnish with a lime wedge. Enjoy!"
    },
    {
        "title": "Chocolate Chip Cookies",
        "content": "1. Preheat your oven to 375°F (190°C). In a mixing bowl, cream together softened butter, white sugar, and brown sugar until light and fluffy. Beat in eggs one at a time, then stir in vanilla extract. Gradually add flour mixture, then fold in chocolate chips. Drop by rounded spoonfuls onto ungreased baking sheets. Bake for 8 to 10 minutes until golden brown. Cool on wire racks."
    },
    {
        "title": "Blueberry Pancakes",
        "content": "1. In a mixing bowl, combine flour, sugar, baking powder, and salt. In a separate bowl, whisk together milk, melted butter, and eggs. Stir wet ingredients into dry ingredients until just combined. Gently fold in fresh blueberries. Pour batter onto a hot greased griddle and cook until bubbles form on the surface. Flip and cook until golden brown on the other side. Serve hot with maple syrup."
    },
    {
        "title": "Chicken Noodle Soup",
        "content": "1. In a large pot, heat olive oil over medium heat. Add diced onions, carrots, and celery, and sauté until softened. Add minced garlic and cook until fragrant. Pour in chicken broth and bring to a simmer. Add cooked shredded chicken, egg noodles, and chopped fresh herbs. Simmer until noodles are cooked through. Season with salt and pepper to taste. Serve hot."
    },
    {
        "title": "Egg Fried Rice",
        "content": "1. Cook white rice according to package instructions and let it cool. In a wok or skillet, heat oil over high heat. Add beaten eggs and scramble until cooked. Add cooked rice to the pan and stir-fry until heated through. Stir in chopped green onions, soy sauce, and cooked peas and carrots. Cook for a few more minutes until everything is well combined. Serve hot."
    },
    {
        "title": "Spinach and Feta Stuffed Chicken",
        "content": "1. Preheat your oven to 375°F (190°C). Butterfly chicken breasts and season with salt and pepper. Mix together chopped spinach, crumbled feta cheese, minced garlic, and dried oregano. Spread the spinach mixture over the chicken breasts, then roll up and secure with toothpicks. Place chicken in a baking dish and bake for 25-30 minutes, or until cooked through. Serve hot."
    },
    {
        "title": "Mango Salsa",
        "content": "1. In a bowl, combine diced mangoes, diced red bell peppers, chopped red onions, chopped cilantro, minced jalapeño, lime juice, and salt. Stir until well combined. Taste and adjust seasoning as needed. Serve chilled with tortilla chips or as a topping for grilled fish or chicken."
    },
    {
        "title": "Guacamole",
        "content": "1. In a bowl, mash ripe avocados with a fork until smooth but still chunky. Stir in diced tomatoes, diced onions, minced garlic, chopped cilantro, lime juice, and salt. Mix until well combined. Taste and adjust seasoning as needed. Serve immediately with tortilla chips or as a topping for tacos or nachos."
    },
    {
        "title": "Vegetarian Chili",
        "content": "1. In a large pot, heat oil over medium heat. Add diced onions, bell peppers, and carrots, and sauté until softened. Stir in minced garlic, chili powder, cumin, and oregano, and cook until fragrant. Add canned diced tomatoes, tomato sauce, cooked beans (such as kidney beans, black beans, and pinto beans), and vegetable broth. Simmer for 20-30 minutes, stirring occasionally. Serve hot with your favorite toppings."
    },
    {
        "title": "Peanut Butter Banana Smoothie",
        "content": "1. In a blender, combine ripe bananas, creamy peanut butter, Greek yogurt, milk, and a handful of ice cubes. Blend until smooth and creamy. Taste and adjust sweetness if needed by adding honey or maple syrup. Pour into glasses and serve immediately."
    },
    {
        "title": "Classic Margherita Pizza",
        "content": "1. Preheat your oven to 500°F (260°C) or as high as it will go. Stretch pizza dough into a circle and place it on a baking sheet or pizza stone. Spread pizza sauce over the dough, then arrange slices of fresh mozzarella cheese and fresh basil leaves on top. Drizzle with olive oil and sprinkle with salt. Bake for 10-12 minutes, until the crust is golden brown and the cheese is bubbly. Serve hot."
    },
    {
        "title": "Beef Tacos",
        "content": "1. In a skillet over medium heat, cook ground beef until browned and crumbled. Drain excess fat. Stir in taco seasoning and water according to package instructions. Simmer for 5 minutes. Warm taco shells in the oven or microwave. Fill each shell with cooked beef and top with shredded lettuce, diced tomatoes, shredded cheese, and other desired toppings."
    },
    {
        "title": "Chicken Quesadillas",
        "content": "1. In a skillet over medium heat, cook diced chicken until no longer pink. Remove from skillet and set aside. In the same skillet, add a tortilla. Sprinkle one half of the tortilla with shredded cheese, cooked chicken, diced onions, and sliced jalapeños. Fold the tortilla in half and cook until golden brown on both sides. Repeat with remaining ingredients. Cut quesadillas into wedges and serve with salsa and sour cream."
    },
    {
        "title": "Creamy Tomato Soup",
        "content": "1. In a large pot, heat olive oil over medium heat. Add diced onions and cook until softened. Add minced garlic and cook until fragrant. Stir in canned crushed tomatoes, chicken broth, dried basil, dried oregano, and a pinch of sugar. Simmer for 15-20 minutes. Blend the soup until smooth using an immersion blender or regular blender. Stir in heavy cream and heat through. Season with salt and pepper to taste. Serve hot with a sprinkle of fresh basil leaves."
    }
]

inverted_index = build_inverted_index(documents)