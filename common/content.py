##############################
#   GLOBALS
global_content = {
    # LOGOS
    "logos": {
        "unid": {
            "primary_logo": "primary_logo.svg",
            "secondary_logo": "primary_logo.svg",
            "logo_alt": "UNID Studio's logo",
        },
    },
    # ICONS
    "ui_icons": {       
        "admin": "admin.svg",
        "burger": "burger.svg",
        "card": "card.svg",
        "documents": "documents.svg",
        "education": "education.svg",
        "error": "exclamation_mark.svg",
        "eye_closed": "eye_closed.svg",
        "eye_open": "eye_open.svg",
        "folder_closed": "folder_closed.svg",
        "folder_open": "folder_open.svg",
        "hourglass": "hourglass.svg",
        "info": "info.svg",
        "message": "letter.svg",
        "stop_watch": "stop_watch.svg",
        "trashcan": "trashcan.svg",
        "user": "user.svg",
    },
    # SOME
    "social_media": {     
        # Unid
        "unid": {     
            "instagram": {"icon": "instagram.svg", "link": "https://www.instagram.com/unid.studio/"},
            "linkedin": {"icon": "linkedin.svg", "link": "https://www.linkedin.com/company/unid-studio/"},
        },
        # Empoyees
        "employees": {     
            "denise": {     
                "instagram": {"icon": "instagram.svg", "link": "https://www.instagram.com/unid.studio/"},
                "linkedin": {"icon": "linkedin.svg", "link": "https://www.linkedin.com/company/unid-studio/"},
            },
            "isabella": {     
                "instagram": {"icon": "instagram.svg", "link": "https://www.instagram.com/unid.studio/"},
                "linkedin": {"icon": "linkedin.svg", "link": "https://www.linkedin.com/company/unid-studio/"},
            },
        },
    },
    # HEADER
    "header": {
        "nav_bar": {
            "nav_items": [
                {"text": "Services & Priser", "link": "/services_and_prices"},
                {"text": "Om UNID Studio", "link": "/about_us"},
                {"text": "Case portfolio", "link": "/portfolio"},
                {"text": "Kontakt", "link": "/contact"},
            ],
        },
        "header_bar": {
            "selling_points": [  
                {"icon": "heart.svg", "text": "Tilfredshedsgaranti"},
                {"icon": "discount.svg", "text": "Studierabat"},
                {"icon": "pen.svg", "text": "Skræddersyet løsning"},
                {"icon": "chat.svg", "text": "Hurtig kundeservice"}
            ],
        },
    },
    # FOOTER
    "footer": {       
        "footer_info": [
            "UNID Studio © 2023",
            "All rights reserved",
            "CVR nr. 43924451",
        ],
    },
    # FORMS
    "form_inputs": {
        # Username
        "username": {
            "label_for": "username",
            "text": "Brugernavn", 
            "icon": "user_circle.svg", 
            "type": "text",
            "name": "username",
            "inputmode":"text",
            "placeholder": "LoremIpsum",
            "form_info": "",
        },
        # Password
        "password": {
            "label_for": "pwd",
            "text": "Adgangskode", 
            "icon": "lock.svg", 
            "type": "password",
            "name": "pwd",
            "inputmode":"text",
            "placeholder": "••••••••",
            "form_info": "Use at least 8 characters, one uppercase, one lowercase and one number.",
        },
        # First name
        "first_name": {
            "label_for": "first_name",
            "text": "Fornavn", 
            "icon": "user_name_semi.svg", 
            "type": "text",
            "name": "first_name",
            "inputmode":"text",
            "placeholder": "Lorem",
            "form_info": "",    
        },
        # Last name
        "last_name": {
            "label_for": "last_name",
            "text": "Efternavn", 
            "icon": "user_name_full.svg", 
            "type": "text",
            "name": "last_name",
            "inputmode":"text",
            "placeholder": "Ipsum",
            "form_info": "",    
        },
        # Email
        "email": {
            "label_for": "email",
            "text": "Email", 
            "icon": "email.svg", 
            "type": "email",
            "name": "email",
            "inputmode":"email",
            "placeholder": "loremipsum@mail.com",
            "form_info": "",    
        },
        # Phone
        "phone": {
            "label_for": "phone",
            "text": "Telefon nummer", 
            "icon": "phone.svg", 
            "type": "tel",
            "name": "phone",
            "inputmode":"tel",
            "placeholder": "12 34 56 67",
            "form_info": "",    
        },
        # Website name
        "website_name": {
            "label_for": "website_name",
            "text": "Navn på din hjemmeside", 
            "icon": "pen_line.svg", 
            "type": "text",
            "name": "website_name",
            "inputmode":"text",
            "placeholder": "Lorem-Ipsum.dk",
            "form_info": "",    
        },
        # Website url
        "website_url": {
            "label_for": "website_url",
            "text": "URL til din hjemmeside", 
            "icon": "www.svg", 
            "type": "url",
            "name": "website_url",
            "inputmode":"url",
            "placeholder": "https://www.lorem-ipsum.dk",
            "form_info": "",    
        },
        # Full name
        "full_name": {
            "label_for": "name",
            "text": "Navn", 
            "icon": "user_circle.svg", 
            "type": "name",
            "name": "name",
            "inputmode":"text",
            "placeholder": "Lorem Ipsum",
            "form_info": "",
        },
    }
}


