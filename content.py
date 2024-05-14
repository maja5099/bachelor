unid_logo = {       
    "primary_logo": "primary_logo.svg",
    "secondary_logo": "primary_logo.svg",
    "logo_alt": "UNID Studio's logo",
}

ui_icons = {       
    "user_icon": "user.tpl", 
    "admin_icon": "admin.tpl",
    "burger_icon": "burger.tpl",
    "hourglass_icon": "hourglass.tpl",
    "stop_watch_icon": "stop_watch.tpl",
    "open_folder_icon": "open_folder.tpl",
    "closed_folder_icon": "closed_folder.tpl",
    "message": "letter.tpl",
}

selling_points = [       
    {"icon": "heart.tpl", "text": "Tilfredshedsgaranti"},
    {"icon": "discount.tpl", "text": "Studierabat"},
    {"icon": "pen.tpl", "text": "Skræddersyet løsning"},
    {"icon": "chat.tpl", "text": "Hurtig kundeservice"}
]

header_nav_items = [
    {"text": "Services & Priser", "link": "/"},
    {"text": "Om UNID Studio", "link": "/"},
    {"text": "Case portfolio", "link": "/portfolio"},
    {"text": "Kontakt", "link": "/contact"},
]

footer_info = [
    "UNID Studio © 2023",
    "All rights reserved",
    "CVR nr. 43924451",
]

social_media = {       
    "instagram": {"icon": "instagram.tpl", "link": "https://www.instagram.com/unid.studio/"},
    "linkedin": {"icon": "linkedin.tpl", "link": "https://www.linkedin.com/company/unid-studio/"},
}

section_landingpage_hero_content = {       
    "header_text": "Unikke & skræddersyede løsninger",
    "subheader_text": "Vi bestræber os på, at lave unikke og kvalitets løsninger som opfylder hver enkel kundes behov.",
    "button_text": "Kontakt os",
    "image": "digital_design.svg",
}

form_inputs = {
    "username": {
        "label_for": "username",
        "text": "Brugernavn", 
        "icon": "user_circle.tpl", 
        "type": "text",
        "name": "username",
        "inputmode":"text",
        "placeholder": "LoremIpsum",
        "form_info": "",
    },
    "password": {
        "label_for": "pwd",
        "text": "Adgangskode", 
        "icon": "lock.tpl", 
        "type": "password",
        "name": "pwd",
        "inputmode":"text",
        "placeholder": "••••••••",
        "form_info": "Use at least 8 characters, one uppercase, one lowercase and one number.",
    },
    "fname": {
        "label_for": "fname",
        "text": "Fornavn", 
        "icon": "user_name_semi.tpl", 
        "type": "text",
        "name": "fname",
        "inputmode":"text",
        "placeholder": "Lorem",
        "form_info": "",    
    },
    "lname": {
        "label_for": "lname",
        "text": "Efternavn", 
        "icon": "user_name_full.tpl", 
        "type": "text",
        "name": "lname",
        "inputmode":"text",
        "placeholder": "Ipsum",
        "form_info": "",    
    },
    "email": {
        "label_for": "email",
        "text": "Email", 
        "icon": "email.tpl", 
        "type": "email",
        "name": "email",
        "inputmode":"email",
        "placeholder": "loremipsum@mail.com",
        "form_info": "",    
    },
    "phone": {
        "label_for": "phone",
        "text": "Telefon nummer", 
        "icon": "phone.tpl", 
        "type": "tel",
        "name": "phone",
        "inputmode":"tel",
        "placeholder": "12 34 56 67",
        "form_info": "",    
    },
    "website_name": {
        "label_for": "website_name",
        "text": "Navn på din hjemmeside", 
        "icon": "pen_line.tpl", 
        "type": "text",
        "name": "website_name",
        "inputmode":"text",
        "placeholder": "Lorem-Ipsum.dk",
        "form_info": "",    
    },
    "website_url": {
        "label_for": "website_url",
        "text": "URL til din hjemmeside", 
        "icon": "www.tpl", 
        "type": "url",
        "name": "website_url",
        "inputmode":"url",
        "placeholder": "https://www.lorem-ipsum.dk",
        "form_info": "",    
    },
    "full_name": {
        "label_for": "name",
        "text": "Navn", 
        "icon": "user_circle.tpl", 
        "type": "name",
        "name": "name",
        "inputmode":"text",
        "placeholder": "Lorem Ipsum",
        "form_info": "",
    },
}

