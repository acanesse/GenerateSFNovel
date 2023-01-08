from urllib import request
import requests
import openai, os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

# Check the API key
if openai.api_key is None:
  print("Please set the OPENAI_API_KEY environment variable")
  exit(1)

# AI generated title list:
title_list = ["The Star Seekers", "The Dreamquest", "The Quantum Rift", "The Omega Protocol", "Realms of Infinity", "The Dark Matter", "The Techno Dream", "The Dream Machine", "The Quantum Conspiracy", "The Galactic War", "The Singularity", "The Alien Menace", "The World Beyond", "The Time Travellers", "The Cyber Paradox", "The War of the Worlds", "The Space Pirates", "The Robotic Revolution", "The Androids", "The Post-Human Age", "The Lost Colony", "The Minds of Tomorrow", "The Machine Uprising", "The Black Hole", "The Artificial Intelligence", "The Stars Beyond", "The Star Forge", "The Time Machine", "The Singularity Virus", "The Quantum Theory", "The Interdimensional Portal", "The Alien Invasion", "The Quantum Leap", "The Nanotech Wars", "The Galactic Empire", "The Transhuman Era", "The War for the Worlds", "The Technological Singularity", "The Cyborg Revolution", "The Space Race", "The Artificial Lifeform", "The Quantum Paradox", "The Planet of the Machines", "The Eternal War", "The Quantum Labyrinth", "The Machine Wars", "The Techno-Apocalypse", "The Digital Frontier", "The Hyperdrive", "The Time Lord", "The Androids of Doom", "The Cyborg Uprising", "The Interdimensional Conflict", "The Space Odyssey", "The Dark Matter Dimension", "The Quantum Dream", "The Robot Rebellion", "The Singularity Paradox", "The Time Warp", "The Cyber War", "The Star Alliance", "The Multiverse", "The Space-Time Continuum", "The Digital Dominion", "The Supercomputer", "The World Within", "The Transhuman Experiment", "The Intergalactic War", "The Cyber Revolution", "The Mind Beyond", "The Techno-Genesis", "The Galactic Genesis", "The Space-Time Odyssey", "The Cybernetics", "The Alien Intelligence", "The Time Paradox", "The Inter-Dimensional War", "The Quantum Reality", "The Robot Uprising", "The Interdimensional Quest", "The Technological Age", "The Time-Space Continuum", "The Artificial Intelligence Uprising", "The Quantum Quest", "The Interdimensional Travelers", "The War for the Universe", "The Transhuman Revolution", "The War of the Machines", "The Quantum Shift", "The Cyber-Apocalypse", "The Transhuman Age", "The Time Travelers", "The Star-Crossed Lovers", "The Intergalactic Space Race", "The Cyber-Genesis", "The Cosmic War", "The Digital Dimension", "The Age of the Machines", "The Alien Encounter", "The Supernova", "The Space-Time War", "The Interdimensional Voyage", "The Galactic Battle", "The Star-Crossed Destiny", "The Time-Space Vortex", "The Digital Apocalypse", "The Interdimensional Odyssey", "The Artificial Intelligence Revolution", "The Quantum Domain", "The Transhuman Uprising", "The Intergalactic Empire", "The Mind of the Machine", "The Interdimensional Battle", "The Time-Space Labyrinth", "The Time Manipulator", "Planet of the Lost", "The Miracle of the Void", "Galaxy Raider", "Starlight Chaser", "The Void's Edge", "Eons of Darkness", "The Jupiter Effect", "The Genesis Cloud", "Futureshock", "Time of the Phoenix", "The Andromeda Engine", "The Day the Earth Changed", "The Power of the Red Star", "Star Splicers", "The Time Traveler's Choice", "The Dragon Blade", "The Doomsday Gambit", "Exile of the Stars", "The Andromeda War", "The Secret of the Singularity", "From the Shadows of Space", "The Gift of Infinity", "The Singularity Storm", "Time Friction", "A Dance in the Dark", "The Revenant of Time", "Time Shadows", "Time Weaver", "The Centauri Paradox", "The Shadow After Time", "The Maelstrom of Time", "The Riddle of the Stars", "A Dream of Machines", "A World Beyond Time", "The Aftermath of the Singularity", "The Quantum War", "The Shattered Earth", "The End of Tomorrow", "The Quantum Divide", "The Edge of the Universe", "Echoes of the Void", "The Labyrinth of Eternity", "The Doorway to Infinity", "The Algorithm of Fate", "The Singularity's Edge", "The Lost Star Fleet", "The Robots of Time", "The Quantum Saboteur", "The Supernova Conspiracy", "The Sentinels of Time", "The Dragon's Claw", "The Mirror Master", "The Stardust Wars", "The Singularity's Fall", "The Andromeda Prophecy", "The Quantum Prophecy", "The Emissary of Time", "The Cyborg Apocalypse", "The Geometry of Time", "The Web of the Stars", "The Shadow War", "The Edge of Forever", "The Future of the Past", "The Mechs of Time", "The Architect of Infinity", "The Time Machine Paradox", "The Quantum Conundrum", "The Paradox of Time", "The Machines of Time", "The Time Dancer", "The Singularity's Fury", "The Star Crossed Universe", "The Final Frontier", "The Kaleidoscope of Time", "The Fractured Universe", "The Quantum Machine", "The Cybernetic War", "The Frozen Age", "The Great Divide", "The Space Time Paradox", "The Quantum Nexus", "The Star Splitter", "The Space Time Labyrinth", "The Edge of Creation", "The Dragon's Lair", "The Web of Time", "The Singularity's Shadow", "The Mechanics of Time", "The Celestial Divide", "The Black Star", "The Rise of the Machines", "The Alpha Star", "The Digital Divide", "The Time Labyrinth", "The Dark Dimension", "The Revolution of Time", "The Time Cataclysm", "The Singularity's Web", "The Vanishing Point", "The Warlord of Time", "The Doomsday Device", "The Time Machine Gambit", "The War in Time", "The Final Battle", "The Quantum Singularity", "The Cosmic Supernova", "The Power Beyond Time", "The Star Seer", "The Time Lord's Crusade", "The Time Shadow", "The Machine Master", "The Quantum Disaster", "The Time Warp Paradox", "The Time Shifter", "The Quantum Void", "The Time Paradoxon", "The Singularity's Revenge", "The Edge of Infinity", "The Time Machine Prophecy", "The Interdimensional Conflict", "The Omega Protocol"]

