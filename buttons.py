

from pyrogram.types import ( InlineKeyboardButton ,
                            InlineKeyboardMarkup ,
                            ReplyKeyboardMarkup ,
                            ReplyKeyboardMarkup)

    
VOICE_SPEECH = InlineKeyboardMarkup(
                                    [
                                        [
                                        InlineKeyboardButton('SPEAK',callback_data='speak')
                                        ]
                                    ]
                                    )
ALLBOTS = InlineKeyboardMarkup(
                                    [
                                        [
                                        InlineKeyboardButton('View All Our Bots ',url='https://t.me/neuraltm/2')
                                        ]
                                    ]
                                    )
APPROACH_BUTTON = InlineKeyboardMarkup(
                                    [
                                        [
                                        InlineKeyboardButton('Professional',callback_data="approach,Professional"),
                                        InlineKeyboardButton('Academic',callback_data="approach,Academic")        
                                        ],
                                        [
                                        InlineKeyboardButton('Direct',callback_data="approach,Direct"),
                                        InlineKeyboardButton('Friendly',callback_data="approach,Friendly")         
                                        ],
                                        [
                                        InlineKeyboardButton('Helpful',callback_data="approach,Helpful")                                                                         ]
                                    ] )
                                                                        
language = ['English', 'Spanish', 'French', 'Italian', 'German', 'Portuguese',
'Polish', 'Ukrainian', 'English', 'Somali', 'Afrikaans', 'Azerbaijani',
'Indonesian', 'Malaysian Malay', 'Malay', 'Javanese', 'Sundanese', 'Bosnian',
'Catalan', 'Czech', 'Chichewa', 'Welsh', 'Danish', 'German', 'Estonian', 'English', 
'English (UK)', 'English (US)', 'Spanish', 'Esperanto', 'Basque', 'French', 'Irish',
'Galician', 'Croatian', 'Xhosa', 'Zulu', 'Icelandic', 'Italian', 'Swahili', 'Haitian Creole', 
'Kurdish', 'Latin', 'Latvian', 'Luxembourgish', 'Lithuanian', 'Hungarian', 'Malagasy', 'Maltese',
'Maori', 'Dutch', 'Norwegian', 'Uzbek', 'Polish', 'Portuguese', 'Romanian', 'Sesotho', 'Albanian',
'Slovak', 'Slovenian', 'Finnish', 'Swedish', 'Tagalog', 'Tatar', 'Turkish', 'Vietnamese', 'Yoruba',
'Greek', 'Belarusian', 'Bulgarian', 'Kyrgyz', 'Kazakh', 'Macedonian', 'Mongolian', 'Russian', 
'Serbian', 'Tajik', 'Ukrainian', 'Georgian', 'Armenian', 'Yiddish', 'Hebrew', 'Uyghur', 'Urdu',
'Arabic', 'Pashto', 'Persian', 'Nepali', 'Marathi', 'Hindi', 'Bengali', 'Punjabi', 'Gujarati',
'Oriya', 'Tamil', 'Telugu', 'Kannada', 'Malayalam', 'Sinhala', 'Thai', 'Lao', 'Burmese', 'Khmer'
, 'Korean', 'Chinese', 'Traditional Chinese', 'Japanese']               
                                    
languages = sorted(list(set(language)))                
                                    
def Languages ():
        pages = [] ; button_limit = 4 ; line_limit = 100 
        for i in languages :
            button = InlineKeyboardButton(i,callback_data = i)
            if len(pages) == 0 or len(pages[-1]) >= line_limit and len(pages[-1][-1]) >= button_limit:
                pages.append([[button]])
            elif len(pages[-1]) == 0 or len(pages[-1][-1]) >= button_limit:
                pages[-1].append([button])
            else:
                pages[-1][-1].append(button)
        page_no = 0
        no_buttons = []
        if len(pages) == 1:
            return pages
        for page in pages:
            page_no += 1
            page_buttons = []
            if page == pages[0]:
                page_buttons.append(
                    InlineKeyboardButton(
                        text="-->",
                        callback_data="tpage+"+str(page_no+1)
                    )
                )
            elif page == pages[-1]:
                page_buttons.append(
                    InlineKeyboardButton(
                        text="<--",
                        callback_data="tpage+"+str(page_no-1)
                    )
                )
            else:
                page_buttons.append(
                    InlineKeyboardButton(
                        text="<--",
                        callback_data="tpage+"+str(page_no-1)
                    )
                )
                page_buttons.append(
                    InlineKeyboardButton(
                        text="-->",
                        callback_data="tpage+"+str(page_no+1)
                    )
                )
            pages[page_no-1].append(page_buttons)
            no_buttons.append(
                InlineKeyboardButton(
                    text=str(page_no),
                    callback_data="tpage+"+str(page_no)
                )
            )
            pages[page_no-1].append(no_buttons)
        return pages        
        
    