section_login_content = {
    "header_text": "Log ind",
    "subheader_text": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quae, voluptatum!",
    "error_icon": "exclamation_mark.tpl",
    "button_text": "Log ind",
    "image": "unid_universe.svg",
    "logo": "primary_logo.svg",
}

section_profile_admin = [
    {"icon": "user.tpl", "text": "Oversigt", "link": "/"},
    {"icon": "card.tpl", "text": "Klippekort", "link": "/"},
    {"icon": "letter.tpl", "text": "Beskeder", "link": "/"},
    {"icon": "settings.tpl", "text": "Indstillinger", "link": "/"},
    {"icon": "log_out.tpl", "text": "Log ud", "link": "/"},
]

section_profile_customer = [
    {"icon": "user.tpl", "text": "Oversigt", "link": "/"},
    {"icon": "card.tpl", "text": "Klippekort", "link": "/"},
    {"icon": "cart.tpl", "text": "Tilkøb", "link": "/"},
    {"icon": "education.tpl", "text": "Kurser", "link": "/"},
    {"icon": "letter.tpl", "text": "Beskeder", "link": "/"},
    {"icon": "settings.tpl", "text": "Indstillinger", "link": "/"},
    {"icon": "log_out.tpl", "text": "Log ud", "link": "/"},
]

pricing_default = {
    "clipcard_a": {
        "info": {
            "title": "Klippekort A",
            "hours": "10 timer",
            "discount": "Spar 1.234 DKK",
            "discount_icon": "discount.tpl",
            "price": "12.345 DKK",
        },
        "selling_points": [
            {"icon": "checkmark.tpl", "text": "Selling point 1"},
            {"icon": "checkmark.tpl", "text": "Selling point 2"},
            {"icon": "checkmark.tpl", "text": "Selling point 3"},
            {"icon": "checkmark.tpl", "text": "Selling point 4"},
        ]
    },
    "clipcard_b": {
        "info": {
            "title": "Klippekort B",
            "hours": "20 timer",
            "discount": "Spar 1.234 DKK",
            "discount_icon": "discount.tpl",
            "price": "12.345 DKK",
        },
        "selling_points": [
            {"icon": "checkmark.tpl", "text": "Selling point 1"},
            {"icon": "checkmark.tpl", "text": "Selling point 2"},
            {"icon": "checkmark.tpl", "text": "Selling point 3"},
            {"icon": "checkmark.tpl", "text": "Selling point 4"},
        ]
    }
}

pricing_accent = {
    "clipcard_c": {
        "info": {
            "title": "Klippekort C",
            "hours": "30 timer",
            "discount": "Spar 1.234 DKK",
            "discount_icon": "discount_full.tpl",
            "price": "12.345 DKK",
        },
        "selling_points": [
            {"icon": "checkmark_full.tpl", "text": "Selling point 1"},
            {"icon": "checkmark_full.tpl", "text": "Selling point 2"},
            {"icon": "checkmark_full.tpl", "text": "Selling point 3"},
            {"icon": "checkmark_full.tpl", "text": "Selling point 4"},
            {"icon": "checkmark_full.tpl", "text": "Selling point 5"},
            {"icon": "checkmark_full.tpl", "text": "Selling point 6"},
        ]
    },
}

section_testimonial_content = {
    "header_text": "Det siger vores kunder",
    "subheader_text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi inventore nam eos incidunt, consequatur animi libero modi doloremque esse? Amet qui doloribus nam saepe vitae.",
    "testimonial_icon": "quote.tpl",
    "testimonials": [
        {
            "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi inventore nam eos incidunt, consequatur animi libero modi doloremque esse? Amet qui doloribus nam saepe vitae.",
            "author_name": "Lorem ipsum", 
            "author_job_title": "Lorem ipsum", 
            "author_image": "user.tpl",
        },
        {
            "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi inventore nam eos incidunt, consequatur animi libero modi doloremque esse? Amet qui doloribus nam saepe vitae.",
            "author_name": "Lorem ipsum", 
            "author_job_title": "Lorem ipsum", 
            "author_image": "user.tpl",
        },
    ],
}