dune_plot ="""
Duke Leto Atreides of House Atreides, ruler of the ocean planet Caladan, is assigned by the Padishah Emperor Shaddam IV to serve as fief ruler of the planet Arrakis. Although Arrakis is a harsh and inhospitable desert planet, it is of enormous importance because it is the only planetary source of melange, or the "spice", a unique and incredibly valuable substance that extends human youth, vitality and lifespan. It is also through the consumption of spice that Spacing Guild Navigators are able to effect safe interstellar travel. Shaddam sees House Atreides as a potential future rival and threat, and conspires with House Harkonnen, the former stewards of Arrakis and the longstanding enemies of House Atreides, to destroy Leto and his family after their arrival. Leto is aware his assignment is a trap of some kind, but is compelled to obey the Emperor’s orders anyway. Leto's concubine Lady Jessica is an acolyte of the Bene Gesserit, an exclusively female group that pursues mysterious political aims and wields seemingly superhuman physical and mental abilities, such as the ability to decide the sex of their children. Though Jessica was instructed by the Bene Gesserit to bear a daughter as part of their breeding program, out of love for Leto she bore a son, Paul. From a young age, Paul has been trained in warfare by Leto's aides, the elite soldiers Duncan Idaho and Gurney Halleck. Thufir Hawat, the Duke's Mentat (people with superhuman intelligence), has instructed Paul in the ways of political intrigue. Jessica has also trained her son in what Bene Gesserit disciplines she can. His prophetic dreams interest Jessica's superior, the Reverend Mother Gaius Helen Mohiam. She subjects Paul to the gom jabbar, a deadly test that causes blinding pain as part of an assessment of the subject's self-control. To her surprise, Paul passes despite being exposed to more pain than any others before him. Leto, Jessica, and Paul travel with their household to occupy Arrakeen, the capital on Arrakis formerly held by House Harkonnen. Leto learns of the dangers involved in harvesting the spice, which is protected by giant sandworms, and negotiates with the planet's native Fremen people, seeing them as a valuable ally rather than foes. Soon after the Atreides' arrival, Harkonnen forces attack, joined by the Emperor's ferocious Sardaukar troops in disguise. Leto is betrayed by his personal physician, the Suk doctor Wellington Yueh, who delivers a drugged Leto to the Baron Vladimir Harkonnen and his twisted Mentat, Piter De Vries. Yueh, however, arranges for Jessica and Paul to escape into the desert, where they are presumed dead by the Harkonnens. Yueh replaces one of Leto's teeth with a poison gas capsule, hoping Leto can kill the Baron during their encounter. The Baron narrowly avoids the gas due to his shield, which instead kills Leto, De Vries, and others. The Baron forces Hawat to take over De Vries' position by dosing him with a long-lasting, fatal poison and threatening to withhold the regular antidote doses unless he obeys. While he follows the Baron's orders, Hawat works secretly to undermine the Harkonnens.  After fleeing into the desert, Paul realizes he has significant powers as a result of the Bene Gesserit breeding scheme, inadvertently caused by Jessica bearing a son and his exposure to high concentrations of spice. In visions, he foresees futures in which he lives among the planet's native Fremen, and is also informed of the addictive qualities of the spice. It is revealed Jessica is the daughter of Baron Harkonnen, a secret kept from her by the Bene Gesserit. After being captured by Fremen, Paul and Jessica are accepted into the Fremen community of Sietch Tabr, and teach them the Bene Gesserit fighting technique known as the "weirding way". Paul proves his manhood by killing a Fremen named Jamis in a ritualistic crysknife fight and chooses the Fremen name Muad'Dib, while Jessica opts to undergo a ritual to become a Reverend Mother by drinking the poisonous Water of Life. Pregnant with Leto's daughter, she inadvertently causes the unborn child, Alia, to become infused with the same powers in the womb. Paul takes a Fremen lover, Chani, and has a son with her, Leto II. Two years pass and Paul's powerful prescience manifests, which confirms for the Fremen that he is their prophesied messiah, a legend planted by the Bene Gesserit's Missionaria Protectiva. Paul embraces his father's belief that the Fremen could be a powerful fighting force to take back Arrakis, but also sees that if he does not control them, their jihad could consume the entire universe. Word of the new Fremen leader reaches both Baron Harkonnen and the Emperor as spice production falls due to their increasingly destructive raids. The Baron encourages his brutish nephew Glossu Rabban to rule with an iron fist, hoping the contrast with his shrewder nephew Feyd-Rautha will make the latter popular among the people of Arrakis when he eventually replaces Rabban. The Emperor, suspecting the Baron of trying to create troops more powerful than the Sardaukar to seize power, sends spies to monitor activity on Arrakis. Hawat uses the opportunity to sow seeds of doubt in the Baron about the Emperor's true plans, putting further strain on their alliance. Gurney, having survived the Harkonnen coup to become a smuggler, reunites with Paul and Jessica after a Fremen raid on his harvester. Believing Jessica to be the traitor, Gurney threatens to kill her, but is stopped by Paul. Paul did not foresee Gurney's attack, and concludes he must increase his prescience by drinking the Water of Life, which is traditionally fatal to males. Paul falls into unconsciousness for several weeks after drinking the poison, but when he wakes, he has clairvoyance across time and space: he is the Kwisatz Haderach, the ultimate goal of the Bene Gesserit breeding program. Paul senses the Emperor and Baron are amassing fleets around Arrakis to quell the Fremen rebellion, and prepares the Fremen for a major offensive against the Harkonnen troops. The Emperor arrives with the Baron on Arrakis. The Emperor’s troops seize a Fremen outpost, killing many including young Leto II, while Alia is captured and taken to the Emperor. Under cover of an electric storm, which shorts out the Emperor's troops' defensive shields, Paul and the Fremen, riding giant sandworms, assault the capital while Alia assassinates the Baron and escapes. The Fremen quickly defeat both the Harkonnen and Sardaukar troops. Paul faces the Emperor, threatening to destroy spice production forever unless Shaddam abdicates the throne. Feyd-Rautha attempts to stop Paul by challenging him to a ritualistic knife fight, during which he attempts to cheat and kill Paul with a poison spur in his belt. Paul gains the upper hand and kills him. The Emperor reluctantly cedes the throne to Paul and promises his daughter Princess Irulan's hand in marriage. As Paul takes control of the Empire, he realizes that while he has achieved his goal, he is no longer able to stop the Fremen jihad, as their belief in him is too powerful to restrain.
"""

