
def rule_sets():

    movement_list = ['new in town', 'brand new here', 'just arrivied', 'new arrival', 'brand new', 'new arrival',
                     'just visiting', 'just arrived', 'limited time', 'limited time only', 'leaving soon',
                     'first time', '1st timer', '1st time', 'first timer', 'stay only', 'few days', 'companionship',
                     'unrushed', 'for the weekend', 'independent', 'work alone', 'working alone', 'fly me', 'fly me to']

    youth_list = ['18 only', '18+', 'virgin', 'barely legal', 'teen', 'teenager', 'prime', 'no pro', 'schoolgirl',
                  'school girl', 'sweet', 'young', 'fantasy', 'very young', 'fresh']

    unconventional_list = ['open mind', 'open minded', 'gfe', 'girlfriend experience', 'girl friend experience',
                           'pornstar experience', 'porn star experience', 'preggo', 'prego', 'pregnant']

    eth_list = ['black beauty', 'asian', 'korean', 'islander', 'caucasian', 'white', 'russia', 'russian', 'exotic',
                'black', 'carribean', 'indian', 'latina', 'columbiana', 'aa', 'brown sugar', 'pocahontas',
                'south east asia', 'south asia', 'east asia', 'south east asian', 'south asian', 'east asian',
                'mixed', 'mulatto', 'milkshake', 'turkish']

    restricted_movement = ['incall only', 'outcall only', 'visit at home', 'visit me at', 'visit me at home'
                     'visit me', 'come to me', 'come to my', 'meet at my']

    job_list = ['group work', 'need models', 'need model', 'agency hiring', 'hiring', 'agency hiring',
                'agency hiring models', 'agency hiring model','agency needs', 'looking for work', 'need work',
                'independent work', 'independent job', 'independently work', 'independent jobs', 'independently working'
                ]

    intent_dict = {'Suspicious Language': movement_list, 'Youth Language': youth_list, 'Ethnic Language': eth_list,
                   'Unconventional Requests': unconventional_list, 'Restricted Movement': restricted_movement,
                   'Job Language': job_list}

    return intent_dict
