# quiz_data.py
# One quiz for every PC part. 10 questions each.
#
# The shape of this file:
#   QUIZZES is a dictionary.      key = part name ("CPU"),  value = a LIST of questions
#   Each question is a dictionary with 4 keys:
#       "question"     the text we show
#       "options"      the answers to pick from (a list)
#       "answer"       the correct one (must match an option EXACTLY)
#       "explanation"  a short "why" we show after the quiz is checked

QUIZZES = {
    # ------------------------------------------------------------
    "CPU": [
        {
            "question": "What is the main job of the CPU?",
            "options": [
                "Store your files permanently",
                "Follow program instructions and do the calculations",
                "Draw the picture on your monitor",
                "Turn wall power into PC power",
            ],
            "answer": "Follow program instructions and do the calculations",
            "explanation": "The CPU is the brain. It reads the instructions of every program and does the calculating.",
        },
        {
            "question": "What is a CPU 'core'?",
            "options": [
                "A cooling fan on top of the CPU",
                "A slot on the motherboard",
                "A mini-processor inside the chip that can work on its own task",
                "A type of memory",
            ],
            "answer": "A mini-processor inside the chip that can work on its own task",
            "explanation": "Each core can handle its own job, so a CPU with 8 cores can work on 8 things at the same time.",
        },
        {
            "question": "Which unit is CPU clock speed measured in?",
            "options": ["Gigabytes (GB)", "Watts (W)", "Pixels", "Gigahertz (GHz)"],
            "answer": "Gigahertz (GHz)",
            "explanation": "GHz tells you how many billions of cycles per second each core can do.",
        },
        {
            "question": "A CPU runs at 4 GHz. Roughly how many cycles does it do every second?",
            "options": ["4 thousand", "4 million", "4 billion", "4 trillion"],
            "answer": "4 billion",
            "explanation": "Giga means billion, so 4 GHz is about 4 billion ticks every second.",
        },
        {
            "question": "Why must the CPU socket match the motherboard socket?",
            "options": [
                "Otherwise the CPU will not physically fit or work",
                "Only so the colours match",
                "Because the case needs it",
                "It does not matter, any CPU fits any board",
            ],
            "answer": "Otherwise the CPU will not physically fit or work",
            "explanation": "Each CPU generation uses a certain socket shape. A wrong match simply will not fit.",
        },
        {
            "question": "Which kind of PC benefits most from a CPU with many cores?",
            "options": [
                "A PC only used for typing a letter",
                "A video editing PC",
                "A PC used only as a music player",
                "A PC that only opens one web page",
            ],
            "answer": "A video editing PC",
            "explanation": "Video editing splits work into many pieces, so more cores finish the job faster.",
        },
        {
            "question": "What does a CPU with 'integrated graphics' let you do?",
            "options": [
                "Run games at the highest settings",
                "Make the CPU run cooler",
                "Store more files",
                "Show a picture without buying a separate graphics card",
            ],
            "answer": "Show a picture without buying a separate graphics card",
            "explanation": "Integrated graphics are a small graphics chip built into the CPU. Fine for school and videos, not for heavy gaming.",
        },
        {
            "question": "What is thermal throttling?",
            "options": [
                "The CPU slows itself down when it gets too hot",
                "The CPU runs faster when it gets hot",
                "A way to save files",
                "A type of cooling fan",
            ],
            "answer": "The CPU slows itself down when it gets too hot",
            "explanation": "Slowing down protects the chip from damage, but you lose speed. Good cooling prevents it.",
        },
        {
            "question": "What does a CPU cooler do?",
            "options": [
                "Makes the CPU smaller",
                "Carries heat away from the CPU",
                "Gives the CPU extra power",
                "Adds more memory",
            ],
            "answer": "Carries heat away from the CPU",
            "explanation": "A heatsink and fan move heat from the chip into the air so the CPU can keep full speed.",
        },
        {
            "question": "Why can a CPU with a lower GHz still be faster than one with a higher GHz?",
            "options": [
                "It can't, higher GHz always wins",
                "Newer designs and more cores can matter more than GHz",
                "Because it costs less",
                "Because it has a bigger box",
            ],
            "answer": "Newer designs and more cores can matter more than GHz",
            "explanation": "GHz is only one clue. How smart the design is and how many cores it has matter too.",
        },
    ],
    # ------------------------------------------------------------
    "GPU": [
        {
            "question": "What is the main job of the GPU?",
            "options": [
                "Draw the images and video you see on screen",
                "Store your games",
                "Supply power to the PC",
                "Connect all the parts together",
            ],
            "answer": "Draw the images and video you see on screen",
            "explanation": "The GPU creates every frame of a game or video and sends it to your monitor.",
        },
        {
            "question": "What is VRAM?",
            "options": [
                "The PC's main memory for programs",
                "Memory on the graphics card used for images and textures",
                "A type of hard drive",
                "A cable for the monitor",
            ],
            "answer": "Memory on the graphics card used for images and textures",
            "explanation": "VRAM holds the pictures the GPU is working on. More VRAM helps at high resolutions.",
        },
        {
            "question": "Why are GPUs good at training AI models?",
            "options": [
                "They have thousands of small cores that work at the same time",
                "They have the most storage",
                "They use the least power",
                "They are always the cheapest part",
            ],
            "answer": "They have thousands of small cores that work at the same time",
            "explanation": "AI needs a huge number of simple calculations at once. That is exactly what a GPU is built for.",
        },
        {
            "question": "Which job needs the strongest GPU?",
            "options": [
                "Writing homework",
                "Browsing the web",
                "Playing new games at high detail",
                "Listening to music",
            ],
            "answer": "Playing new games at high detail",
            "explanation": "Modern games draw millions of pixels many times a second, which is heavy work for a GPU.",
        },
        {
            "question": "Which screen resolution needs the MOST GPU power in games?",
            "options": ["720p", "1080p", "1440p", "4K"],
            "answer": "4K",
            "explanation": "4K has about four times as many pixels as 1080p, so the GPU has much more to draw.",
        },
        {
            "question": "What does FPS measure in a game?",
            "options": [
                "Frames per second, how many pictures are drawn each second",
                "File processing speed",
                "Fan power setting",
                "Free player slots",
            ],
            "answer": "Frames per second, how many pictures are drawn each second",
            "explanation": "Higher FPS feels smoother. Many gamers aim for 60 FPS or more.",
        },
        {
            "question": "What should you check about the PSU before buying a strong GPU?",
            "options": [
                "Its colour",
                "That it has enough watts and the right power connectors",
                "That it is the same brand as the GPU",
                "Nothing, any PSU works",
            ],
            "answer": "That it has enough watts and the right power connectors",
            "explanation": "Strong GPUs use a lot of power and need specific cables from the PSU.",
        },
        {
            "question": "Why check the size of a graphics card before buying?",
            "options": [
                "Bigger cards are always faster",
                "It changes the price of the case",
                "Some cards are very long and may not fit in your case",
                "The monitor must be the same size",
            ],
            "answer": "Some cards are very long and may not fit in your case",
            "explanation": "Always compare the card's length with the space your case allows.",
        },
        {
            "question": "Why does a school and homework PC often not need a separate graphics card?",
            "options": [
                "Schools ban graphics cards",
                "The CPU's built-in graphics can handle light tasks",
                "Homework needs no screen",
                "A separate graphics card would not work",
            ],
            "answer": "The CPU's built-in graphics can handle light tasks",
            "explanation": "That is why our app puts 0% of the budget into the GPU for School & Homework.",
        },
        {
            "question": "What is a good way to compare two graphics cards?",
            "options": [
                "Pick the one with more RGB lights",
                "Pick the one with the biggest box",
                "Pick the most expensive one",
                "Look at independent game benchmarks",
            ],
            "answer": "Look at independent game benchmarks",
            "explanation": "Benchmarks show real FPS in real games, which is much more useful than a spec list.",
        },
    ],
    # ------------------------------------------------------------
    "RAM": [
        {
            "question": "What is RAM used for?",
            "options": [
                "Short-term memory for programs that are open right now",
                "Keeping files forever",
                "Cooling the CPU",
                "Drawing graphics",
            ],
            "answer": "Short-term memory for programs that are open right now",
            "explanation": "RAM is the fast workspace where running programs keep their data.",
        },
        {
            "question": "What happens to the data in RAM when you turn the PC off?",
            "options": [
                "It is saved for ever",
                "It moves to the GPU",
                "It is erased",
                "It moves to the case",
            ],
            "answer": "It is erased",
            "explanation": "RAM forgets everything without power. That is why you must save your work to storage.",
        },
        {
            "question": "In the desk analogy, what does MORE RAM give you?",
            "options": [
                "A faster chair",
                "A bigger desk, so more programs can be open at once",
                "A bigger bookshelf for permanent files",
                "A brighter lamp",
            ],
            "answer": "A bigger desk, so more programs can be open at once",
            "explanation": "More RAM means more room to keep programs and files open without slowing down.",
        },
        {
            "question": "About how much RAM is a good starting point for a modern PC?",
            "options": ["1 GB", "4 MB", "128 GB", "16 GB"],
            "answer": "16 GB",
            "explanation": "16 GB handles everyday use and gaming well. 32 GB is more comfortable for editing and multitasking.",
        },
        {
            "question": "Can you use DDR5 RAM in a motherboard that only supports DDR4?",
            "options": [
                "Yes, always",
                "Only if you push hard",
                "Yes, but it runs slower",
                "No, the RAM type must match the motherboard",
            ],
            "answer": "No, the RAM type must match the motherboard",
            "explanation": "DDR4 and DDR5 have different notches and connections. They are not interchangeable.",
        },
        {
            "question": "What does a higher MHz number on RAM mean?",
            "options": [
                "The memory is a little faster",
                "The memory is bigger",
                "The memory is cooler",
                "The memory is cheaper",
            ],
            "answer": "The memory is a little faster",
            "explanation": "MHz is speed, not size. It usually makes a smaller difference than having enough GB.",
        },
        {
            "question": "What can happen when your PC runs out of RAM?",
            "options": [
                "Nothing at all",
                "The screen turns off",
                "The PC slows down because it starts using storage as overflow",
                "The CPU gets faster",
            ],
            "answer": "The PC slows down because it starts using storage as overflow",
            "explanation": "Storage is much slower than RAM, so the whole PC feels sluggish.",
        },
        {
            "question": "Which task usually needs the MOST RAM?",
            "options": [
                "Reading a text message",
                "Playing a simple 2D game",
                "Editing 4K video",
                "Listening to music",
            ],
            "answer": "Editing 4K video",
            "explanation": "Big video files and many layers need lots of workspace, which is why Video Editing gets 15% for RAM in our app.",
        },
        {
            "question": "Which is faster to read and write: RAM or an SSD?",
            "options": ["An SSD", "They are exactly the same", "It depends on the colour", "RAM"],
            "answer": "RAM",
            "explanation": "RAM is much faster than even the best SSD. That is why programs load into RAM to run.",
        },
        {
            "question": "What does '32GB' mean in '32GB DDR5-6000'?",
            "options": [
                "The speed",
                "The amount of memory (capacity)",
                "The version of the memory",
                "The price",
            ],
            "answer": "The amount of memory (capacity)",
            "explanation": "32GB is the size. DDR5 is the type, and 6000 is the speed in MHz.",
        },
    ],
    # ------------------------------------------------------------
    "Motherboard": [
        {
            "question": "What is the main job of the motherboard?",
            "options": [
                "Store your photos",
                "Make the PC look good",
                "Connect all the parts so they can talk to each other",
                "Cool the graphics card",
            ],
            "answer": "Connect all the parts so they can talk to each other",
            "explanation": "Every part plugs into the motherboard, like buildings connected by roads.",
        },
        {
            "question": "What must match between the motherboard and the CPU?",
            "options": ["The colour", "The socket", "The brand of the case", "The screen size"],
            "answer": "The socket",
            "explanation": "The socket is the shape and pin layout where the CPU sits. A wrong socket means the CPU won't fit.",
        },
        {
            "question": "What are 'traces' on a motherboard?",
            "options": [
                "Tiny copper lines that carry signals",
                "Dust marks",
                "Cooling fans",
                "Screws that hold it in place",
            ],
            "answer": "Tiny copper lines that carry signals",
            "explanation": "Traces are the real roads of the board, carrying data between the parts.",
        },
        {
            "question": "What does a chipset name like 'B650' tell you?",
            "options": [
                "The price of the board",
                "The size of the case",
                "Which features and extras the board supports",
                "How many games it can run",
            ],
            "answer": "Which features and extras the board supports",
            "explanation": "The chipset decides things like how many USB ports, SSD slots and upgrade options you get.",
        },
        {
            "question": "What is a motherboard 'form factor' such as ATX or mini-ITX?",
            "options": [
                "Its brand",
                "Its size and shape",
                "Its colour theme",
                "Its warranty length",
            ],
            "answer": "Its size and shape",
            "explanation": "The form factor decides which cases the board will fit into.",
        },
        {
            "question": "What is the benefit of a board with built-in Wi-Fi?",
            "options": [
                "It makes the CPU faster",
                "It adds more RAM",
                "It connects to wireless internet without an extra adapter",
                "It lowers the power bill",
            ],
            "answer": "It connects to wireless internet without an extra adapter",
            "explanation": "That is why our Wi-Fi board costs a bit more. It saves buying a separate Wi-Fi card.",
        },
        {
            "question": "Where does an M.2 NVMe SSD plug in?",
            "options": [
                "Into the power supply",
                "Into the case fan",
                "Into the graphics card",
                "Into an M.2 slot on the motherboard",
            ],
            "answer": "Into an M.2 slot on the motherboard",
            "explanation": "M.2 SSDs are small sticks that plug straight onto the board. More slots means more room for drives.",
        },
        {
            "question": "Which part normally plugs into the long PCIe x16 slot?",
            "options": ["The graphics card", "The RAM", "The CPU", "The case fan"],
            "answer": "The graphics card",
            "explanation": "The PCIe x16 slot gives the GPU a fast connection to the rest of the PC.",
        },
        {
            "question": "Why does your motherboard choice limit future upgrades?",
            "options": [
                "It decides which CPUs and RAM type you can use",
                "It decides your monitor size",
                "It decides your internet speed",
                "It does not limit anything",
            ],
            "answer": "It decides which CPUs and RAM type you can use",
            "explanation": "A board with a good socket and extra slots gives you more upgrade room later.",
        },
        {
            "question": "What is the BIOS (or UEFI) on a motherboard?",
            "options": [
                "A type of RAM",
                "A cable for the monitor",
                "Software that fills the hard drive",
                "Firmware that starts the PC and holds basic settings",
            ],
            "answer": "Firmware that starts the PC and holds basic settings",
            "explanation": "It is the first thing that runs when you press the power button, before Windows even loads.",
        },
    ],
    # ------------------------------------------------------------
    "Storage": [
        {
            "question": "What is storage used for?",
            "options": [
                "Keeping files, games and Windows even when the power is off",
                "Drawing graphics",
                "Cooling the CPU",
                "Short-term memory for open programs",
            ],
            "answer": "Keeping files, games and Windows even when the power is off",
            "explanation": "Storage is the bookshelf. Things stay there until you delete them.",
        },
        {
            "question": "Which is usually faster, an SSD or an HDD?",
            "options": ["HDD", "They are exactly the same", "SSD", "It depends on the colour"],
            "answer": "SSD",
            "explanation": "An SSD has no moving parts, so it reads and writes much faster.",
        },
        {
            "question": "What does 'NVMe' describe?",
            "options": [
                "A very fast type of SSD",
                "A type of RAM",
                "A kind of case",
                "A cable for the monitor",
            ],
            "answer": "A very fast type of SSD",
            "explanation": "NVMe SSDs connect over fast lanes on the motherboard and are the quickest type you can buy for a normal PC.",
        },
        {
            "question": "What does an HDD have inside that an SSD does not?",
            "options": [
                "Spinning disks and a moving read head",
                "Memory chips",
                "A power supply",
                "A tiny CPU",
            ],
            "answer": "Spinning disks and a moving read head",
            "explanation": "Those moving parts make HDDs slower and more fragile than SSDs.",
        },
        {
            "question": "Why does a PC with an SSD usually start up faster?",
            "options": [
                "It has more RAM",
                "It loads Windows files from storage much faster",
                "It uses less power",
                "It has a better case",
            ],
            "answer": "It loads Windows files from storage much faster",
            "explanation": "Booting means reading lots of files from storage, so faster storage means a faster start.",
        },
        {
            "question": "About how many GB are in 1 TB?",
            "options": ["10", "100", "1,000", "1,000,000"],
            "answer": "1,000",
            "explanation": "Tera means a thousand giga, so 1 TB is about 1,000 GB.",
        },
        {
            "question": "Why do some people still buy an HDD?",
            "options": [
                "It is faster than an SSD",
                "It is cheap for a lot of storage",
                "It uses no power",
                "It never fails",
            ],
            "answer": "It is cheap for a lot of storage",
            "explanation": "HDDs cost less per GB, which is good for big libraries of videos or backups.",
        },
        {
            "question": "What happens to the files on an SSD when you turn the PC off?",
            "options": [
                "They are erased",
                "They move to RAM",
                "They stay saved",
                "They move to the GPU",
            ],
            "answer": "They stay saved",
            "explanation": "Unlike RAM, storage keeps its data without power.",
        },
        {
            "question": "Why is 1 TB a good starting size for a gaming PC?",
            "options": [
                "Games are tiny",
                "Modern games can each take tens of GB or more",
                "Windows needs exactly 1 TB",
                "The GPU needs it",
            ],
            "answer": "Modern games can each take tens of GB or more",
            "explanation": "A few big games can fill 500 GB very quickly.",
        },
        {
            "question": "What is the best way to protect important files from a drive failing?",
            "options": [
                "Buy a faster drive",
                "Keep a backup copy somewhere else, like the cloud or an external drive",
                "Turn the PC off more often",
                "Delete old files",
            ],
            "answer": "Keep a backup copy somewhere else, like the cloud or an external drive",
            "explanation": "Any drive can fail one day. A second copy in another place saves your work.",
        },
    ],
    # ------------------------------------------------------------
    "PSU": [
        {
            "question": "What does the PSU do?",
            "options": [
                "Turns wall power into power the PC parts can use",
                "Stores your files",
                "Draws the pictures",
                "Cools the case",
            ],
            "answer": "Turns wall power into power the PC parts can use",
            "explanation": "The PSU converts the mains power from your wall into the lower voltages the parts need.",
        },
        {
            "question": "What does the 'Watts' number on a PSU tell you?",
            "options": [
                "How big the PSU is",
                "How much power it can deliver",
                "How fast the CPU is",
                "How much memory it has",
            ],
            "answer": "How much power it can deliver",
            "explanation": "A 750W PSU can supply up to 750 watts to all the parts together.",
        },
        {
            "question": "What does an 80+ rating (Bronze, Gold...) tell you?",
            "options": [
                "How long the cable is",
                "The size of the PSU",
                "How loud the fan is",
                "How efficient the PSU is",
            ],
            "answer": "How efficient the PSU is",
            "explanation": "A higher rating means less power is wasted as heat.",
        },
        {
            "question": "Which is more efficient?",
            "options": ["80+ Bronze", "80+ Gold", "They are always the same", "Neither"],
            "answer": "80+ Gold",
            "explanation": "Gold is a higher efficiency level than Bronze, so it wastes less energy.",
        },
        {
            "question": "Why leave some extra wattage (headroom) when choosing a PSU?",
            "options": [
                "So the PSU looks bigger",
                "So you can upgrade later and the PSU is not working at its limit",
                "Because wattage must always be a round number",
                "It is not needed",
            ],
            "answer": "So you can upgrade later and the PSU is not working at its limit",
            "explanation": "Headroom keeps the PSU cooler and quieter, and leaves space for a stronger GPU later.",
        },
        {
            "question": "In a gaming PC, which part usually uses the most power?",
            "options": ["The case", "The RAM", "The SSD", "The graphics card"],
            "answer": "The graphics card",
            "explanation": "High-end GPUs can use hundreds of watts. The CPU is usually second.",
        },
        {
            "question": "What can a cheap, poor-quality PSU do?",
            "options": [
                "Make the PC faster",
                "Damage other parts",
                "Add more RAM",
                "Nothing at all",
            ],
            "answer": "Damage other parts",
            "explanation": "A bad PSU can give unstable power. Never save money here.",
        },
        {
            "question": "Why check the PSU connectors before buying a GPU?",
            "options": [
                "The GPU needs specific power cables, and the PSU must have them",
                "To see the colour",
                "To match the case fans",
                "No reason",
            ],
            "answer": "The GPU needs specific power cables, and the PSU must have them",
            "explanation": "Strong GPUs need special power plugs. If the PSU lacks them, the card can't run.",
        },
        {
            "question": "What does 'modular' mean on a PSU?",
            "options": [
                "It is made of Lego",
                "The cables can be detached so you only use the ones you need",
                "It works with any case",
                "It has no fan",
            ],
            "answer": "The cables can be detached so you only use the ones you need",
            "explanation": "Fewer loose cables means a tidier build and better airflow.",
        },
        {
            "question": "Where does the PSU get its power from?",
            "options": [
                "The wall socket",
                "The motherboard",
                "The CPU",
                "The graphics card",
            ],
            "answer": "The wall socket",
            "explanation": "You plug the PSU into the wall, and it shares the power with every other part through its cables.",
        },
    ],
    # ------------------------------------------------------------
    "Case": [
        {
            "question": "What is the job of the case?",
            "options": [
                "Hold and protect all the parts and help with airflow",
                "Make the CPU faster",
                "Store the games",
                "Supply the power",
            ],
            "answer": "Hold and protect all the parts and help with airflow",
            "explanation": "The case is the house. It keeps parts safe, in place and cool.",
        },
        {
            "question": "Why do many cases have a mesh front panel?",
            "options": [
                "To look old-fashioned",
                "To let more air flow in and cool the parts",
                "To keep the PC quiet",
                "To hold more RAM",
            ],
            "answer": "To let more air flow in and cool the parts",
            "explanation": "Mesh has lots of tiny holes, so fans can pull in plenty of cool air.",
        },
        {
            "question": "What is thermal throttling?",
            "options": [
                "Parts slow themselves down when they get too hot",
                "A fast way to boot the PC",
                "A way to add RAM",
                "A type of case fan",
            ],
            "answer": "Parts slow themselves down when they get too hot",
            "explanation": "A case with poor airflow can cause throttling, which lowers performance.",
        },
        {
            "question": "Which case size is the most common choice for a standard ATX build?",
            "options": ["Mid tower", "Pocket size", "Server rack", "Cube of 5 cm"],
            "answer": "Mid tower",
            "explanation": "Mid towers fit standard boards and graphics cards and leave room for airflow.",
        },
        {
            "question": "What do case fans do?",
            "options": [
                "Make the PC run Windows",
                "Move air through the case to push hot air out",
                "Charge your phone",
                "Store the files",
            ],
            "answer": "Move air through the case to push hot air out",
            "explanation": "Cool air comes in, passes over the parts, and warm air is pushed out.",
        },
        {
            "question": "Why check the clearance (maximum GPU length) of a case?",
            "options": [
                "Some graphics cards are too long for some cases",
                "To check the price",
                "To see if it has Wi-Fi",
                "To match the monitor",
            ],
            "answer": "Some graphics cards are too long for some cases",
            "explanation": "The case's spec sheet lists the longest GPU it can take. Compare it with your card.",
        },
        {
            "question": "Which case feature is mostly about looks rather than performance?",
            "options": [
                "Mesh front panel",
                "Number of fans",
                "Dust filters",
                "RGB lighting",
            ],
            "answer": "RGB lighting",
            "explanation": "RGB looks cool but does not make the PC faster or cooler.",
        },
        {
            "question": "What is good practice to keep a PC cool for years?",
            "options": [
                "Cover all the vents",
                "Clean the dust filters regularly",
                "Put it in a closed cupboard",
                "Never turn it off",
            ],
            "answer": "Clean the dust filters regularly",
            "explanation": "Dust blocks airflow and traps heat, so cleaning filters keeps temperatures low.",
        },
        {
            "question": "What is the best basic airflow plan?",
            "options": [
                "Cool air in at the front, hot air out at the back or top",
                "Hot air in, cool air out",
                "All fans pointing at the wall",
                "No fans at all",
            ],
            "answer": "Cool air in at the front, hot air out at the back or top",
            "explanation": "Hot air rises, so pushing it out of the top or back works with nature.",
        },
        {
            "question": "What should you check about a case and your motherboard BEFORE buying?",
            "options": [
                "That the case supports your motherboard's size",
                "That they are the same colour",
                "That they are from the same shop",
                "Nothing, all cases fit all boards",
            ],
            "answer": "That the case supports your motherboard's size",
            "explanation": "A mini-ITX case cannot hold a full ATX board. Always match the form factor.",
        },
    ],
}