# This script generates text from a language model trained on the GPT-2 model.
def generate_text(prompt, length=1800, tmp=0.8):
  
  completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=length,
    temperature=tmp,
  )

  message = completions.choices[0].text

  return message.strip()

# get plot from title
def get_plot(title, plot_example):
    prompt = f'Invent the plot for the SF novel "{title}". Give a lot of details, your text should be 2000 words long'
    plot = generate_text(prompt)
    return plot

# get summary from title and plot
def get_summary(title, plot):
    prompt = f'Invent the back cover summary of the science fiction novel titled: "{title}". It should be 500 words long. The plot of the book is: \n {plot}'
    summary = generate_text(prompt)
    return summary

def get_sample(title, plot):
    prompt = f'Write a 2000 words sample from the novel: "{title}". The text ends on a cliffhanger. The full plot of the book is the following: \n {plot}'
    sample = generate_text(prompt)
    return sample

def get_keywords(title, plot):
    prompt = f'Invent 5 keywords for the science fiction novel titled: "{title}". The plot of the book is: \n {plot}'
    keywords = generate_text(prompt)
    return keywords

def book_cover_description(title, plot):
    prompt = f'Describe in one sentence the book cover for the novel titled: "{title}"'
    description = generate_text(prompt)
    return description



def generate_novel(title):
    plot = get_plot(title, dune_plot)
    summary = get_summary(title, plot)
    summary = get_summary(title, plot)
    sample = get_sample(title, plot)
    keywords = get_keywords(title, plot)
    cover_description = book_cover_description(title, plot)
    return {
        'title': title,
        'plot': plot,
        'summary': summary,
        'sample': sample,
        'keywords': keywords,
        'cover_description': cover_description
    }


def main():

    all_novels = []

    for title in title_list:
        novel = generate_novel(title)
        print(novel)
        all_novels.append(novel)

    with open('run/novels.json', 'w') as f:
        json.dump(all_novels, f, ensure_ascii=False)

if __name__ == '__main__': 
    main()