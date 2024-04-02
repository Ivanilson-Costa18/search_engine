from app.utils import build_inverted_index

documents = [
    {
        "title": "Allrecipes",
        "content": "Find a vast collection of recipes searchable by cuisine, ingredients, meal type, and dietary needs. Offers step-by-step instructions, user reviews, and nutritional information.",
        "url": "https://www.allrecipes.com/recipes/"
    },
    {
        "title": "American Council on Exercise (ACE)",
        "content": "Discover evidence-based workout routines, fitness tips, and healthy meal plans for all levels. Provides personalized recommendations and training programs.",
        "url": "https://www.acefitness.org/"
    },
    {
        "title": "BBC News - World Politics",
        "content": "Stay informed with in-depth coverage of politics, national and international news. Offers analysis from a variety of perspectives, along with multimedia content and podcasts.",
        "url": "https://www.bbc.com/news/world/politics"
    },
    {
        "title": "Forever 21",
        "content": "Shop a wide variety of trendy and affordable clothing and accessories for men, women, and children. Offers free shipping and returns on many items.",
        "url": "https://www.forever21.com/"
    },
    {
        "title": "B&H Photo Video",
        "content": "Explore a vast selection of electronics, appliances, and video games. Provides detailed product information, customer reviews, and educational buying guides.",
        "url": "https://www.bhphotovideo.com/"
    },
    {
        "title": "Lonely Planet",
        "content": "Find inspiration and plan your next trip. Offers travel guides, hotel and flight deals, user reviews, and destination recommendations.",
        "url": "https://www.lonelyplanet.com/"
    },
    {
        "title": "Investopedia",
        "content": "Stay informed about personal finance, investing, and the economy. Offers news articles, educational resources, and financial tools.",
        "url": "https://www.investopedia.com/"
    },
    {
        "title": "BBC News",
        "url": "https://www.bbc.com/news",
        "content": "Global news coverage from the BBC.",
    },
    {
        "title": "The New York Times",
        "url": "https://www.nytimes.com",
        "content": "International news with a focus on US affairs.",
    },
    {
        "title": "Khan Academy",
        "url": "https://www.khanacademy.org",
        "content": "Free online educational resources.",
    },
    {
        "title": "GitHub",
        "url": "https://github.com",
        "content": "Version control platform for software development.",
    },
    {
        "title": "Imgur",
        "url": "https://imgur.com",
        "content": "Image hosting and sharing platform.",
    },
    {
        "title": "Wikipedia",
        "url": "https://en.wikipedia.org",
        "content": "Free online encyclopedia.",
    },
    {
        "title": "Spotify",
        "url": "https://www.spotify.com",
        "content": "Music streaming service.",
    },
    {
        "title": "Stack Overflow",
        "url": "https://stackoverflow.com",
        "content": "Programming Q&A website.",
    },
    {
        "title": "National Geographic",
        "url": "https://www.nationalgeographic.com",
        "content": "Magazine and website about science, history, and nature.",
    },
    {
        "title": "YouTube",
        "url": "https://www.youtube.com",
        "content": "Online video sharing platform.",
    },
    {
        "title": "TED Talks",
        "url": "https://www.ted.com",
        "content": "Inspirational talks on a wide range of topics by leading experts.",
    },
    {
        "title": "Coursera",
        "url": "https://www.coursera.org",
        "content": "Online learning platform with courses from top universities and companies.",
    },
    {
        "title": "IMDb",
        "url": "https://www.imdb.com",
        "content": "Website with information about movies, TV shows, and actors.",
    },
    {
        "title": "The Verge",
        "url": "https://www.verge.com",
        "content": "Technology news website covering gadgets, apps, games, and the internet.",
    },
    {
        "title": "Reddit",
        "url": "https://www.reddit.com",
        "content": "Social news aggregation and discussion website.",
    },
    {
        "title": "MIT Technology Review",
        "url": "https://www.technologyreview.com",
        "content": "Magazine and website focusing on the latest developments in technology.",
    },
    {
        "title": "Codecademy",
        "url": "https://www.codecademy.com",
        "content": "Online platform with interactive coding tutorials in various languages.",
    },
    {
        "title": "Duolingo",
        "url": "https://www.duolingo.com",
        "content": "Free language learning app that uses gamification to make learning fun.",
    },
    {
        "title": "arXiv",
        "url": "https://arxiv.org",
        "content": "Online repository for scientific research papers.",
    },
    {
        "title": "Project Gutenberg",
        "url": "https://www.gutenberg.org",
        "content": "Volunteer effort to digitize and archive cultural works, especially books.",
    },
    {
        "title": "GitHub Pages",
        "url": "https://pages.github.com",
        "content": "Service to create and host a website using Git.",
    },
    {
        "title": "Stack Overflow Documentation",
        "url": "https://developer.stackoverflow.com",
        "content": "Collection of technical documentation written by developers.",
    },
    {
        "title": "Khan Academy Kids",
        "url": "https://www.khanacademy.org/kids",
        "content": "Free online learning platform designed for children.",
    },
    {
        "title": "Reuters",
        "url": "https://www.reuters.com",
        "content": "International news agency known for its reliable and unbiased reporting.",
    },
    {
        "title": "CodePen",
        "url": "https://codepen.io",
        "content": "Platform to experiment, test, and showcase front-end code snippets.",
    },
    {
        "title": "Evernote",
        "url": "https://www.evernote.com",
        "content": "App for note-taking, organizing ideas, and managing projects.",
    },
    {
        "title": "Dropbox",
        "url": "https://www.dropbox.com",
        "content": "File hosting service for storing and sharing documents, photos, and videos.",
    },
    {
        "title": "Netflix",
        "url": "https://www.netflix.com",
        "content": "Subscription-based streaming service offering movies, TV shows, documentaries, and more.",
    },
    {
        "title": "Pinterest",
        "url": "https://www.pinterest.com",
        "content": "Visual discovery platform for finding ideas, inspiration, and tutorials.",
    },
    {
        "title": "WhatsApp",
        "url": "https://www.whatsapp.com",
        "content": "Messaging app for sending and receiving messages, photos, videos, and voice notes.",
    },
    {
        "title": "Instagram",
        "url": "https://www.instagram.com",
        "content": "Photo and video sharing social network for connecting with friends and following interests.",
    },
    {
        "title": "Twitter",
        "url": "https://twitter.com",
        "content": "Social media platform for sharing short messages (tweets) and following news and trends.",
    },
    {
        "title": "Tesla",
        "url": "https://www.tesla.com",
        "content": "Electric vehicle and clean energy company focused on sustainable transportation.",
    },
    {
        "title": "WebMD",
        "url": "https://www.webmd.com",
        "content": "Website providing information and resources for health and medical conditions.",
    },
    {
        "title": "Skillshare",
        "url": "https://www.skillshare.com",
        "content": "Online learning platform offering classes on creative and professional skills.",
    },
    {
        "title": "Udacity",
        "url": "https://www.udacity.com",
        "content": "Platform offering online courses and nanodegrees to prepare for tech careers.",
    },
    {
        "title": "Stack Exchange Network",
        "url": "https://stackexchange.com",
        "content": "Network of question-and-answer sites for various topics, including Stack Overflow.",
    },
    {
        "title": "HackerRank",
        "url": "https://www.hackerrank.com",
        "content": "Platform for practicing coding skills, competing in challenges, and preparing for coding interviews.",
    },
    {
        "title": "TED-Ed",
        "url": "https://www.youtube.com/user/TEDEducation",
        "content": "YouTube channel from TED Talks offering educational animated videos on various subjects.",
    },
    {
        "title": "LiveScience",
        "url": "https://www.livescience.com",
        "content": "Website covering science news, discoveries, and research in a clear and engaging way.",
    },
    {
        "title": "Business Insider",
        "url": "https://www.businessinsider.com",
        "content": "Website providing news, analysis, and insights on business, finance, and technology.",
    },
    {
        "title": "Financial Times",
        "url": "https://www.ft.com",
        "content": "Subscription-based financial news website known for its global business coverage.",
    },
    {
        "title": "Quartz",
        "url": "https://qz.com",
        "content": "Website providing innovative and business-focused news on a global scale.",
    },
    {
        "title": "The Guardian",
        "url": "https://www.theguardian.com",
        "content": "British daily newspaper known for its liberal and progressive stance on news.",
    },
    {
        "title": "The Washington Post",
        "url": "https://www.washingtonpost.com",
        "content": "American daily newspaper known for its in-depth reporting and investigative journalism.",
    },
    {
        "title": "The Atlantic",
        "url": "https://www.theatlantic.com",
        "content": "American magazine known for its in-depth articles on politics, society, and culture.",
    },
    {
        "title": "The New Yorker",
        "url": "https://www.newyorker.com",
        "content": "American weekly magazine known for its long-form journalism, fiction, and cartoons.",
    },
    {
        "title": "The Economist (Business)",
        "url": "https://www.economist.com/business",
        "content": "Business section of The Economist website, focusing on global business news and analysis.",
    },
    {
        "title": "Harvard Business Review",
        "url": "https://hbr.org",
        "content": "Management magazine and website offering insights and best practices for business leaders.",
    },
    {
        "title": "Forbes",
        "url": "https://www.forbes.com",
        "content": "Business magazine and website focusing on finance, investing, entrepreneurship, and leadership.",
    },
    {
        "title": "Fast Company",
        "url": "https://www.fastcompany.com",
        "content": "Magazine and website offering articles and insights on innovation, technology, and leadership.",
    },
    {
        "title": "Inc.",
        "url": "https://www.inc.com",
        "content": "Magazine and website focused on entrepreneurship, startups, and small business growth.",
    },
    {
        "title": "Bloomberg",
        "url": "https://www.bloomberg.com",
        "content": "Financial news service and media company providing in-depth coverage of business, finance, and markets.",
    },
    {
        "title": "The Motley Fool",
        "url": "https://www.fool.com",
        "content": "Website offering financial advice, stock market analysis, and investing education.",
    },
    {
        "title": "CNBC",
        "url": "https://www.cnbc.com",
        "content": "Financial news cable television channel and website providing business news, market analysis, and investment information.",
    },
    {
        "title": "NPR",
        "url": "https://www.npr.org",
        "content": "Non-profit media organization providing news, talk shows, and music programming.",
    },
    {
        "title": "BBC World Service",
        "url": "https://www.bbc.com/worldservice",
        "content": "International radio network from the BBC, providing news and information in multiple languages.",
    },
    {
        "title": "The New Yorker Fiction",
        "url": "https://www.newyorker.com/fiction",
        "content": "Fiction section of The New Yorker website, featuring short stories by renowned authors.",
    },
]

inverted_index = build_inverted_index(documents)
