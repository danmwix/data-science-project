from bs4 import BeautifulSoup, element
import pandas as pd
import numpy as np
import asyncio
import aiohttp
import time

async def getGenre(url, session, sem, rec):
    async with sem:
        async with session.get(url) as game_response:
            print(f"Response Status for rec no. {rec}: {game_response.status}")
            sub_soup = BeautifulSoup(await game_response.text(), "lxml")
            # again, the info box is inconsistent among games so we
            # have to find all the h2 and traverse from that to the genre name
            h2s = sub_soup.find("div", {"id": "gameGenInfoBox"}).find_all('h2')
            # make a temporary tag here to search for the one that contains
            # the word "Genre"
            temp_tag = element.Tag
            for h2 in h2s:
                if h2.string == 'Genre':
                    temp_tag = h2

            return temp_tag.next_sibling.string




async def main():
    # Using aiohttp, we'll need to set the maximum amount of concurrent requests
    print(f"Start time: {time.strftime('%X')}")
    MAXIMUM_CONCURRENT_PAGES = 1
    MAXIMUM_CONCURRENT_SUBPAGES = 3
    SEMAPHORE_PAGE = asyncio.Semaphore(MAXIMUM_CONCURRENT_PAGES)
    SEMAPHORE_SUBPAGE = asyncio.Semaphore(MAXIMUM_CONCURRENT_SUBPAGES)


    # Desired Pages to Parse, current count of parsed games
    pages = 3
    # IMPORTANT, PAGE RESULTS CONTAIN THE MAXIMUM AMOUNT OF GAMES LOADED PER PAGE
    # THIS ALSO AFFECTS SUBPAGE PARSING!!!!
    page_results = 20
    rec_count = 0

    # These are the different columns that would be included in the final dataset
    rank = []
    gname = []
    platform = []
    year = []
    genre = []
    critic_score = []
    user_score = []
    publisher = []
    developer = []
    sales_na = []
    sales_pal = []
    sales_jp = []
    sales_ot = []
    sales_gl = []
    game_url = []

    urlhead = 'https://www.vgchartz.com/gamedb/?page='
    urltail = '&console=&region=All&developer=&publisher=&genre=&boxart=Both&ownership=Both'
    urltail += f'&results={page_results}&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0'
    urltail += '&showpublisher=1&showvgchartzscore=0&shownasales=1&showdeveloper=1&showcriticscore=1'
    urltail += '&showpalsales=0&showpalsales=1&showreleasedate=1&showuserscore=1&showjapansales=1'
    urltail += '&showlastupdate=0&showothersales=1&showgenre=1&sort=GL'

    # Creating the session object, this is to prevent making a new handshake each time we request a specific page
    # The comment was more useful when requests was being used, aiohttp does this by default
    async with aiohttp.ClientSession() as session:
        async with SEMAPHORE_PAGE:
            for page in range(1,pages):
            
                surl = urlhead + str(page) + urltail
                async with session.get(surl) as response:
                    soup = BeautifulSoup(await response.text(), "lxml")
                    
                    # Debugging: Keep track of the last page parsed
                    print(f"Page: {page}")
                    
                    # Parsing the anchor tags which contain the information for each game entry
                    game_tags = list(soup.select('a[href^="https://www.vgchartz.com/game/"]')
        )


                    async with asyncio.TaskGroup() as tg:
                        tasks = []
                        for tag in game_tags:

                            # add name to list
                            gname.append(" ".join(tag.string.split()))
                            print(f"{rec_count + 1} Fetch data for game {gname[-1]}")

                            # get different attributes
                            # traverse up the DOM tree
                            data = tag.parent.parent.find_all("td")
                            rank.append(np.int32(data[0].string))
                            platform.append(data[3].find('img').attrs['alt'])
                            publisher.append(data[4].string)
                            developer.append(data[5].string)
                            critic_score.append(
                                float(data[6].string) if
                                not data[6].string.startswith("N/A") else np.nan)
                            user_score.append(
                                float(data[7].string) if
                                not data[7].string.startswith("N/A") else np.nan)
                            sales_na.append(
                                float(data[9].string[:-1]) if
                                not data[9].string.startswith("N/A") else np.nan)
                            sales_pal.append(
                                float(data[10].string[:-1]) if
                                not data[10].string.startswith("N/A") else np.nan)
                            sales_jp.append(
                                float(data[11].string[:-1]) if
                                not data[11].string.startswith("N/A") else np.nan)
                            sales_ot.append(
                                float(data[12].string[:-1]) if
                                not data[12].string.startswith("N/A") else np.nan)
                            sales_gl.append(
                                float(data[8].string[:-1]) if
                                not data[8].string.startswith("N/A") else np.nan)
                            release_year = data[13].string.split()[-1]
                            
                            # different format for year since that data just contains the last 2 digits
                            if release_year.startswith('N/A'):
                                year.append('N/A')
                            else:
                                if int(release_year) >= 27:
                                    year_to_add = np.int32("19" + release_year)
                                else:
                                    year_to_add = np.int32("20" + release_year)
                                year.append(year_to_add)
                            url_to_game = tag.attrs['href']
                            game_url.append(url_to_game)
                            
                            # go to every individual website to get genre info
                            tasks.append(tg.create_task(getGenre(url_to_game, session, SEMAPHORE_SUBPAGE, rec_count)))
                            rec_count += 1

                    genre.extend([t.result() for t in tasks])


    columns = {
        'Rank': rank,
        'Name': gname,
        'Platform': platform,
        'Year': year,
        'Genre': genre,
        'Critic_Score': critic_score,
        'User_Score': user_score,
        'Publisher': publisher,
        'Developer': developer,
        'NA_Sales': sales_na,
        'PAL_Sales': sales_pal,
        'JP_Sales': sales_jp,
        'Other_Sales': sales_ot,
        'Global_Sales': sales_gl,
        'Game_url': game_url
    }
    print(rec_count)
    for key, value in columns.items():
        print(key, len(value))
    df = pd.DataFrame(columns)
    print(df.columns)
    df = df[[
        'Rank', 'Name', 'Platform', 'Year', 'Genre',
        'Publisher', 'Developer', 'Critic_Score', 'User_Score',
        'NA_Sales', 'PAL_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]
    df.to_csv("vgsales.csv", sep=",", encoding='utf-8', index=False)
    print(f"End time: {time.strftime('%X')}")


asyncio.run(main())