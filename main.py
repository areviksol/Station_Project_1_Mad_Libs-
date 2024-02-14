from random import choice

def extract_variables(template):
    variables = []
    i = 0
    while i < len(template):
        ind1 = template.find("<")
        ind2 = template.find(">")
        if ind1 != -1 and ind2 != -1:
            variables.append(template[ind1 : ind2 + 1])
            template = template[ind2 + 1:]
            i = -1
        i += 1
    return variables

def fill_mad_libs(variables, template):
    story = template
    for var in variables:
        user_input = input(f"Input {var[1:-1]}: ")
        story = story.replace(var, user_input)
    return story

templates = [
    '''It was about <Number> <Measure of time> 
    ago when I arrived at the hospital in a 
    <Mode of Transportation>. The hospital is a/an <Adjective> place,
    there are a lot of <Adjective2> <Noun> here. 
    There are nurses here who have <Color> <Part of the Body>. 
    If someone wants to come into my room 
    I told them that they have to <Verb> first. 
    I've decorated my room with <Number2> <Noun2>. 
    Today I talked to a doctor and they were wearing a 
    <Noun3> on their <Part of the Body 2>. 
    I heard that all doctors <Verb> <Noun4> every day for breakfast. 
    The most <Adjective3> thing about being in 
    the hospital is the <Silly Word> <Noun> !''',

    '''This weekend I am going camping with 
    <Proper Noun (Person's Name) >. I packed my lantern, 
    sleeping bag, and <Noun>. I am so <Adjective (Feeling) >
    to <Verb> in a tent. I am <Adjective (Feeling) 2 >
    we might see an <Animal>, I hear they're kind of dangerous. 
    While we're camping, we are going to hike, fish, and <Verb2>. 
    I have heard that the <Color> lake is great for 
    <Verb (ending in ing)>. Then we will <Adverb (ending in ly) >
    hike through the forest for <Number> <Measure of Time>. 
    If I see a <Color> <Animal> while hiking, 
    I am going to bring it home as a pet! 
    At night we will tell <Number> <Silly Word> stories and roast 
    <Noun2> around the campfire!!''',

    '''Dear <Proper Noun (Person's Name)>, 
    I am writing to you from a <Adjective> castle in an enchanted forest. 
    I found myself here one day after going for a ride on a 
    <Color> <Animal> in <Place>. 
    There are <Adjective2> <Magical Creature (Plural) > and 
    <Adjective3> <Magical Creature (Plural)2 > here! 
    In the <Room in a House> there is a pool full of <Noun>. 
    I fall asleep each night on a <Noun2> of <Noun(Plural)3 > 
    and dream of <Adjective4> <Noun (Plural)4 >. 
    It feels as though I have lived here for <Number> <Measure of time>.
    I hope one day you can visit, although the only way to get here 
    now is <Verb (ending in ing)> on a <Adjective5>  <Noun5>!!'''
]
try:
    print("Do you want to choose a template or should it be randomly selected?")
    choice_input = input("Enter 'choose' to select a template or 'random' for a random selection: ")

    if choice_input.lower() == "choose":
        print("Available Templates:")
        for index, template in enumerate(templates):
            print(f"{index + 1}. Template {index + 1}")

        selected_template_index = int(input("Choose a template (enter the corresponding number): ")) - 1
        selected_template = templates[selected_template_index]
    else:
        selected_template = choice(templates)

    template_variables = extract_variables(selected_template)

    completed_story = fill_mad_libs(template_variables, selected_template)

    print(completed_story)
except KeyboardInterrupt:
    print("interrupted!")
except ValueError:
    print("Not valid template!")