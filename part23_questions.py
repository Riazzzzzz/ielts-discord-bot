import random

part2_with_part3 = [

    {
        "part2": (
            "Describe a person you admire.\n"
            "You should say:\n"
            "- who the person is\n"
            "- how you know him or her\n"
            "- what qualities this person has\n"
            "and explain why you admire this person."
        ),
        "part3": [
            "Why do people admire others?",
            "Are role models important for young people?",
            "Do famous people make good role models?",
            "Can admiration influence success?",
            "Is it better to admire family members or celebrities?"
        ]
    },

    {
        "part2": (
            "Describe a person who has had a positive influence on you.\n"
            "You should say:\n"
            "- who the person is\n"
            "- when you met him or her\n"
            "- how he or she influenced you\n"
            "and explain why the influence was positive."
        ),
        "part3": [
            "How can one person influence another?",
            "Why are positive influences important in life?",
            "Can teachers influence students more than parents?",
            "Do peers influence young people negatively sometimes?",
            "How can people become positive role models?"
        ]
    },

    {
        "part2": (
            "Describe a person you enjoy spending time with.\n"
            "You should say:\n"
            "- who the person is\n"
            "- how you know this person\n"
            "- what you usually do together\n"
            "and explain why you enjoy spending time with him or her."
        ),
        "part3": [
            "Why is it important to spend time with others?",
            "Do people prefer being alone or with others today?",
            "How do friendships change over time?",
            "Is it easy to make friends as an adult?",
            "What makes a strong friendship?"
        ]
    },

    {
        "part2": (
            "Describe a family member who is important to you.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what kind of person he or she is\n"
            "- what role this person plays in your life\n"
            "and explain why he or she is important to you."
        ),
        "part3": [
            "How have family roles changed in recent years?",
            "Is family still important in modern society?",
            "Do young people rely less on family now?",
            "Should family members live together?",
            "How can family support affect success?"
        ]
    },

    {
        "part2": (
            "Describe a teacher who helped you a lot.\n"
            "You should say:\n"
            "- who the teacher was\n"
            "- what subject he or she taught\n"
            "- how the teacher helped you\n"
            "and explain why you remember this teacher."
        ),
        "part3": [
            "What qualities make a good teacher?",
            "Is teaching an important profession?",
            "How has education changed in recent years?",
            "Should teachers be strict or friendly?",
            "Do students respect teachers today?"
        ]
    },

    {
        "part2": (
            "Describe a friend you trust.\n"
            "You should say:\n"
            "- who the friend is\n"
            "- how long you have known him or her\n"
            "- why you trust this person\n"
            "and explain how trust affects your friendship."
        ),
        "part3": [
            "Why is trust important in relationships?",
            "Is it easy to trust people today?",
            "Can trust be rebuilt once it is broken?",
            "Do people trust friends more than family?",
            "How does trust develop over time?"
        ]
    },

    {
        "part2": (
            "Describe a person you met recently and liked.\n"
            "You should say:\n"
            "- who the person is\n"
            "- where you met him or her\n"
            "- what you talked about\n"
            "and explain why you liked this person."
        ),
        "part3": [
            "Is first impression important?",
            "How quickly do people judge others?",
            "Can first impressions be wrong?",
            "Is it easier to meet new people today?",
            "What helps people make a good impression?"
        ]
    },

    {
        "part2": (
            "Describe a person who is very good at his or her job.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what job he or she does\n"
            "- why he or she is good at it\n"
            "and explain how this person inspires others."
        ),
        "part3": [
            "What skills are important at work today?",
            "Is experience more important than education?",
            "How can people improve their job skills?",
            "Should people change jobs often?",
            "What makes someone successful at work?"
        ]
    },

    {
        "part2": (
            "Describe a person who is good at making people laugh.\n"
            "You should say:\n"
            "- who the person is\n"
            "- how you know him or her\n"
            "- how he or she makes people laugh\n"
            "and explain why humor is important."
        ),
        "part3": [
            "Why do people enjoy humor?",
            "Is laughter important for health?",
            "Do different cultures have different humor?",
            "Can humor be used at work?",
            "Is it good to laugh at oneself?"
        ]
    },

    {
        "part2": (
            "Describe a person who motivates you.\n"
            "You should say:\n"
            "- who the person is\n"
            "- how you know him or her\n"
            "- how this person motivates you\n"
            "and explain why motivation is important."
        ),
        "part3": [
            "Why do people need motivation?",
            "Can motivation come from within?",
            "How can teachers motivate students?",
            "Is motivation more important than talent?",
            "How does motivation affect success?"
        ]
    },

    {
        "part2": (
            "Describe a famous person you would like to meet.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what he or she is famous for\n"
            "- why you would like to meet this person\n"
            "and explain what you would talk about if you met him or her."
        ),
        "part3": [
            "Why do people admire famous people?",
            "Do celebrities influence young people?",
            "Is fame always a positive thing?",
            "Should famous people behave responsibly?",
            "Do people today value fame more than before?"
        ]
    },

    {
        "part2": (
            "Describe a leader you admire.\n"
            "You should say:\n"
            "- who the leader is\n"
            "- what kind of leader he or she is\n"
            "- what achievements this leader has\n"
            "and explain why you admire this leader."
        ),
        "part3": [
            "What qualities make a good leader?",
            "Are leaders born or made?",
            "Do young people want to be leaders today?",
            "How does leadership affect society?",
            "Can leadership skills be taught?"
        ]
    },

    {
        "part2": (
            "Describe a person who is good at managing people.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what his or her job is\n"
            "- how he or she manages people\n"
            "and explain why good management is important."
        ),
        "part3": [
            "Why is management important in organizations?",
            "What makes a manager successful?",
            "Is managing people a difficult skill?",
            "Should managers be friendly or strict?",
            "How can management affect productivity?"
        ]
    },

    {
        "part2": (
            "Describe a neighbor you know well.\n"
            "You should say:\n"
            "- who the neighbor is\n"
            "- how long you have known him or her\n"
            "- how often you meet\n"
            "and explain how your relationship with this neighbor is."
        ),
        "part3": [
            "Is it important to have good neighbors?",
            "Do people interact with neighbors less today?",
            "How can neighbors help each other?",
            "What problems can neighbors have?",
            "Has neighborhood life changed over time?"
        ]
    },

    {
        "part2": (
            "Describe a person who likes helping others.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what kind of help he or she provides\n"
            "- why this person helps others\n"
            "and explain how helping others benefits society."
        ),
        "part3": [
            "Why do some people like helping others?",
            "Should people help others without expecting anything?",
            "Is volunteering popular among young people?",
            "How can governments encourage people to help others?",
            "Does helping others improve happiness?"
        ]
    },

    {
        "part2": (
            "Describe a person who has an interesting hobby.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what hobby he or she has\n"
            "- how long he or she has had this hobby\n"
            "and explain why you find this hobby interesting."
        ),
        "part3": [
            "Why are hobbies important?",
            "Do people have less free time today?",
            "Are hobbies different for young and old people?",
            "Can hobbies help reduce stress?",
            "Should children be encouraged to have hobbies?"
        ]
    },

    {
        "part2": (
            "Describe a person who taught you an important lesson.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what lesson he or she taught you\n"
            "- when this happened\n"
            "and explain how this lesson affected your life."
        ),
        "part3": [
            "How do people learn important life lessons?",
            "Is learning from experience better than advice?",
            "Who usually teaches children life lessons?",
            "Can mistakes be good teachers?",
            "Do schools teach life skills effectively?"
        ]
    },

    {
        "part2": (
            "Describe a person who is very creative.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what kind of creative work he or she does\n"
            "- how this creativity is shown\n"
            "and explain why creativity is important."
        ),
        "part3": [
            "Why is creativity important in society?",
            "Can creativity be learned?",
            "Are creative people valued at work?",
            "Does technology affect creativity?",
            "Should schools encourage creativity?"
        ]
    },

    {
        "part2": (
            "Describe a person who enjoys traveling.\n"
            "You should say:\n"
            "- who the person is\n"
            "- where he or she likes to travel\n"
            "- how often this person travels\n"
            "and explain why traveling is important to this person."
        ),
        "part3": [
            "Why do people enjoy traveling?",
            "Is traveling more popular now than before?",
            "Does traveling help people understand other cultures?",
            "Are there disadvantages of frequent travel?",
            "Should young people travel more?"
        ]
    },

    {
        "part2": (
            "Describe a person who has achieved success in life.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what success he or she has achieved\n"
            "- how this success was achieved\n"
            "and explain what you can learn from this person."
        ),
        "part3": [
            "How do people define success?",
            "Is success measured by money?",
            "Do successful people work harder than others?",
            "Can success bring happiness?",
            "How can society support success?"
        ]
    },

    {
        "part2": (
            "Describe a person who is good at communication.\n"
            "You should say:\n"
            "- who the person is\n"
            "- how you know him or her\n"
            "- how this person communicates well\n"
            "and explain why good communication is important."
        ),
        "part3": [
            "Why are communication skills important today?",
            "Can communication skills be improved?",
            "Is face-to-face communication better than online communication?",
            "Do young people communicate differently from older people?",
            "How does communication affect relationships?"
        ]
    },

    {
        "part2": (
            "Describe a person you respect for his or her honesty.\n"
            "You should say:\n"
            "- who the person is\n"
            "- how you know this person\n"
            "- how he or she shows honesty\n"
            "and explain why honesty is important."
        ),
        "part3": [
            "Why is honesty important in society?",
            "Is it difficult to be honest sometimes?",
            "Should people always tell the truth?",
            "How does honesty affect trust?",
            "Do people value honesty less today?"
        ]
    },

    {
        "part2": (
            "Describe a person who has changed your way of thinking.\n"
            "You should say:\n"
            "- who the person is\n"
            "- when you met him or her\n"
            "- how this person changed your thinking\n"
            "and explain why this change was important."
        ),
        "part3": [
            "Can people change their opinions easily?",
            "Who influences people's thinking most?",
            "Is it good to change one's way of thinking?",
            "Do young people think differently from older people?",
            "How does education shape thinking?"
        ]
    },

    {
        "part2": (
            "Describe a person who is good at solving problems.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what kind of problems he or she solves\n"
            "- how this person solves problems\n"
            "and explain why problem-solving skills are important."
        ),
        "part3": [
            "Why are problem-solving skills important?",
            "Do schools teach problem-solving effectively?",
            "Are some people better problem-solvers than others?",
            "How can people improve problem-solving skills?",
            "Does technology help solve problems?"
        ]
    },

    {
        "part2": (
            "Describe a person you enjoy talking to.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what you usually talk about\n"
            "- how often you talk to this person\n"
            "and explain why you enjoy these conversations."
        ),
        "part3": [
            "Why do people enjoy talking to others?",
            "Are deep conversations important?",
            "Do people talk less face-to-face today?",
            "Is it easier to talk to friends or family?",
            "How can conversations strengthen relationships?"
        ]
    },

    {
        "part2": (
            "Describe a person who is good at learning new things.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what new things he or she learns\n"
            "- how this person learns quickly\n"
            "and explain why learning new things is important."
        ),
        "part3": [
            "Why is lifelong learning important?",
            "Do young people learn faster than older people?",
            "How can people learn new skills effectively?",
            "Does technology help learning?",
            "Should adults continue formal education?"
        ]
    },

    {
        "part2": (
            "Describe a person who takes good care of others.\n"
            "You should say:\n"
            "- who the person is\n"
            "- who he or she takes care of\n"
            "- how this care is shown\n"
            "and explain why caring for others is important."
        ),
        "part3": [
            "Why is caring for others important in society?",
            "Do people care less about others today?",
            "Who should take care of elderly people?",
            "Is caring a natural quality?",
            "How can societies encourage caring behavior?"
        ]
    },

    {
        "part2": (
            "Describe a person who is very confident.\n"
            "You should say:\n"
            "- who the person is\n"
            "- how this person shows confidence\n"
            "- in what situations this confidence is seen\n"
            "and explain why confidence is important."
        ),
        "part3": [
            "Why is confidence important for success?",
            "Can confidence be developed?",
            "Is confidence different from arrogance?",
            "Do confident people perform better?",
            "How can parents build confidence in children?"
        ]
    },

    {
        "part2": (
            "Describe a person who is important in your community.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what role this person plays\n"
            "- how this person helps the community\n"
            "and explain why this person is important."
        ),
        "part3": [
            "Who are important people in a community?",
            "How can individuals improve their communities?",
            "Is community involvement important today?",
            "Do young people care about community work?",
            "How has community life changed?"
        ]
    },

    {
        "part2": (
            "Describe a person you would like to work with in the future.\n"
            "You should say:\n"
            "- who the person is\n"
            "- what kind of work he or she does\n"
            "- why you would like to work with this person\n"
            "and explain how working together could be beneficial."
        ),
        "part3": [
            "Why is teamwork important at work?",
            "What makes a good colleague?",
            "Is it better to work alone or in a team?",
            "How can people improve teamwork skills?",
            "Does teamwork improve productivity?"
        ]
    },

    {
        "part2": (
            "Describe a place you enjoy visiting.\n"
            "You should say:\n"
            "- where the place is\n"
            "- how often you visit it\n"
            "- what you do there\n"
            "and explain why you enjoy visiting this place."
        ),
        "part3": [
            "Why do people like visiting different places?",
            "Do people prefer familiar places or new places?",
            "How do places affect people's mood?",
            "Is it important to have places for relaxation?",
            "Have people's travel habits changed recently?"
        ]
    },

    {
        "part2": (
            "Describe a place where you like to relax.\n"
            "You should say:\n"
            "- where it is\n"
            "- when you usually go there\n"
            "- what you do there\n"
            "and explain why this place helps you relax."
        ),
        "part3": [
            "Why is relaxation important in modern life?",
            "Do people relax differently today than in the past?",
            "What are common ways to relax?",
            "Should cities have more relaxing places?",
            "Can relaxation improve productivity?"
        ]
    },

    {
        "part2": (
            "Describe a place you visited that was very crowded.\n"
            "You should say:\n"
            "- where the place was\n"
            "- when you visited it\n"
            "- why it was crowded\n"
            "and explain how you felt about the crowd."
        ),
        "part3": [
            "Why do some places become crowded?",
            "Is overcrowding a problem in cities?",
            "How does overcrowding affect daily life?",
            "What can governments do to reduce overcrowding?",
            "Do tourists like crowded places?"
        ]
    },

    {
        "part2": (
            "Describe a place that is special to you.\n"
            "You should say:\n"
            "- where the place is\n"
            "- what you usually do there\n"
            "- why it is special to you\n"
            "and explain how this place makes you feel."
        ),
        "part3": [
            "Why do people become attached to certain places?",
            "Do places hold emotional value?",
            "Should historic places be protected?",
            "Can places influence personal identity?",
            "Do people value places more as they get older?"
        ]
    },

    {
        "part2": (
            "Describe a place you would like to visit in the future.\n"
            "You should say:\n"
            "- where the place is\n"
            "- why you want to visit it\n"
            "- what you would like to do there\n"
            "and explain why this place interests you."
        ),
        "part3": [
            "Why do people like planning future trips?",
            "Does travel broaden people's minds?",
            "Are travel plans different for young and older people?",
            "Is international travel important?",
            "How does tourism affect local people?"
        ]
    },

    {
        "part2": (
            "Describe a place where you grew up.\n"
            "You should say:\n"
            "- where it is\n"
            "- what it was like when you lived there\n"
            "- what changes have happened\n"
            "and explain how this place influenced you."
        ),
        "part3": [
            "How do childhood places affect people?",
            "Do people like to return to their hometown?",
            "How have towns and cities changed over time?",
            "Is it better to grow up in a city or countryside?",
            "Should old neighborhoods be preserved?"
        ]
    },

    {
        "part2": (
            "Describe a public place you often visit.\n"
            "You should say:\n"
            "- what the place is\n"
            "- where it is located\n"
            "- what people usually do there\n"
            "and explain why this place is important."
        ),
        "part3": [
            "Why are public places important?",
            "Should governments invest more in public spaces?",
            "Do people use public places less today?",
            "How can public places bring people together?",
            "What problems can public places face?"
        ]
    },

    {
        "part2": (
            "Describe a place you visited that impressed you.\n"
            "You should say:\n"
            "- where the place was\n"
            "- what you saw there\n"
            "- why it impressed you\n"
            "and explain how it made you feel."
        ),
        "part3": [
            "What makes a place impressive?",
            "Do natural places impress people more than cities?",
            "How does architecture affect people?",
            "Should impressive places be protected?",
            "Do people appreciate beauty more when traveling?"
        ]
    },

    {
        "part2": (
            "Describe a place where people go to exercise.\n"
            "You should say:\n"
            "- what the place is\n"
            "- where it is\n"
            "- who usually goes there\n"
            "and explain why exercise places are important."
        ),
        "part3": [
            "Why is physical exercise important?",
            "Do people exercise more today than in the past?",
            "Should governments provide free exercise facilities?",
            "What prevents people from exercising regularly?",
            "Can public exercise spaces improve health?"
        ]
    },

    {
        "part2": (
            "Describe a place where you like to study or work.\n"
            "You should say:\n"
            "- where it is\n"
            "- what you usually do there\n"
            "- why you prefer this place\n"
            "and explain how this place helps you concentrate."
        ),
        "part3": [
            "Why is the environment important for studying?",
            "Do people work better alone or with others?",
            "How has technology changed work spaces?",
            "Should schools provide better study spaces?",
            "Can surroundings affect productivity?"
        ]
    },

    {
        "part2": (
            "Describe a place where you like to spend time with friends.\n"
            "You should say:\n"
            "- where the place is\n"
            "- how often you go there\n"
            "- what you usually do there\n"
            "and explain why you like spending time with friends in this place."
        ),
        "part3": [
            "Why do people like spending time with friends?",
            "Do social places help build relationships?",
            "Have social activities changed in recent years?",
            "Are friendships stronger when people meet regularly?",
            "Do young people socialize differently from older people?"
        ]
    },

    {
        "part2": (
            "Describe a place you visited during a holiday.\n"
            "You should say:\n"
            "- where the place was\n"
            "- who you went with\n"
            "- what you did there\n"
            "and explain why this holiday was memorable."
        ),
        "part3": [
            "Why are holidays important for people?",
            "Do people prefer short or long holidays?",
            "How do holidays affect mental health?",
            "Are family holidays becoming less common?",
            "Should employers give more holiday time?"
        ]
    },

    {
        "part2": (
            "Describe a place where you learned something new.\n"
            "You should say:\n"
            "- where the place is\n"
            "- what you learned there\n"
            "- how you learned it\n"
            "and explain why this experience was important."
        ),
        "part3": [
            "Can learning happen outside classrooms?",
            "Why is practical learning important?",
            "Do people learn better by doing?",
            "How can places influence learning?",
            "Should schools organize more outdoor learning?"
        ]
    },

    {
        "part2": (
            "Describe a place that has changed a lot over time.\n"
            "You should say:\n"
            "- where the place is\n"
            "- what it was like before\n"
            "- what changes have happened\n"
            "and explain how you feel about these changes."
        ),
        "part3": [
            "Why do places change over time?",
            "Are changes always positive?",
            "How do modern developments affect cities?",
            "Should old buildings be replaced?",
            "How can cities balance development and tradition?"
        ]
    },

    {
        "part2": (
            "Describe a place you visited with your family.\n"
            "You should say:\n"
            "- where the place was\n"
            "- who you went with\n"
            "- what you did together\n"
            "and explain why this visit was special."
        ),
        "part3": [
            "Why is it important for families to spend time together?",
            "Do families travel less today?",
            "What activities are suitable for family trips?",
            "Can travel strengthen family relationships?",
            "Should children travel with their parents?"
        ]
    },

    {
        "part2": (
            "Describe a place where people celebrate festivals.\n"
            "You should say:\n"
            "- what the place is\n"
            "- where it is located\n"
            "- what festivals are celebrated there\n"
            "and explain why festivals are important in this place."
        ),
        "part3": [
            "Why are festivals important in cultures?",
            "Do festivals bring communities together?",
            "Have traditional festivals changed over time?",
            "Should governments support festivals?",
            "Are festivals becoming more commercialized?"
        ]
    },

    {
        "part2": (
            "Describe a place where you feel safe.\n"
            "You should say:\n"
            "- where the place is\n"
            "- why you feel safe there\n"
            "- who you are usually with there\n"
            "and explain why safety is important."
        ),
        "part3": [
            "What makes a place safe?",
            "Is safety a major concern in cities?",
            "Do people feel safer today than before?",
            "How can governments improve public safety?",
            "Does technology help increase safety?"
        ]
    },

    {
        "part2": (
            "Describe a place where people go to shop.\n"
            "You should say:\n"
            "- what the place is\n"
            "- where it is\n"
            "- what people usually buy there\n"
            "and explain why this place is popular."
        ),
        "part3": [
            "Why do people enjoy shopping?",
            "Is online shopping replacing physical stores?",
            "Do shopping habits differ by age?",
            "How does shopping affect the economy?",
            "Should cities control the number of shopping centers?"
        ]
    },

    {
        "part2": (
            "Describe a place you visited that was very quiet.\n"
            "You should say:\n"
            "- where the place was\n"
            "- when you went there\n"
            "- what you did there\n"
            "and explain why the quietness was enjoyable."
        ),
        "part3": [
            "Why do people like quiet places?",
            "Is noise pollution a serious problem?",
            "Do people prefer quiet or lively environments?",
            "How does noise affect health?",
            "Should cities create more quiet zones?"
        ]
    },

    {
        "part2": (
            "Describe a place you would recommend to others.\n"
            "You should say:\n"
            "- where the place is\n"
            "- what people can do there\n"
            "- who would enjoy this place\n"
            "and explain why you would recommend it."
        ),
        "part3": [
            "Why do people recommend places to others?",
            "How do reviews influence travel decisions?",
            "Do people trust online recommendations?",
            "Is word-of-mouth still important?",
            "How can tourism affect recommended places?"
        ]
    },

    {
        "part2": (
            "Describe a place you often visit on weekends.\n"
            "You should say:\n"
            "- where the place is\n"
            "- who you usually go with\n"
            "- what you do there\n"
            "and explain why you like visiting this place on weekends."
        ),
        "part3": [
            "How do people usually spend weekends?",
            "Have weekend activities changed over time?",
            "Is it important to rest on weekends?",
            "Do people prefer staying at home or going out?",
            "How do weekends affect work-life balance?"
        ]
    },

    {
        "part2": (
            "Describe a place related to nature that you enjoy.\n"
            "You should say:\n"
            "- where the place is\n"
            "- what natural features it has\n"
            "- what you usually do there\n"
            "and explain why you enjoy being in this place."
        ),
        "part3": [
            "Why do people enjoy spending time in nature?",
            "Is protecting nature important?",
            "Do people visit natural places less today?",
            "How can governments protect natural areas?",
            "Does nature help reduce stress?"
        ]
    },

    {
        "part2": (
            "Describe a place where you experienced good customer service.\n"
            "You should say:\n"
            "- where the place is\n"
            "- what service you received\n"
            "- how the staff behaved\n"
            "and explain why the service impressed you."
        ),
        "part3": [
            "Why is customer service important for businesses?",
            "How does good service affect customers?",
            "Can customer service be taught?",
            "Do customers expect more today?",
            "Should companies reward good service?"
        ]
    },

    {
        "part2": (
            "Describe a place where you like to go alone.\n"
            "You should say:\n"
            "- where the place is\n"
            "- when you usually go there\n"
            "- what you do there\n"
            "and explain why you like being alone in this place."
        ),
        "part3": [
            "Why do people sometimes like being alone?",
            "Is spending time alone healthy?",
            "Do people today have less time alone?",
            "How can solitude help mental health?",
            "Should children learn to enjoy being alone?"
        ]
    },

    {
        "part2": (
            "Describe a place that is popular with tourists.\n"
            "You should say:\n"
            "- where the place is\n"
            "- why tourists visit it\n"
            "- what people can see or do there\n"
            "and explain how tourism affects this place."
        ),
        "part3": [
            "Why do tourists visit popular places?",
            "Does tourism help or harm local areas?",
            "How can tourism be managed sustainably?",
            "Do tourists behave differently from locals?",
            "Should tourist numbers be limited?"
        ]
    },

    {
        "part2": (
            "Describe a place where you would like to live in the future.\n"
            "You should say:\n"
            "- where the place is\n"
            "- what it is like\n"
            "- why you would like to live there\n"
            "and explain how life there might be different."
        ),
        "part3": [
            "Why do people choose where to live?",
            "Do people prefer cities or smaller towns?",
            "How does location affect lifestyle?",
            "Will people move more in the future?",
            "How important is quality of life?"
        ]
    },

    {
        "part2": (
            "Describe a place where you had an interesting conversation.\n"
            "You should say:\n"
            "- where the place was\n"
            "- who you talked to\n"
            "- what the conversation was about\n"
            "and explain why it was interesting."
        ),
        "part3": [
            "What makes a conversation interesting?",
            "Do surroundings affect conversations?",
            "Are deep conversations becoming rare?",
            "Do people communicate better in certain places?",
            "Can conversations change opinions?"
        ]
    },

    {
        "part2": (
            "Describe a place you visited that was very hot or cold.\n"
            "You should say:\n"
            "- where the place was\n"
            "- when you went there\n"
            "- what the weather was like\n"
            "and explain how the weather affected your experience."
        ),
        "part3": [
            "How does weather affect travel plans?",
            "Do people adapt easily to extreme weather?",
            "Is climate change affecting travel?",
            "Do people prefer warm or cold climates?",
            "How does weather influence daily life?"
        ]
    },

    {
        "part2": (
            "Describe a place you learned about from the internet.\n"
            "You should say:\n"
            "- where the place is\n"
            "- how you learned about it\n"
            "- why it interested you\n"
            "and explain whether you would like to visit it."
        ),
        "part3": [
            "How does the internet influence travel choices?",
            "Do people trust online travel information?",
            "Has the internet changed tourism?",
            "Are virtual tours useful?",
            "Can online content replace real travel?"
        ]
    },

    {
        "part2": (
            "Describe a place where you spent a long time.\n"
            "You should say:\n"
            "- where the place is\n"
            "- why you stayed there for long\n"
            "- what you did during that time\n"
            "and explain how this experience affected you."
        ),
        "part3": [
            "Why do people stay longer in certain places?",
            "Does long-term stay change people's views?",
            "Is slow travel becoming popular?",
            "Do people prefer short visits or long stays?",
            "How does staying longer affect local communities?"
        ]
    },

    {
        "part2": (
            "Describe an event you enjoyed recently.\n"
            "You should say:\n"
            "- what the event was\n"
            "- when and where it happened\n"
            "- who you attended it with\n"
            "and explain why you enjoyed this event."
        ),
        "part3": [
            "Why do people enjoy attending events?",
            "Are social events important in modern life?",
            "Do people prefer small or large events?",
            "How do events help people relax?",
            "Have events changed due to technology?"
        ]
    },

    {
        "part2": (
            "Describe a family event you remember well.\n"
            "You should say:\n"
            "- what the event was\n"
            "- who attended it\n"
            "- what happened during the event\n"
            "and explain why you remember it clearly."
        ),
        "part3": [
            "Why are family events important?",
            "Do families celebrate fewer events today?",
            "What kinds of events bring families together?",
            "How do family traditions change over time?",
            "Are family events important for children?"
        ]
    },

    {
        "part2": (
            "Describe an event that made you happy.\n"
            "You should say:\n"
            "- what the event was\n"
            "- when it happened\n"
            "- why it made you happy\n"
            "and explain how you felt after the event."
        ),
        "part3": [
            "What kinds of events make people happy?",
            "Is happiness related to special occasions?",
            "Do people remember happy events longer?",
            "Can small events make people happy?",
            "How do celebrations affect mood?"
        ]
    },

    {
        "part2": (
            "Describe an event that was important to you.\n"
            "You should say:\n"
            "- what the event was\n"
            "- why it was important\n"
            "- what you did during the event\n"
            "and explain how it influenced you."
        ),
        "part3": [
            "Why are important events remembered for a long time?",
            "Do important events change people?",
            "What kinds of events shape a person’s life?",
            "Do people value personal or public events more?",
            "Can negative events have positive effects?"
        ]
    },

    {
        "part2": (
            "Describe a celebration you attended.\n"
            "You should say:\n"
            "- what the celebration was\n"
            "- where it took place\n"
            "- what people did there\n"
            "and explain why the celebration was enjoyable."
        ),
        "part3": [
            "Why do people celebrate special occasions?",
            "Have celebrations changed over time?",
            "Do celebrations strengthen relationships?",
            "Are traditional celebrations disappearing?",
            "Should governments support cultural celebrations?"
        ]
    },

    {
        "part2": (
            "Describe an event you waited a long time for.\n"
            "You should say:\n"
            "- what the event was\n"
            "- why you waited for it\n"
            "- how you felt when it finally happened\n"
            "and explain why it was worth waiting for."
        ),
        "part3": [
            "Why do people look forward to events?",
            "Does waiting make events more enjoyable?",
            "Are people less patient today?",
            "What events require long preparation?",
            "How does anticipation affect emotions?"
        ]
    },

    {
        "part2": (
            "Describe an event that did not go as planned.\n"
            "You should say:\n"
            "- what the event was\n"
            "- what went wrong\n"
            "- how you dealt with the situation\n"
            "and explain what you learned from it."
        ),
        "part3": [
            "Why do plans sometimes fail?",
            "How should people handle unexpected problems?",
            "Can bad events have positive outcomes?",
            "Are flexible people happier?",
            "Should people always plan events carefully?"
        ]
    },

    {
        "part2": (
            "Describe a public event you attended.\n"
            "You should say:\n"
            "- what the event was\n"
            "- where it was held\n"
            "- what people did there\n"
            "and explain why this event was memorable."
        ),
        "part3": [
            "Why are public events important?",
            "Do public events help build community?",
            "What problems can public events cause?",
            "Should public events be free?",
            "How can public events be better organized?"
        ]
    },

    {
        "part2": (
            "Describe an event that helped you learn something new.\n"
            "You should say:\n"
            "- what the event was\n"
            "- what you learned from it\n"
            "- how it helped you\n"
            "and explain why learning from events is important."
        ),
        "part3": [
            "Can people learn from real-life experiences?",
            "Is experiential learning effective?",
            "Do people learn better from success or failure?",
            "Should schools focus more on real-life learning?",
            "How does experience shape knowledge?"
        ]
    },

    {
        "part2": (
            "Describe an event that you shared with others.\n"
            "You should say:\n"
            "- what the event was\n"
            "- who you shared it with\n"
            "- what you did together\n"
            "and explain why sharing this event was meaningful."
        ),
        "part3": [
            "Why do people like sharing experiences?",
            "Do shared experiences strengthen relationships?",
            "Are shared memories important?",
            "How has social media changed sharing events?",
            "Is it better to experience events alone or with others?"
        ]
    },

    {
        "part2": (
            "Describe an event that made you proud.\n"
            "You should say:\n"
            "- what the event was\n"
            "- where and when it happened\n"
            "- why it made you proud\n"
            "and explain how this event affected you."
        ),
        "part3": [
            "Why do people feel proud of certain events?",
            "Is it good to feel proud of achievements?",
            "Do cultural values affect what people feel proud of?",
            "Can pride motivate people?",
            "Is too much pride harmful?"
        ]
    },

    {
        "part2": (
            "Describe an event where you helped someone.\n"
            "You should say:\n"
            "- what the event was\n"
            "- who you helped\n"
            "- how you helped\n"
            "and explain why helping others is important."
        ),
        "part3": [
            "Why do people help others?",
            "Should helping others be taught in schools?",
            "Do people help strangers less today?",
            "How does helping others benefit society?",
            "Can helping others improve happiness?"
        ]
    },

    {
        "part2": (
            "Describe an event that was challenging for you.\n"
            "You should say:\n"
            "- what the event was\n"
            "- why it was challenging\n"
            "- how you handled it\n"
            "and explain what you learned from it."
        ),
        "part3": [
            "Why do people face challenges in life?",
            "Are challenges necessary for personal growth?",
            "How do people usually overcome difficulties?",
            "Do young people face different challenges today?",
            "Can challenges make people stronger?"
        ]
    },

    {
        "part2": (
            "Describe an event that surprised you.\n"
            "You should say:\n"
            "- what the event was\n"
            "- why it was unexpected\n"
            "- how you reacted\n"
            "and explain why the surprise was memorable."
        ),
        "part3": [
            "Why do people like surprises?",
            "Are surprises always positive?",
            "Do surprises strengthen relationships?",
            "How do cultural differences affect surprises?",
            "Is planning better than being spontaneous?"
        ]
    },

    {
        "part2": (
            "Describe an event that caused a change in your life.\n"
            "You should say:\n"
            "- what the event was\n"
            "- when it happened\n"
            "- how it changed your life\n"
            "and explain why this change was important."
        ),
        "part3": [
            "What kinds of events change people’s lives?",
            "Do people resist change?",
            "Is change easier for young people?",
            "Can sudden events lead to positive change?",
            "How do people adapt to major life changes?"
        ]
    },

    {
        "part2": (
            "Describe an event that involved teamwork.\n"
            "You should say:\n"
            "- what the event was\n"
            "- who you worked with\n"
            "- what role you played\n"
            "and explain why teamwork was important."
        ),
        "part3": [
            "Why is teamwork important?",
            "Do people work better alone or in teams?",
            "What skills are needed for teamwork?",
            "How can teamwork be improved?",
            "Does teamwork lead to better results?"
        ]
    },

    {
        "part2": (
            "Describe an event that was well organized.\n"
            "You should say:\n"
            "- what the event was\n"
            "- who organized it\n"
            "- why it was well organized\n"
            "and explain why organization is important."
        ),
        "part3": [
            "Why is organization important for events?",
            "What problems occur in poorly organized events?",
            "Who is responsible for organizing public events?",
            "Can technology help event organization?",
            "Should people learn organizational skills?"
        ]
    },

    {
        "part2": (
            "Describe an event that taught you a lesson.\n"
            "You should say:\n"
            "- what the event was\n"
            "- what lesson you learned\n"
            "- how it affected you\n"
            "and explain why this lesson was important."
        ),
        "part3": [
            "Do people learn more from mistakes?",
            "Why are life lessons memorable?",
            "Can lessons change behavior?",
            "Should schools teach life lessons?",
            "Do people learn lessons at different stages of life?"
        ]
    },

    {
        "part2": (
            "Describe an event that made you nervous.\n"
            "You should say:\n"
            "- what the event was\n"
            "- why you felt nervous\n"
            "- how you managed your nerves\n"
            "and explain what helped you most."
        ),
        "part3": [
            "Why do people feel nervous in certain situations?",
            "Is nervousness always a bad thing?",
            "How can people reduce nervousness?",
            "Do young people feel more nervous today?",
            "Can experience reduce nervousness?"
        ]
    },

    {
        "part2": (
            "Describe an event that brought people together.\n"
            "You should say:\n"
            "- what the event was\n"
            "- who participated\n"
            "- how people interacted\n"
            "and explain why this event was meaningful."
        ),
        "part3": [
            "Why are events important for social bonding?",
            "Do community events strengthen relationships?",
            "Are people becoming less socially connected?",
            "How can events encourage cooperation?",
            "Should communities organize more events?"
        ]
    },

    {
        "part2": (
            "Describe an event you attended online.\n"
            "You should say:\n"
            "- what the event was\n"
            "- when it happened\n"
            "- why you attended it\n"
            "and explain how it was different from in-person events."
        ),
        "part3": [
            "Why have online events become popular?",
            "Are online events as effective as physical ones?",
            "What are the advantages of online events?",
            "Do online events reduce social interaction?",
            "Will online events remain popular in the future?"
        ]
    },

    {
        "part2": (
            "Describe an event you prepared for carefully.\n"
            "You should say:\n"
            "- what the event was\n"
            "- how you prepared for it\n"
            "- why preparation was important\n"
            "and explain how preparation affected the outcome."
        ),
        "part3": [
            "Why is preparation important?",
            "Do people prepare differently for important events?",
            "Can over-preparation be a problem?",
            "How does preparation reduce stress?",
            "Should schools teach planning skills?"
        ]
    },

    {
        "part2": (
            "Describe an event that was cancelled.\n"
            "You should say:\n"
            "- what the event was\n"
            "- why it was cancelled\n"
            "- how you felt about it\n"
            "and explain what you did instead."
        ),
        "part3": [
            "Why do events get cancelled?",
            "How do people react to cancellations?",
            "Should organizers compensate participants?",
            "Are people more understanding today?",
            "How can cancellations be handled better?"
        ]
    },

    {
        "part2": (
            "Describe an event that involved competition.\n"
            "You should say:\n"
            "- what the event was\n"
            "- who participated\n"
            "- what the result was\n"
            "and explain how competition affected you."
        ),
        "part3": [
            "Is competition good or bad?",
            "Does competition motivate people?",
            "Are people more competitive today?",
            "Should schools encourage competition?",
            "How does competition affect teamwork?"
        ]
    },

    {
        "part2": (
            "Describe an event that helped you relax.\n"
            "You should say:\n"
            "- what the event was\n"
            "- where it took place\n"
            "- why it helped you relax\n"
            "and explain why relaxation events are important."
        ),
        "part3": [
            "Why do people need relaxation?",
            "What kinds of events help people relax?",
            "Do people relax differently today?",
            "Can relaxation improve mental health?",
            "Should workplaces promote relaxation?"
        ]
    },

    {
        "part2": (
            "Describe an event related to culture or tradition.\n"
            "You should say:\n"
            "- what the event was\n"
            "- what traditions were involved\n"
            "- who participated\n"
            "and explain why cultural events are important."
        ),
        "part3": [
            "Why are cultural events important?",
            "Are traditional events disappearing?",
            "Should young people participate in traditions?",
            "How do cultural events preserve identity?",
            "Can traditions change over time?"
        ]
    },

    {
        "part2": (
            "Describe an event that made you laugh.\n"
            "You should say:\n"
            "- what the event was\n"
            "- who was involved\n"
            "- why it was funny\n"
            "and explain why laughter is important."
        ),
        "part3": [
            "Why is laughter important in life?",
            "Do people laugh less today?",
            "Can humor reduce stress?",
            "Is humor culturally different?",
            "Should humor be used in education?"
        ]
    },

    {
        "part2": (
            "Describe an event you would like to experience again.\n"
            "You should say:\n"
            "- what the event was\n"
            "- when it happened\n"
            "- why you want to experience it again\n"
            "and explain what made it special."
        ),
        "part3": [
            "Why do people want to repeat experiences?",
            "Are first experiences more memorable?",
            "Do people value experiences over possessions?",
            "Can repeated events feel the same?",
            "How do memories influence choices?"
        ]
    },

    {
        "part2": (
            "Describe an event that involved learning a skill.\n"
            "You should say:\n"
            "- what the event was\n"
            "- what skill you learned\n"
            "- how it helped you\n"
            "and explain why skill-based events are useful."
        ),
        "part3": [
            "Why are skills important today?",
            "Do people prefer learning skills practically?",
            "Can short events teach useful skills?",
            "Should skill training be compulsory?",
            "How does skill learning affect careers?"
        ]
    },

    {
        "part2": (
            "Describe an event that was stressful.\n"
            "You should say:\n"
            "- what the event was\n"
            "- why it was stressful\n"
            "- how you dealt with stress\n"
            "and explain what you learned from it."
        ),
        "part3": [
            "Why do people experience stress?",
            "Are stressful events unavoidable?",
            "How can people manage stress better?",
            "Do modern lifestyles increase stress?",
            "Can stress sometimes be helpful?"
        ]
    },

    {
        "part2": (
            "Describe an object you use every day.\n"
            "You should say:\n"
            "- what the object is\n"
            "- how long you have had it\n"
            "- how you use it\n"
            "and explain why it is important to you."
        ),
        "part3": [
            "Why do people become attached to everyday objects?",
            "Do people rely too much on objects today?",
            "How have everyday objects changed over time?",
            "Are simple objects sometimes more useful?",
            "Can objects affect people’s lifestyles?"
        ]
    },

    {
        "part2": (
            "Describe an object that was given to you as a gift.\n"
            "You should say:\n"
            "- what the object is\n"
            "- who gave it to you\n"
            "- why it was given to you\n"
            "and explain why this gift is meaningful."
        ),
        "part3": [
            "Why do people give gifts?",
            "Are expensive gifts always better?",
            "How do gifts strengthen relationships?",
            "Do gift-giving traditions differ across cultures?",
            "Is it better to give practical or emotional gifts?"
        ]
    },

    {
        "part2": (
            "Describe an object that is very useful for study or work.\n"
            "You should say:\n"
            "- what the object is\n"
            "- how you use it\n"
            "- why it is useful\n"
            "and explain how it helps you."
        ),
        "part3": [
            "How has technology changed study tools?",
            "Do students depend too much on devices?",
            "Are traditional tools still important?",
            "How can tools improve productivity?",
            "Should schools provide learning tools?"
        ]
    },

    {
        "part2": (
            "Describe an object you bought recently.\n"
            "You should say:\n"
            "- what the object is\n"
            "- why you bought it\n"
            "- how you use it\n"
            "and explain how you feel about this purchase."
        ),
        "part3": [
            "Why do people enjoy buying new things?",
            "Do people make impulsive purchases?",
            "How does advertising influence buying behavior?",
            "Is it better to buy quality or cheap items?",
            "Should people plan their purchases carefully?"
        ]
    },

    {
        "part2": (
            "Describe an object that you keep at home.\n"
            "You should say:\n"
            "- what the object is\n"
            "- where you keep it\n"
            "- how often you use it\n"
            "and explain why you keep it."
        ),
        "part3": [
            "Why do people keep certain objects at home?",
            "Do people keep unnecessary items?",
            "How does clutter affect daily life?",
            "Is minimalism becoming popular?",
            "Should people regularly remove unused items?"
        ]
    },

    {
        "part2": (
            "Describe an object that is important in your culture.\n"
            "You should say:\n"
            "- what the object is\n"
            "- how it is used\n"
            "- why it is important\n"
            "and explain what it represents."
        ),
        "part3": [
            "Why are cultural objects important?",
            "Do traditional objects lose value over time?",
            "How can cultural objects be preserved?",
            "Should young people learn about cultural items?",
            "Can objects represent national identity?"
        ]
    },

    {
        "part2": (
            "Describe an object that helps you relax.\n"
            "You should say:\n"
            "- what the object is\n"
            "- when you use it\n"
            "- how it helps you relax\n"
            "and explain why relaxation is important."
        ),
        "part3": [
            "Why do people need relaxation?",
            "Do objects help people reduce stress?",
            "Are relaxation habits changing?",
            "Can relaxation improve productivity?",
            "Should people make time to relax daily?"
        ]
    },

    {
        "part2": (
            "Describe an object you would like to replace.\n"
            "You should say:\n"
            "- what the object is\n"
            "- why you want to replace it\n"
            "- what you would replace it with\n"
            "and explain how a new object would help you."
        ),
        "part3": [
            "Why do people replace objects?",
            "Do people replace items too quickly?",
            "How does technology encourage replacement?",
            "Is repairing better than replacing?",
            "How can people reduce waste?"
        ]
    },

    {
        "part2": (
            "Describe an object that is easy to use.\n"
            "You should say:\n"
            "- what the object is\n"
            "- how you learned to use it\n"
            "- why it is easy to use\n"
            "and explain why simplicity is important."
        ),
        "part3": [
            "Why is simplicity important in design?",
            "Do people prefer simple or complex products?",
            "How does design affect usability?",
            "Can complex tools discourage users?",
            "Should designers focus on user experience?"
        ]
    },

    {
        "part2": (
            "Describe an object you carry with you every day.\n"
            "You should say:\n"
            "- what the object is\n"
            "- where you carry it\n"
            "- how often you use it\n"
            "and explain why you always carry it."
        ),
        "part3": [
            "Why do people carry personal objects?",
            "Have daily items changed over generations?",
            "Do people depend too much on portable objects?",
            "How do personal objects reflect personality?",
            "Can forgetting important objects cause stress?"
        ]
    },

    {
        "part2": (
            "Describe an object you lost in the past.\n"
            "You should say:\n"
            "- what the object was\n"
            "- when you lost it\n"
            "- how you felt about losing it\n"
            "and explain why it was important to you."
        ),
        "part3": [
            "Why do people feel upset when they lose things?",
            "Are people more careless with objects today?",
            "How can people avoid losing important items?",
            "Do digital objects reduce the risk of loss?",
            "Should children be taught to take care of belongings?"
        ]
    },

    {
        "part2": (
            "Describe an object you repaired instead of replacing.\n"
            "You should say:\n"
            "- what the object was\n"
            "- why it needed repair\n"
            "- how it was repaired\n"
            "and explain why you chose to repair it."
        ),
        "part3": [
            "Why do people prefer repairing objects?",
            "Is repairing cheaper than replacing?",
            "Do people have repair skills today?",
            "How does repairing help the environment?",
            "Should repair skills be taught in schools?"
        ]
    },

    {
        "part2": (
            "Describe an object that makes your daily life easier.\n"
            "You should say:\n"
            "- what the object is\n"
            "- how you use it\n"
            "- how it saves time or effort\n"
            "and explain why it is helpful."
        ),
        "part3": [
            "Why do people like convenience products?",
            "Has technology made life easier?",
            "Do convenience items reduce skills?",
            "Are people becoming too dependent on tools?",
            "How do modern tools change lifestyles?"
        ]
    },

    {
        "part2": (
            "Describe an object you borrowed from someone.\n"
            "You should say:\n"
            "- what the object was\n"
            "- who you borrowed it from\n"
            "- why you needed it\n"
            "and explain how borrowing affected your relationship."
        ),
        "part3": [
            "Why do people borrow things?",
            "Is borrowing common today?",
            "What problems can borrowing cause?",
            "Is borrowing better than buying?",
            "How does trust affect borrowing?"
        ]
    },

    {
        "part2": (
            "Describe an object that is expensive.\n"
            "You should say:\n"
            "- what the object is\n"
            "- why it is expensive\n"
            "- whether it is worth the price\n"
            "and explain how people decide value."
        ),
        "part3": [
            "Why do people buy expensive items?",
            "Do expensive items last longer?",
            "How do people judge quality?",
            "Is brand value important?",
            "Should people spend carefully?"
        ]
    },

    {
        "part2": (
            "Describe an object you use for entertainment.\n"
            "You should say:\n"
            "- what the object is\n"
            "- how often you use it\n"
            "- what kind of entertainment it provides\n"
            "and explain why it is enjoyable."
        ),
        "part3": [
            "Why is entertainment important in life?",
            "Do people spend too much time on entertainment devices?",
            "Has entertainment changed due to technology?",
            "Is passive entertainment harmful?",
            "How can people balance entertainment and work?"
        ]
    },

    {
        "part2": (
            "Describe an object that reminds you of someone.\n"
            "You should say:\n"
            "- what the object is\n"
            "- who it reminds you of\n"
            "- why it is meaningful\n"
            "and explain how objects can hold memories."
        ),
        "part3": [
            "Why do objects carry emotional value?",
            "Do people keep souvenirs for a long time?",
            "Can objects replace memories?",
            "Is sentimental value more important than price?",
            "How do memories affect emotions?"
        ]
    },

    {
        "part2": (
            "Describe an object that you think is beautiful.\n"
            "You should say:\n"
            "- what the object is\n"
            "- what it looks like\n"
            "- why you find it beautiful\n"
            "and explain how beauty affects people."
        ),
        "part3": [
            "Why do people appreciate beautiful objects?",
            "Is beauty subjective?",
            "Do beautiful objects cost more?",
            "How does design influence taste?",
            "Should functionality be more important than beauty?"
        ]
    },

    {
        "part2": (
            "Describe an object used for special occasions.\n"
            "You should say:\n"
            "- what the object is\n"
            "- when it is used\n"
            "- why it is special\n"
            "and explain why people value special items."
        ),
        "part3": [
            "Why do people use special items for occasions?",
            "Do special objects increase enjoyment?",
            "Are traditions connected to special items?",
            "Do people still value formal objects?",
            "How do special items reflect culture?"
        ]
    },

    {
        "part2": (
            "Describe an object that you would like to give as a gift.\n"
            "You should say:\n"
            "- what the object is\n"
            "- who you would give it to\n"
            "- why you chose it\n"
            "and explain why it would be a good gift."
        ),
        "part3": [
            "What makes a gift meaningful?",
            "Is choosing gifts difficult?",
            "Do people prefer practical gifts?",
            "How does gift choice show care?",
            "Should gifts match personality?"
        ]
    },

    {
        "part2": (
            "Describe an object you bought online.\n"
            "You should say:\n"
            "- what the object was\n"
            "- why you bought it online\n"
            "- whether you were satisfied with it\n"
            "and explain your experience."
        ),
        "part3": [
            "Why do people prefer online shopping?",
            "What problems can online shopping cause?",
            "Is online shopping replacing traditional stores?",
            "How can customers avoid online scams?",
            "Will online shopping continue to grow?"
        ]
    },

    {
        "part2": (
            "Describe an object you use for learning a skill.\n"
            "You should say:\n"
            "- what the object is\n"
            "- what skill you are learning\n"
            "- how the object helps you\n"
            "and explain why it is useful."
        ),
        "part3": [
            "Why are learning tools important?",
            "Do tools make learning easier?",
            "Are traditional learning tools still useful?",
            "Should learning tools be affordable?",
            "Can tools replace teachers?"
        ]
    },

    {
        "part2": (
            "Describe an object that saves energy or resources.\n"
            "You should say:\n"
            "- what the object is\n"
            "- how it saves energy or resources\n"
            "- why it is important\n"
            "and explain how it benefits the environment."
        ),
        "part3": [
            "Why is saving energy important?",
            "Do people care enough about the environment?",
            "Can technology help protect the environment?",
            "Should governments promote eco-friendly products?",
            "How can individuals reduce energy use?"
        ]
    },

    {
        "part2": (
            "Describe an object you learned to use as a child.\n"
            "You should say:\n"
            "- what the object was\n"
            "- who taught you to use it\n"
            "- how you felt learning it\n"
            "and explain why it was memorable."
        ),
        "part3": [
            "Why are childhood memories strong?",
            "Do children learn skills faster than adults?",
            "How does early learning affect future abilities?",
            "Should children learn practical skills early?",
            "Do childhood objects shape personality?"
        ]
    },

    {
        "part2": (
            "Describe an object you stopped using.\n"
            "You should say:\n"
            "- what the object was\n"
            "- why you stopped using it\n"
            "- what you use instead\n"
            "and explain how your needs changed."
        ),
        "part3": [
            "Why do people stop using objects?",
            "Does technology make objects outdated quickly?",
            "Do people keep unused items?",
            "Is it hard to change habits?",
            "How do changing needs affect consumption?"
        ]
    },

    {
        "part2": (
            "Describe an object that makes a sound.\n"
            "You should say:\n"
            "- what the object is\n"
            "- what sound it makes\n"
            "- when you hear it\n"
            "and explain how you feel about this sound."
        ),
        "part3": [
            "How do sounds affect emotions?",
            "Are people sensitive to noise today?",
            "What sounds do people find relaxing?",
            "Should noise pollution be controlled?",
            "How does sound affect concentration?"
        ]
    },

    {
        "part2": (
            "Describe an object that you keep for safety.\n"
            "You should say:\n"
            "- what the object is\n"
            "- why it is important for safety\n"
            "- how often it is used\n"
            "and explain why safety objects matter."
        ),
        "part3": [
            "Why is personal safety important?",
            "Do people feel safer today?",
            "What objects improve safety at home?",
            "Should safety education be improved?",
            "How does safety affect quality of life?"
        ]
    },

    {
        "part2": (
            "Describe an object you associate with success.\n"
            "You should say:\n"
            "- what the object is\n"
            "- why it represents success\n"
            "- how it motivates people\n"
            "and explain why symbols of success matter."
        ),
        "part3": [
            "Why do people value symbols of success?",
            "Do symbols motivate achievement?",
            "Is success defined differently today?",
            "Can success be measured by objects?",
            "Should society change its view of success?"
        ]
    },

    {
        "part2": (
            "Describe an object you use to organize your life.\n"
            "You should say:\n"
            "- what the object is\n"
            "- how you use it\n"
            "- why organization is important\n"
            "and explain how it improves your life."
        ),
        "part3": [
            "Why is organization important?",
            "Do people rely too much on planners?",
            "How does organization reduce stress?",
            "Should children learn organization skills?",
            "Can organization improve productivity?"
        ]
    },

    {
        "part2": (
            "Describe an object that you think will be useful in the future.\n"
            "You should say:\n"
            "- what the object is\n"
            "- how it will be used\n"
            "- why it will be important\n"
            "and explain how it may change life."
        ),
        "part3": [
            "How do people predict future needs?",
            "Will future objects simplify life?",
            "Can technology solve future problems?",
            "Are people too dependent on technology?",
            "How should society prepare for future changes?"
        ]
    },

    {
        "part2": (
            "Describe an experience that taught you an important lesson.\n"
            "You should say:\n"
            "- what the experience was\n"
            "- when it happened\n"
            "- what lesson you learned\n"
            "and explain why this lesson was important."
        ),
        "part3": [
            "Do people learn better from experience or advice?",
            "Why are life lessons memorable?",
            "Can negative experiences be useful?",
            "Should schools teach life lessons?",
            "Do people learn lessons at different ages?"
        ]
    },

    {
        "part2": (
            "Describe an experience that made you feel confident.\n"
            "You should say:\n"
            "- what the experience was\n"
            "- why it made you confident\n"
            "- how it affected you\n"
            "and explain why confidence is important."
        ),
        "part3": [
            "How do people build confidence?",
            "Does success increase confidence?",
            "Can confidence change behavior?",
            "Is confidence important for children?",
            "Can confidence be learned?"
        ]
    },

    {
        "part2": (
            "Describe an experience that was difficult but rewarding.\n"
            "You should say:\n"
            "- what the experience was\n"
            "- why it was difficult\n"
            "- why it was rewarding\n"
            "and explain how it changed you."
        ),
        "part3": [
            "Why are difficult experiences valuable?",
            "Do people grow more from challenges?",
            "How do people stay motivated during difficulties?",
            "Are young people less patient today?",
            "Can struggle lead to success?"
        ]
    },

    {
        "part2": (
            "Describe an experience you had for the first time.\n"
            "You should say:\n"
            "- what the experience was\n"
            "- when it happened\n"
            "- how you felt about it\n"
            "and explain why it was memorable."
        ),
        "part3": [
            "Why are first-time experiences memorable?",
            "Do people enjoy trying new things?",
            "Are people afraid of new experiences?",
            "Do first experiences influence future choices?",
            "How do new experiences shape personality?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you helped someone.\n"
            "You should say:\n"
            "- what you did\n"
            "- who you helped\n"
            "- how you felt afterward\n"
            "and explain why helping others is important."
        ),
        "part3": [
            "Why do people help others?",
            "Does helping others benefit the helper?",
            "Should volunteering be encouraged?",
            "Do people help strangers less today?",
            "How does helping others strengthen communities?"
        ]
    },

    {
        "part2": (
            "Describe an experience that made you feel proud.\n"
            "You should say:\n"
            "- what the experience was\n"
            "- why you felt proud\n"
            "- who was involved\n"
            "and explain how it influenced you."
        ),
        "part3": [
            "Why do people feel proud of achievements?",
            "Is pride important for motivation?",
            "Can pride be harmful?",
            "Do cultures value pride differently?",
            "How does pride affect confidence?"
        ]
    },

    {
        "part2": (
            "Describe an experience that changed your opinion.\n"
            "You should say:\n"
            "- what the experience was\n"
            "- what opinion changed\n"
            "- why it changed\n"
            "and explain how experiences shape opinions."
        ),
        "part3": [
            "Can people easily change opinions?",
            "What influences opinions most?",
            "Are experiences more powerful than facts?",
            "Do young people change opinions faster?",
            "How does education affect opinions?"
        ]
    },

    {
        "part2": (
            "Describe an experience that made you nervous.\n"
            "You should say:\n"
            "- what the experience was\n"
            "- why you felt nervous\n"
            "- how you handled it\n"
            "and explain what helped you most."
        ),
        "part3": [
            "Why do people feel nervous?",
            "Is nervousness always negative?",
            "How can people manage nervousness?",
            "Do young people feel more pressure today?",
            "Can experience reduce anxiety?"
        ]
    },

    {
        "part2": (
            "Describe an experience that made you happy.\n"
            "You should say:\n"
            "- what the experience was\n"
            "- why it made you happy\n"
            "- how you felt afterward\n"
            "and explain why happiness is important."
        ),
        "part3": [
            "What experiences bring happiness?",
            "Is happiness linked to success?",
            "Do people remember happy experiences longer?",
            "Can simple experiences bring happiness?",
            "How does happiness affect health?"
        ]
    },

    {
        "part2": (
            "Describe an experience you shared with others.\n"
            "You should say:\n"
            "- what the experience was\n"
            "- who you shared it with\n"
            "- why it was meaningful\n"
            "and explain how shared experiences affect relationships."
        ),
        "part3": [
            "Why are shared experiences important?",
            "Do shared memories strengthen bonds?",
            "Has technology changed shared experiences?",
            "Is it better to experience things alone or together?",
            "How do shared experiences build trust?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you worked as part of a team.\n"
            "You should say:\n"
            "- what the situation was\n"
            "- who you worked with\n"
            "- what your role was\n"
            "and explain why teamwork was important."
        ),
        "part3": [
            "Why is teamwork important?",
            "Do people work better in teams or alone?",
            "What skills are needed for teamwork?",
            "How can teamwork improve productivity?",
            "What problems can arise in teamwork?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you solved a problem.\n"
            "You should say:\n"
            "- what the problem was\n"
            "- how you solved it\n"
            "- what the result was\n"
            "and explain why problem-solving is important."
        ),
        "part3": [
            "Why is problem-solving an important skill?",
            "Do schools teach problem-solving effectively?",
            "How do people usually approach problems?",
            "Can teamwork help solve problems?",
            "How does problem-solving affect confidence?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you made a quick decision.\n"
            "You should say:\n"
            "- what the situation was\n"
            "- why you had to decide quickly\n"
            "- what happened afterward\n"
            "and explain how you felt about it."
        ),
        "part3": [
            "Is making quick decisions risky?",
            "When are quick decisions necessary?",
            "Do young people make decisions faster?",
            "Should decisions always be carefully planned?",
            "How can decision-making skills be improved?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you learned something new.\n"
            "You should say:\n"
            "- what you learned\n"
            "- how you learned it\n"
            "- why it was useful\n"
            "and explain how learning affects personal growth."
        ),
        "part3": [
            "Why is lifelong learning important?",
            "How do people prefer to learn new skills?",
            "Does technology help learning?",
            "Are people learning more today?",
            "How does learning change thinking?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you helped solve a conflict.\n"
            "You should say:\n"
            "- what the conflict was\n"
            "- how you helped\n"
            "- what the outcome was\n"
            "and explain why conflict resolution matters."
        ),
        "part3": [
            "Why do conflicts occur?",
            "How can conflicts be resolved peacefully?",
            "Is conflict sometimes necessary?",
            "Do people avoid conflicts today?",
            "Should schools teach conflict resolution?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you felt under pressure.\n"
            "You should say:\n"
            "- what caused the pressure\n"
            "- how you handled it\n"
            "- what you learned\n"
            "and explain how pressure affects performance."
        ),
        "part3": [
            "What causes pressure in modern life?",
            "Does pressure improve performance?",
            "How do people manage stress?",
            "Are young people under more pressure today?",
            "Can pressure be beneficial?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you achieved a goal.\n"
            "You should say:\n"
            "- what the goal was\n"
            "- how you achieved it\n"
            "- why it was important\n"
            "and explain how goal-setting affects success."
        ),
        "part3": [
            "Why is setting goals important?",
            "Do people set realistic goals?",
            "How can goals motivate people?",
            "Should children be taught goal-setting?",
            "Can goals change over time?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you failed at something.\n"
            "You should say:\n"
            "- what you failed at\n"
            "- why it happened\n"
            "- what you learned\n"
            "and explain how failure affects personal growth."
        ),
        "part3": [
            "Why do people fear failure?",
            "Can failure lead to success?",
            "How should parents react to children's failures?",
            "Is failure necessary for learning?",
            "How do cultures view failure?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you had to be patient.\n"
            "You should say:\n"
            "- what the situation was\n"
            "- why patience was needed\n"
            "- how you felt\n"
            "and explain why patience is important."
        ),
        "part3": [
            "Why is patience important?",
            "Are people less patient today?",
            "How can patience be developed?",
            "Does technology reduce patience?",
            "Is patience related to success?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you felt surprised.\n"
            "You should say:\n"
            "- what surprised you\n"
            "- why it was unexpected\n"
            "- how you reacted\n"
            "and explain why surprises are memorable."
        ),
        "part3": [
            "Why do people enjoy surprises?",
            "Are surprises always positive?",
            "Do surprises create strong memories?",
            "Should surprises be planned?",
            "How do surprises affect emotions?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you had to wait for something important.\n"
            "You should say:\n"
            "- what you were waiting for\n"
            "- how long you waited\n"
            "- how you felt during the wait\n"
            "and explain why waiting was difficult or meaningful."
        ),
        "part3": [
            "Why do people find waiting difficult?",
            "Does waiting teach patience?",
            "How can waiting affect emotions?",
            "Are people less willing to wait today?",
            "Can waiting improve decision-making?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you tried something challenging.\n"
            "You should say:\n"
            "- what the challenge was\n"
            "- why you tried it\n"
            "- how you felt afterward\n"
            "and explain why challenges are important."
        ),
        "part3": [
            "Why do people take on challenges?",
            "Do challenges help build confidence?",
            "Should children be encouraged to face challenges?",
            "Are people today afraid of challenges?",
            "How do challenges affect personal growth?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you followed rules strictly.\n"
            "You should say:\n"
            "- what the situation was\n"
            "- what rules you followed\n"
            "- why the rules were important\n"
            "and explain how rules affect behavior."
        ),
        "part3": [
            "Why do societies need rules?",
            "Are rules always necessary?",
            "Do people follow rules willingly?",
            "Can strict rules be harmful?",
            "How should rules be enforced?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you broke a rule.\n"
            "You should say:\n"
            "- what rule you broke\n"
            "- why you broke it\n"
            "- what happened afterward\n"
            "and explain what you learned from it."
        ),
        "part3": [
            "Why do people break rules?",
            "Are rules more important for children?",
            "Should rule-breaking always be punished?",
            "Can breaking rules lead to change?",
            "How do rules reflect social values?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you had to adapt to change.\n"
            "You should say:\n"
            "- what changed\n"
            "- why it changed\n"
            "- how you adapted\n"
            "and explain why adaptability is important."
        ),
        "part3": [
            "Why is adaptability important today?",
            "Do people resist change?",
            "How can people become more adaptable?",
            "Is change usually positive?",
            "How does change affect mental health?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you managed your time well.\n"
            "You should say:\n"
            "- what you had to do\n"
            "- how you planned your time\n"
            "- what the result was\n"
            "and explain why time management matters."
        ),
        "part3": [
            "Why is time management important?",
            "Do people manage time better today?",
            "Should time management be taught in school?",
            "How does poor time management affect life?",
            "Can technology help manage time?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you felt relaxed.\n"
            "You should say:\n"
            "- what you were doing\n"
            "- where you were\n"
            "- why you felt relaxed\n"
            "and explain why relaxation is important."
        ),
        "part3": [
            "Why is relaxation important?",
            "How do people relax today?",
            "Do people relax less than before?",
            "Can relaxation improve productivity?",
            "How does relaxation affect mental health?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you received useful advice.\n"
            "You should say:\n"
            "- who gave you the advice\n"
            "- what the advice was\n"
            "- why it was useful\n"
            "and explain how advice can influence decisions."
        ),
        "part3": [
            "Why do people give advice?",
            "Is advice always helpful?",
            "Do people follow advice easily?",
            "Who gives the best advice?",
            "How does advice affect relationships?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you felt disappointed.\n"
            "You should say:\n"
            "- what caused the disappointment\n"
            "- how you reacted\n"
            "- what you learned\n"
            "and explain how disappointment affects people."
        ),
        "part3": [
            "Why do people feel disappointed?",
            "How can disappointment be handled positively?",
            "Do expectations cause disappointment?",
            "Is disappointment necessary for growth?",
            "How do cultures deal with disappointment?"
        ]
    },

    {
        "part2": (
            "Describe an experience where you overcame a fear.\n"
            "You should say:\n"
            "- what fear you had\n"
            "- how you overcame it\n"
            "- how you felt afterward\n"
            "and explain why overcoming fear is important."
        ),
        "part3": [
            "Why do people have fears?",
            "Is fear useful?",
            "How can people overcome fear?",
            "Are fears learned or natural?",
            "How does overcoming fear affect confidence?"
        ]
    },

    {
        "part2": (
            "Describe an important decision you made in your life.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- when you made it\n"
            "- why it was important\n"
            "and explain how it affected your life."
        ),
        "part3": [
            "Why are some decisions more difficult than others?",
            "Do people make better decisions as they grow older?",
            "How do emotions affect decision-making?",
            "Should people seek advice before making decisions?",
            "Can one decision change a person’s life?"
        ]
    },

    {
        "part2": (
            "Describe a decision you made quickly.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why you made it quickly\n"
            "- what happened afterward\n"
            "and explain whether it was a good decision."
        ),
        "part3": [
            "Are quick decisions usually risky?",
            "When is it better to decide quickly?",
            "Do young people make decisions faster?",
            "Should decisions always be planned carefully?",
            "How can people improve decision-making skills?"
        ]
    },

    {
        "part2": (
            "Describe a decision you regretted.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why you regretted it\n"
            "- what you learned from it\n"
            "and explain how regret influences future decisions."
        ),
        "part3": [
            "Why do people regret decisions?",
            "Is regret a useful emotion?",
            "Can people learn from bad decisions?",
            "Do people regret missed opportunities more?",
            "How can regret be reduced?"
        ]
    },

    {
        "part2": (
            "Describe a decision that required careful planning.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why planning was necessary\n"
            "- what the outcome was\n"
            "and explain why planning matters."
        ),
        "part3": [
            "Why is planning important in decision-making?",
            "Do people plan less today?",
            "Can too much planning cause delays?",
            "How does planning reduce risk?",
            "Should children learn planning skills?"
        ]
    },

    {
        "part2": (
            "Describe a decision you made with help from others.\n"
            "You should say:\n"
            "- who helped you\n"
            "- what decision you made\n"
            "- why their help was useful\n"
            "and explain why advice matters."
        ),
        "part3": [
            "Why do people ask for advice?",
            "Who gives better advice: family or friends?",
            "Is expert advice always reliable?",
            "Do people depend too much on others’ opinions?",
            "How does advice affect confidence?"
        ]
    },

    {
        "part2": (
            "Describe a decision that involved risk.\n"
            "You should say:\n"
            "- what the risk was\n"
            "- why you took it\n"
            "- what the result was\n"
            "and explain how people evaluate risk."
        ),
        "part3": [
            "Why do some people enjoy taking risks?",
            "Are risks necessary for success?",
            "How do people assess risks?",
            "Are young people more willing to take risks?",
            "Should risks be encouraged?"
        ]
    },

    {
        "part2": (
            "Describe a decision you postponed.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why you delayed it\n"
            "- what happened later\n"
            "and explain why people postpone decisions."
        ),
        "part3": [
            "Why do people delay decisions?",
            "Is postponing decisions harmful?",
            "How can people avoid procrastination?",
            "Do complex decisions take longer?",
            "Should deadlines be enforced?"
        ]
    },

    {
        "part2": (
            "Describe a decision related to your education.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why you made it\n"
            "- how it affected your studies\n"
            "and explain why education decisions matter."
        ),
        "part3": [
            "How important are education-related decisions?",
            "Do students receive enough guidance?",
            "Should parents influence education choices?",
            "Are education decisions stressful?",
            "How does education shape careers?"
        ]
    },

    {
        "part2": (
            "Describe a decision related to your career.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why it was difficult\n"
            "- what the result was\n"
            "and explain how career decisions affect life."
        ),
        "part3": [
            "Why are career decisions challenging?",
            "Do people change careers more often today?",
            "Should salary influence career choice?",
            "How does job satisfaction affect decisions?",
            "Can career mistakes be corrected?"
        ]
    },

    {
        "part2": (
            "Describe a decision you made that benefited others.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- who benefited from it\n"
            "- why it was helpful\n"
            "and explain why decisions can impact society."
        ),
        "part3": [
            "Should people consider others when making decisions?",
            "Do personal decisions affect society?",
            "Why are ethical decisions important?",
            "Can one decision inspire others?",
            "How can decision-making be more responsible?"
        ]
    },

    {
        "part2": (
            "Describe a decision you made that changed your routine.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why you made it\n"
            "- how your routine changed\n"
            "and explain how habits influence daily life."
        ),
        "part3": [
            "Why are habits hard to change?",
            "Do routines improve productivity?",
            "Can routines limit creativity?",
            "How can people develop good habits?",
            "Should routines be flexible?"
        ]
    },

    {
        "part2": (
            "Describe a decision you made under pressure.\n"
            "You should say:\n"
            "- what the situation was\n"
            "- why you felt pressure\n"
            "- what decision you made\n"
            "and explain how pressure affects decisions."
        ),
        "part3": [
            "How does pressure affect thinking?",
            "Do people make poor decisions under pressure?",
            "How can pressure be managed?",
            "Are some people better at handling pressure?",
            "Does experience reduce pressure?"
        ]
    },

    {
        "part2": (
            "Describe a decision you made based on advice.\n"
            "You should say:\n"
            "- who gave the advice\n"
            "- what the advice was\n"
            "- why you followed it\n"
            "and explain how advice influences decisions."
        ),
        "part3": [
            "Why do people rely on advice?",
            "Is professional advice more valuable?",
            "Should advice always be followed?",
            "How does advice affect independence?",
            "Can advice be misleading?"
        ]
    },

    {
        "part2": (
            "Describe a decision you made alone.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why you decided alone\n"
            "- how you felt afterward\n"
            "and explain why independence matters."
        ),
        "part3": [
            "Why do people prefer making decisions alone?",
            "Is independence important in life?",
            "Do people feel confident deciding alone?",
            "Can independence lead to mistakes?",
            "How does independence affect responsibility?"
        ]
    },

    {
        "part2": (
            "Describe a decision that affected your family.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why it affected your family\n"
            "- how your family reacted\n"
            "and explain why family decisions are important."
        ),
        "part3": [
            "Why are family decisions challenging?",
            "Who usually makes decisions in families?",
            "Should children be involved in family decisions?",
            "How do family decisions affect relationships?",
            "Do cultural values influence family decisions?"
        ]
    },

    {
        "part2": (
            "Describe a decision you changed later.\n"
            "You should say:\n"
            "- what the original decision was\n"
            "- why you changed it\n"
            "- what the result was\n"
            "and explain why people change decisions."
        ),
        "part3": [
            "Why do people change decisions?",
            "Is changing decisions a sign of weakness?",
            "Can flexibility improve outcomes?",
            "Should people stick to decisions longer?",
            "How do people evaluate new information?"
        ]
    },

    {
        "part2": (
            "Describe a decision involving money.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why money was involved\n"
            "- what the outcome was\n"
            "and explain how people manage finances."
        ),
        "part3": [
            "Why is financial decision-making important?",
            "Do people manage money well?",
            "Should financial education be compulsory?",
            "How does income affect decisions?",
            "Are people more careful with money today?"
        ]
    },

    {
        "part2": (
            "Describe a decision related to health.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why it was important\n"
            "- how it affected your health\n"
            "and explain why health decisions matter."
        ),
        "part3": [
            "Why are health decisions important?",
            "Do people take health seriously?",
            "Should governments promote healthy choices?",
            "How does lifestyle affect health decisions?",
            "Can technology improve health awareness?"
        ]
    },

    {
        "part2": (
            "Describe a decision that involved learning a new skill.\n"
            "You should say:\n"
            "- what skill you decided to learn\n"
            "- why you chose it\n"
            "- how it helped you\n"
            "and explain why skill decisions are valuable."
        ),
        "part3": [
            "Why is learning new skills important?",
            "Do people learn skills more easily when young?",
            "Should skills be updated regularly?",
            "How does skill learning affect careers?",
            "Can skills increase confidence?"
        ]
    },

    {
        "part2": (
            "Describe a decision that made your life easier.\n"
            "You should say:\n"
            "- what the decision was\n"
            "- why it helped you\n"
            "- how life improved\n"
            "and explain how good decisions improve quality of life."
        ),
        "part3": [
            "What makes a decision good?",
            "Do people reflect on past decisions?",
            "Can small decisions have big effects?",
            "Should people analyze decisions deeply?",
            "How do good decisions shape life?"
        ]
    },

    {
        "part2": (
            "Describe a piece of technology you use every day.\n"
            "You should say:\n"
            "- what the technology is\n"
            "- how you use it\n"
            "- why it is important to you\n"
            "and explain how it affects your daily life."
        ),
        "part3": [
            "Why do people depend heavily on technology?",
            "Does technology save time or waste time?",
            "How has technology changed communication?",
            "Are people becoming too dependent on technology?",
            "How would life be without modern technology?"
        ]
    },

    {
        "part2": (
            "Describe a social media platform you often use.\n"
            "You should say:\n"
            "- what the platform is\n"
            "- how you use it\n"
            "- why it is popular\n"
            "and explain its impact on communication."
        ),
        "part3": [
            "Why is social media popular?",
            "Does social media improve relationships?",
            "What problems can social media cause?",
            "Should social media use be controlled?",
            "How will social media change in the future?"
        ]
    },

    {
        "part2": (
            "Describe a website that you find useful.\n"
            "You should say:\n"
            "- what the website is\n"
            "- how you use it\n"
            "- why it is useful\n"
            "and explain how websites help people today."
        ),
        "part3": [
            "Why do people rely on websites for information?",
            "Are websites more reliable than books?",
            "How can people judge online information?",
            "Do websites make learning easier?",
            "Should online information be regulated?"
        ]
    },

    {
        "part2": (
            "Describe a TV program you enjoy watching.\n"
            "You should say:\n"
            "- what the program is\n"
            "- what it is about\n"
            "- why you enjoy it\n"
            "and explain the role of TV in entertainment."
        ),
        "part3": [
            "Do people still watch television regularly?",
            "How has TV content changed?",
            "Is TV more educational or entertaining?",
            "Should children’s TV programs be controlled?",
            "Will TV become less popular in the future?"
        ]
    },

    {
        "part2": (
            "Describe a news source you trust.\n"
            "You should say:\n"
            "- what the source is\n"
            "- how often you use it\n"
            "- why you trust it\n"
            "and explain why trust in media is important."
        ),
        "part3": [
            "Why is trust important in news?",
            "How can people identify fake news?",
            "Is social media a reliable news source?",
            "Should governments control the news?",
            "How has news consumption changed?"
        ]
    },

    {
        "part2": (
            "Describe a time when technology caused a problem.\n"
            "You should say:\n"
            "- what the problem was\n"
            "- why it happened\n"
            "- how it was solved\n"
            "and explain the disadvantages of technology."
        ),
        "part3": [
            "What problems can technology create?",
            "Does technology increase stress?",
            "Should people reduce screen time?",
            "Can technology failures be dangerous?",
            "How can technology be used responsibly?"
        ]
    },

    {
        "part2": (
            "Describe a mobile app you find useful.\n"
            "You should say:\n"
            "- what the app is\n"
            "- how you use it\n"
            "- why it is useful\n"
            "and explain how apps improve daily life."
        ),
        "part3": [
            "Why are mobile apps popular?",
            "Do apps make life easier?",
            "Are there too many apps today?",
            "How do apps affect productivity?",
            "Will apps replace traditional services?"
        ]
    },

    {
        "part2": (
            "Describe a piece of technology you want to buy.\n"
            "You should say:\n"
            "- what it is\n"
            "- why you want it\n"
            "- how it would help you\n"
            "and explain how technology influences choices."
        ),
        "part3": [
            "Why do people want new technology?",
            "Does advertising influence technology purchases?",
            "Are people spending too much on gadgets?",
            "Should technology be affordable for everyone?",
            "How does technology shape lifestyle?"
        ]
    },

    {
        "part2": (
            "Describe a film or video you watched online.\n"
            "You should say:\n"
            "- what it was\n"
            "- where you watched it\n"
            "- why you liked it\n"
            "and explain how online videos influence entertainment."
        ),
        "part3": [
            "Why are online videos popular?",
            "Has online media replaced traditional media?",
            "Do people prefer short or long videos?",
            "How do videos influence opinions?",
            "Should online content be monitored?"
        ]
    },

    {
        "part2": (
            "Describe a time when you learned something from the internet.\n"
            "You should say:\n"
            "- what you learned\n"
            "- how you learned it\n"
            "- why it was useful\n"
            "and explain how the internet supports learning."
        ),
        "part3": [
            "Why do people use the internet to learn?",
            "Is online learning effective?",
            "What are the disadvantages of online learning?",
            "Should online education replace classrooms?",
            "How will learning change in the future?"
        ]
    },

    {
        "part2": (
            "Describe a device that improved communication.\n"
            "You should say:\n"
            "- what the device is\n"
            "- how it improves communication\n"
            "- why it is important\n"
            "and explain how communication has evolved."
        ),
        "part3": [
            "How has technology changed communication?",
            "Do people communicate less face-to-face?",
            "Is digital communication effective?",
            "What communication problems exist today?",
            "How can communication be improved?"
        ]
    },

    {
        "part2": (
            "Describe a time when media influenced your opinion.\n"
            "You should say:\n"
            "- what media it was\n"
            "- what opinion changed\n"
            "- why it influenced you\n"
            "and explain the power of media."
        ),
        "part3": [
            "How does media influence opinions?",
            "Is media influence always negative?",
            "Do young people trust media?",
            "Should media be unbiased?",
            "How can people think critically about media?"
        ]
    },

    {
        "part2": (
            "Describe a technology-related skill you learned.\n"
            "You should say:\n"
            "- what the skill is\n"
            "- how you learned it\n"
            "- why it is useful\n"
            "and explain why technology skills matter."
        ),
        "part3": [
            "Why are technology skills important today?",
            "Should technology be taught in schools?",
            "Are older people less comfortable with technology?",
            "Can technology skills improve employment?",
            "How often should people update their skills?"
        ]
    },

    {
        "part2": (
            "Describe a problem caused by social media.\n"
            "You should say:\n"
            "- what the problem is\n"
            "- who it affects\n"
            "- why it is serious\n"
            "and explain how social media should be managed."
        ),
        "part3": [
            "What problems does social media create?",
            "Does social media affect mental health?",
            "Should social media companies take responsibility?",
            "Can social media addiction be prevented?",
            "How should young people use social media?"
        ]
    },

    {
        "part2": (
            "Describe a technology you think will be important in the future.\n"
            "You should say:\n"
            "- what the technology is\n"
            "- how it will be used\n"
            "- why it is important\n"
            "and explain how it may change society."
        ),
        "part3": [
            "How do people predict future technologies?",
            "Will technology solve major global problems?",
            "Are people too optimistic about technology?",
            "Should future technology be controlled?",
            "How can society prepare for technological change?"
        ]
    },

    {
        "part2": (
            "Describe a time when technology helped you save time.\n"
            "You should say:\n"
            "- what technology it was\n"
            "- how it saved your time\n"
            "- what you did with the saved time\n"
            "and explain why time-saving technology is valuable."
        ),
        "part3": [
            "Why is saving time important today?",
            "Does technology always save time?",
            "How do people use saved time productively?",
            "Are people busier than before?",
            "Can time-saving technology reduce stress?"
        ]
    },

    {
        "part2": (
            "Describe a piece of technology you found difficult to use.\n"
            "You should say:\n"
            "- what the technology was\n"
            "- why it was difficult\n"
            "- how you dealt with it\n"
            "and explain why some technology is hard to use."
        ),
        "part3": [
            "Why do some people struggle with technology?",
            "Should technology be simpler?",
            "Do companies consider user experience enough?",
            "How can people learn to use new technology?",
            "Is complex technology unavoidable?"
        ]
    },

    {
        "part2": (
            "Describe a situation where media gave incorrect information.\n"
            "You should say:\n"
            "- what the information was\n"
            "- where you saw or heard it\n"
            "- what the result was\n"
            "and explain why misinformation is dangerous."
        ),
        "part3": [
            "Why does misinformation spread easily?",
            "How can people verify information?",
            "Should media be punished for false information?",
            "Does misinformation affect public trust?",
            "How can misinformation be reduced?"
        ]
    },

    {
        "part2": (
            "Describe a technology that improved your learning experience.\n"
            "You should say:\n"
            "- what the technology was\n"
            "- how it helped you learn\n"
            "- why it was effective\n"
            "and explain how technology supports education."
        ),
        "part3": [
            "How does technology change education?",
            "Are digital tools better than traditional methods?",
            "Can technology replace teachers?",
            "Should schools invest more in technology?",
            "What problems can technology cause in education?"
        ]
    },

    {
        "part2": (
            "Describe a time when you reduced your use of technology.\n"
            "You should say:\n"
            "- what technology you reduced\n"
            "- why you reduced it\n"
            "- how it affected you\n"
            "and explain why limiting technology can be beneficial."
        ),
        "part3": [
            "Why do people reduce screen time?",
            "Is digital detox necessary?",
            "Does reducing technology improve focus?",
            "Should children’s screen time be limited?",
            "Can people live without technology?"
        ]
    },

    {
        "part2": (
            "Describe a technology-related change in your daily routine.\n"
            "You should say:\n"
            "- what changed\n"
            "- why it changed\n"
            "- how your routine improved or worsened\n"
            "and explain how technology affects habits."
        ),
        "part3": [
            "How does technology change daily routines?",
            "Are habits easier to change with technology?",
            "Does technology encourage laziness?",
            "How can people balance technology use?",
            "Will routines become fully automated?"
        ]
    },

    {
        "part2": (
            "Describe a time when you shared information online.\n"
            "You should say:\n"
            "- what you shared\n"
            "- why you shared it\n"
            "- what response you received\n"
            "and explain why people share information online."
        ),
        "part3": [
            "Why do people share information online?",
            "Is sharing online information risky?",
            "Do people overshare on social media?",
            "How does online sharing affect privacy?",
            "Should people be more careful online?"
        ]
    },

    {
        "part2": (
            "Describe a device you think people rely on too much.\n"
            "You should say:\n"
            "- what the device is\n"
            "- why people rely on it\n"
            "- what problems it causes\n"
            "and explain the risks of over-reliance on technology."
        ),
        "part3": [
            "Why do people become dependent on devices?",
            "Is dependency on technology dangerous?",
            "How can people reduce dependency?",
            "Does technology reduce basic skills?",
            "Should people be encouraged to use technology less?"
        ]
    },

    {
        "part2": (
            "Describe a time when technology helped you communicate during a problem.\n"
            "You should say:\n"
            "- what the problem was\n"
            "- what technology you used\n"
            "- how it helped\n"
            "and explain why communication technology matters."
        ),
        "part3": [
            "Why is communication important during problems?",
            "Has technology improved emergency communication?",
            "Can technology cause misunderstandings?",
            "Should communication tools be more reliable?",
            "How will communication change in the future?"
        ]
    },

    {
        "part2": (
            "Describe a form of media you would like to use less.\n"
            "You should say:\n"
            "- what it is\n"
            "- why you want to reduce it\n"
            "- what you would do instead\n"
            "and explain how media consumption affects life."
        ),
        "part3": [
            "Do people consume too much media?",
            "How does media affect attention span?",
            "Should people control media habits?",
            "Is traditional media still relevant?",
            "How can healthy media habits be developed?"
        ]
    },

    {
        "part2": (
            "Describe a time when technology failed you.\n"
            "You should say:\n"
            "- what failed\n"
            "- why it was a problem\n"
            "- how you handled it\n"
            "and explain why technology reliability matters."
        ),
        "part3": [
            "Why do people trust technology so much?",
            "What problems occur when technology fails?",
            "Should people have backup plans?",
            "Can over-reliance increase risk?",
            "How can technology be made more reliable?"
        ]
    },

    {
        "part2": (
            "Describe a media personality you follow.\n"
            "You should say:\n"
            "- who the person is\n"
            "- where you follow them\n"
            "- why you like their content\n"
            "and explain the influence of media personalities."
        ),
        "part3": [
            "Why do people follow media personalities?",
            "Do influencers affect opinions?",
            "Should influencers be responsible role models?",
            "Is fame easier to achieve today?",
            "How do influencers impact young people?"
        ]
    },

    {
        "part2": (
            "Describe a time when technology made you feel isolated.\n"
            "You should say:\n"
            "- what technology was involved\n"
            "- why you felt isolated\n"
            "- how you dealt with it\n"
            "and explain the social impact of technology."
        ),
        "part3": [
            "Can technology increase loneliness?",
            "Do people socialize less face-to-face?",
            "How can technology improve social connections?",
            "Should people balance online and offline life?",
            "Does technology change social skills?"
        ]
    },

    {
        "part2": (
            "Describe a positive change brought by media.\n"
            "You should say:\n"
            "- what the change was\n"
            "- who benefited from it\n"
            "- why it was positive\n"
            "and explain how media can support society."
        ),
        "part3": [
            "How can media bring positive change?",
            "Does media raise social awareness?",
            "Can media influence behavior positively?",
            "Should media focus more on positive news?",
            "How does media shape public opinion?"
        ]
    },

    {
        "part2": (
            "Describe a technology trend you want to follow in the future.\n"
            "You should say:\n"
            "- what the trend is\n"
            "- why it interests you\n"
            "- how it may affect life\n"
            "and explain why future trends matter."
        ),
        "part3": [
            "Why are people interested in technology trends?",
            "Do trends influence purchasing behavior?",
            "Are technology trends predictable?",
            "Can trends create social pressure?",
            "How should people adapt to future technology?"
        ]
    },

]


def get_part2_and_part3():
    topic = random.choice(part2_with_part3)
    return topic["part2"], random.sample(topic["part3"], 5)