##############################
#   FRONTPAGE / INDEX
frontpage_content = {
    # HERO SECTION
    "hero_section": {       
        "header_text": "Unikke & skræddersyede løsninger",
        "subheader_text": "Vi bestræber os på, at lave unikke og kvalitets løsninger som opfylder hver enkel kundes behov.",
        "button_text": "Kontakt os",
        "image": "digital_design.svg",
    },
    # TESTIMONIAL SECTION
    "testimonial_section": {
        "header_text": "Det siger vores kunder",
        "subheader_text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi inventore nam eos incidunt, consequatur animi libero modi doloremque esse? Amet qui doloribus nam saepe vitae.",
        "testimonial_icon": "quote.svg",
        # Testiomonials
        "testimonials": [
            {
                "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi inventore nam eos incidunt, consequatur animi libero modi doloremque esse? Amet qui doloribus nam saepe vitae.",
                "author_name": "Lorem ipsum", 
                "author_job_title": "Lorem ipsum", 
                "author_image": "user.svg",
            },
            {
                "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi inventore nam eos incidunt, consequatur animi libero modi doloremque esse? Amet qui doloribus nam saepe vitae.",
                "author_name": "Lorem ipsum", 
                "author_job_title": "Lorem ipsum", 
                "author_image": "user.svg",
            },
        ],
    }
}


##############################
#   SERVICES_AND_PRICES
services_and_prices_content = {
    "header_text": "Services og priser",
    "subheader_text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi inventore nam eos incidunt, consequatur animi libero modi doloremque esse? Amet qui doloribus nam saepe vitae.",
    # SERVICES SECTION
    "services_section": {
        "header_text": "Det kan vi hjælpe dig med",
        "subheader_text": "SERVICES",
        "illustration": "graphic_design.png",
        "illustration_alt": "Illustration af digitalt design",
        # Paragraphs
        "paragraphs": [
            {
                "title": "Websites",
                "text": "Vi bruger WordPress, til at udvikle websites. Hvis du har specifikke ønsker, kan vi i det fleste tilfælde efterleve disse, da vi kan foretage ændringer direkte i koden – og udvikle sitet efter dit ønske og tilpasse det dine behov.",
            },
            {
                "title": "Design af prototyper",
                "text": "Skal du udvikle en app og mangler et design? Eller har du brug for en prototype til dit website? Vi designer professionelle interaktive prototyper i Figma, som kan bruges til brugertests, eller til at sende direkte til din udvikler.",
            },
            {
                "title": "Visuel identitet",
                "text": "Mangler du en visuel identitet, vil være letgenkendelig og skille dig ud fra mængden? Så kan vi hjælpe dig med at skabe en unik identitet. På baggrund af dine ønsker, kan vi udforme et logo, en farvepalette, finde typografier og evt. designe et 5. element, der matcher din virksomeheds identitet – og det budskab du ønsker at sende til kunden.",
            },
            {
                "title": "Grafisk design",
                "text": "Vi har ekspertise indenfor grafisk design, og kan hjælpe med grafisk opsætning af layout, visitkort, brochurer, plakater samt udarbejdelse af SoMe content.",
            },
        ],
    },
    # PRICES SECTION
    "prices_section":{
        "header_text": "Find det rette klippekort til dig",
        "subheader_text": "PRISER",
        "pricings": {
            # Pricing default
            "pricing_default": {
                "clipcard_a": {
                    "info": {
                        "title": "Klippekort",
                        "hours": "10 timer",
                        "discount": "Spar 1.234 DKK",
                        "discount_icon": "discount.svg",
                        "price": "12.345 DKK",
                    },
                    "selling_points": [
                        {"icon": "checkmark.svg", "text": "Selling point 1"},
                        {"icon": "checkmark.svg", "text": "Selling point 2"},
                        {"icon": "checkmark.svg", "text": "Selling point 3"},
                        {"icon": "checkmark.svg", "text": "Selling point 4"},
                    ]
                },
            },
            # Pricing accent
            "pricing_accent": {
                "clipcard_c": {
                    "info": {
                        "title": "Klippekort C",
                        "hours": "30 timer",
                        "discount": "Spar 1.234 DKK",
                        "discount_icon": "discount_full.svg",
                        "price": "12.345 DKK",
                    },
                    "selling_points": [
                        {"icon": "checkmark_full.svg", "text": "Selling point 1"},
                        {"icon": "checkmark_full.svg", "text": "Selling point 2"},
                        {"icon": "checkmark_full.svg", "text": "Selling point 3"},
                        {"icon": "checkmark_full.svg", "text": "Selling point 4"},
                        {"icon": "checkmark_full.svg", "text": "Selling point 5"},
                        {"icon": "checkmark_full.svg", "text": "Selling point 6"},
                    ]
                },
            }
        }
    },
}


