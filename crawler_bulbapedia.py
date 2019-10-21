import requests,re
from bs4 import BeautifulSoup
import os.path


# skip these, as the crawler messes up it's text
problematic_episodes_list = ['AG120','XY124','DP048','DP120']


def prepareEpisode (link):
    html = requests.get(link).text

    episode_name = re.search('/wiki/(.*)',link)

    episode_name = episode_name.group(1)

    soup = BeautifulSoup(html, "lxml")

    texto_que_importa = soup.find_all('h2')[2]


    s = ''
    #import ipdb
    #ipdb.set_trace()
    for node in texto_que_importa.next_elements:
        if(hasattr(node,'text')):
            if(node.text == 'Major events'):
                break
            else:
                if (len(node.text) > 20):
                    s = s + node.text


    file_name = episode_name + '.txt'

    with open('data/pokeCorpusBulba/' + file_name, 'w') as text_file:
        if (episode_name not in problematic_episodes_list):
            text_file.write(s)


episode_links = []

main_link = 'https://bulbapedia.bulbagarden.net/wiki/'



for suffix,final_epi in [("EP",274),("AG",192),("DP",191),("XY",140),("SM",74)]:
    for i in range (1, final_epi + 1):
        # mask episode number in 3 digit string with 0s 
        ep_number = '{:=03d}'.format(i)
        episode_links.append(main_link + suffix + ep_number)


if not os.path.exists('data/pokeCorpusBulba'):
    os.makedirs('data/pokeCorpusBulba')

#print (episode_links)
for link in episode_links:
    prepareEpisode(link)
    print('Saved episode ' + link)