##############################
#   ABOUT_US
about_us_content = {
    "header_text": "Om UNID Studio",
    "subheader_text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi inventore nam eos incidunt, consequatur animi libero modi doloremque esse? Amet qui doloribus nam saepe vitae.",
    # HIGHLIGHTS SECTION
    "highlights_section": {
        "header_text": "Lille studio - med store idéer",
        "subheader_text": "OM UNID STUDIO",
        # Highlights
        "highlights": [
            {"illustration": "tools.png", "illustration_alt": "Illustration med kreative værktøjer", "title": "Erfaring", "text": "Vi har stor erfaring indenfor grafisk design og udvikling af websites. Med vores ekspertise, kan vi skræddersy en løsning efter dine ønsker og behov."},
            {"illustration": "book.png", "illustration_alt": "Illustration med en bog", "title": "KEA Ignite", "text": "Vi har et samarbejde med KEA. Hvis du er iværksætter, og går på KEA, så giver vi rabat på vores ydelser."},
            {"illustration": "screen.png", "illustration_alt": "Illustration med en skærm med former på", "title": "Tidligere cases", "text": "Vi vægter tilfredshedgaranti højt, og afslutter ikke en case, før kunden er tilfreds. Vores tidligere cases, kan ses i vores portfolio."},
            {"illustration": "phone_mail.png", "illustration_alt": "Illustration med en telefon og et brev", "title": "Kontakt os", "text": "Lad os høre om din idé. Vi er altid parate, til at hjælpe - og vi skræddersyer gerne én løsning til netop din virksomhed."},
        ],
    },
    # VISION SECTION
    "vision_section": {
        "header_text": "Vores vision",
        "subheader_text": "VISION",
        "introduction_text": "Vi glæder os over at støtte ambitiøse studerende på deres iværksætterrejse.",
        "illustration": "digital_design.svg",
        "illustration_alt": "Illustration af digitalt design",
        # Paragraphs
        "paragraphs": [
            {
                "title": "",
                "text": "Vi tror på, at en stærk start er nøglen til vedvarende vækst – og for at gøre denne start så tilgængelig som muligt, tilbyder vi særlige studierabatter på vores hjemmesidepakker. På den måde ønsker vi at lette byrden for nye forretningsfolk og give dem den nødvendige digitale platform, til at realisere deres visioner.",
            },
            {
                "title": "Hvordan opnår du studierabat?",
                "text": "Jonglerer du med både iværksætteri og uddannelse, så tilbyder vi særlige studierabatter på vores hjemmesidepakker. Det eneste krav vi har til dig, er at du skal være iværksætter samt være indskrevet på en uddannelsesinstitution – og kunne fremvise et gyldigt studiekort. Opnå din studierabat i dag, og lad os sammen bygge fundamentet for din fremtidige succes.",
            },
        ],
    },
    # SKILLS SECTION
    "skills_section": {
        "header_text": "Et udpluk af vores kompetencer",
        "subheader_text": "KOMPETENCER",
        # Skills
        "skills": [
            {"icon": "heart.svg", "title": "Lorem ipsum"},
            {"icon": "heart.svg", "title": "Lorem ipsum"},
            {"icon": "heart.svg", "title": "Lorem ipsum"},
            {"icon": "heart.svg", "title": "Lorem ipsum"},
            {"icon": "heart.svg", "title": "Lorem ipsum"},
            {"icon": "heart.svg", "title": "Lorem ipsum"},
            {"icon": "heart.svg", "title": "Lorem ipsum"},
            {"icon": "heart.svg", "title": "Lorem ipsum"},
            {"icon": "heart.svg", "title": "Lorem ipsum"},
            {"icon": "heart.svg", "title": "Lorem ipsum"},
            {"icon": "heart.svg", "title": "Lorem ipsum"},
            {"icon": "heart.svg", "title": "Lorem ipsum"},
        ],
    },
    # TEAM SECTION
    "team_section": {
        "header_text": "Bag om teamet - hvem er vi?",
        "subheader_text": "TEAM",
        "introduction_text": "Vi er et dedikeret og kreativt team, som har sans for selv de mindste detaljer. For os er det vigtigt at levere den bedste og mest konkurrencedygtige løsning.",
        # Paragraphs
        "paragraphs": [
            {
                "title": "",
                "text": "Vi, Denise & Isabella, står bag UNID Studio. Vi har begge et stort flair, for at designe og udvikle digitale løsninger. Vi har udarbejdet og leveret mange digitale løsninger, og sammen udgør vi et team, hvor vores forskellige færdigheder og kompetencer komplementerer hinanden godt – og danner grobund for kreative løsninger, der skiller sig ud. Når vi udvikler websites og andre løsninger, vægter vi dine ønsker og behov højt, og på baggrund af det, kommer vi med vores forslag på, hvordan vi sammen kan komme i mål – og få udviklet den bedste løsning til lige netop dig.",
            },
        ],
        # Employees
        "employees": [
            {"employee_image": "denise.jpg", "image_alt": "Portræt af Denise", "employee_name": "Denise Dalvang Hansen", "employee_job_title": "Designer & grafiker", "employee_information": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolor, fuga?"},
            {"employee_image": "isabella.jpg", "image_alt": "Portræt af Isabella", "employee_name": "Isabella Hilarius Nielsen", "employee_job_title": "Webudvikler", "employee_information": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolor, fuga?"},
        ],
    },
}

section_login_content = {
    "header_text": "Log ind",
    "subheader_text": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quae, voluptatum!",
    "button_text": "Log ind",
    "image": "unid_universe.svg",
    "logo": "primary_logo.svg",
}

section_signup_content = {
    "header_text": "Opret bruger",
    "subheader_text": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quae, voluptatum!",
    "button_text": "Opret bruger",
}

section_profile_admin = [
    {"icon": "user.svg", "text": "Oversigt", "template": "profile_overview"},
    {"icon": "card.svg", "text": "Klippekort", "template": "profile_admin_clipcard"},
    {"icon": "stop_watch.svg", "text": "Timeregistrering", "template": "profile_admin_hour_registration"},
    {"icon": "letter.svg", "text": "Beskeder", "template": "profile_admin_messages"},
    {"icon": "settings.svg", "text": "Indstillinger", "template": "profile_settings"},
]

section_profile_customer = [
    {"icon": "user.svg", "text": "Oversigt", "template": "profile_overview"},
    {"icon": "card.svg", "text": "Klippekort", "template": "profile_customer_clipcard"},
    {"icon": "cart.svg", "text": "Tilkøb", "template": "profile_additional_purchase"},
    {"icon": "education.svg", "text": "Kurser", "template": "profile_courses"},
    {"icon": "letter.svg", "text": "Beskeder", "template": "profile_customer_messages"},
    {"icon": "settings.svg", "text": "Indstillinger", "template": "profile_settings"},
]





error_content = {
    "title": "Hov! Der skete en fejl",
    "image": "unid_universe.svg",
    "button_link": "/", 
    "button_text": "Gå til forsiden",
    "404": {
        "error_title": "Fejl 404: Siden blev ikke fundet",
        "error_message": "Beklager, men den side, du forsøgte at tilgå, eksisterer ikke. Tjek venligst URL'en og prøv igen, eller kontakt os, hvis problemet fortsætter."
    },
    "500": {
        "error_title": "Fejl 500: Intern Serverfejl",
        "error_message": "Vi beklager, men der er sket en fejl på serveren, som forhindrer udførelsen af din anmodning. Prøv venligst igen senere, eller kontakt os, hvis problemet fortsætter."
    },
}

