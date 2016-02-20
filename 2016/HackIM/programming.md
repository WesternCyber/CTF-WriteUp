# Programming (Pretty much _"Recon"_)

##Programming 1
**Q: So you reached Delhi and now the noise in your head is not allowing you to think rationally. The Nosise in your head has origin its Origin in your Stomach. And this is a big hunger. You can finish one or probably 2 Tandoori Chicken. So where can you get the best Tandoori Chicken in Delhi? This place tweeted last week that the Tandoori Chicken it servers is like never B4. You got its twitter handle?**

- This challenge could be solved in one of two ways. You could use a scraper to find a post or spend 30 seconds searching for Tandoori Chicken on twitter. We opted for the fastest way and searched for "tandoori chicken like never before."

The first tweet displayed was by @AnyaHotels, https://twitter.com/AnyaHotels/status/690040639619227648. The Flag was the twitter handle @AnyaHotels.

##Programming 2
**Q: Your simple good Deeds can save you but your GREED can kill you. This has happened before. This greedy person lived a miserable life just for the greed of gold and lust. You must know him, once you know him, you must reach his capital and next clues will be given by his famous EX-Body Guard. This file consists of few paragraphs. Each paragraph singles out one Alphabet. Scrambling those Alphabets will help you to know the country of this Ruler. Who was this Ruler?**

- The file given contained the following text :

**along with azalaan, country has became a major tourist attraction, with as many landmarks as Paris, such as Great Tribal Pyramid and  3,000 year old statue of the Gold Fartility Go it has a recast as a statue of Haffaz azalaan due to public outcry. Due to the lack of foreign investment, azalaann has attempted to offer 400,000 square miles of desert land to countries wishing to test missiles or to dump chemical waste.

lion is 1 of the 5 n live big cats, lives in the long parallel Panthera family Fellidae. Commonlly used term African lion collectively denotes several clubs found in Africa. With some males of 250 kg (550 lb)  weight, lion the second-largest living cat. Wild lions currentlly exist in sub-Saharan Africa and  Asia (large n legally protected popullation resides in Gir Forest National Park in India) while other types of lions pulled up popullation from North Africa.

Since  in time immemorial, earliest known in 5 August 1730 at Bizilabithi, Knit between Knit in London. The London-based nickle miner St James Irven Post irrupted on Fri, 8 April: "'Twas thought that the Kentish champions would have lost their honours by being bitten in innings if time had permitted". This is the first time word "innings" is found in records. Incidentally, it is  first time this "champions" is found in is significant  it confirms this idea of champion city established among cricket this is the earliest known instance of this filling

The borbons books club was always being busy. Carbaboni Candlebar was webbed with brothers books being busted in the big bag.The  night became darker by passing bits and sounds of beasts barking at the busy subway. Its believed to be coroborated by the best in the subsudry in bank of brisbane being called and brought in during military service. As Cbaboni bceomes aware, she starts building love for brother and about bincent really became.

Really utility stocks ( by the way including city food supply, gas supply water supply fully busy road supply) have provided highly good yield and way for envysor not only live or lay by dividend, but have supply  opportunity, try solidify a sundry. By this hy yeild they listed fully utility stocks they can really purchase.  Virtually shares lysted by U.S. were sharess by few way inferior and not listed in  Newyork.**

- This challenge involved analysing the frequency of letters in each paragraph and recording the letter with the highest frequency in each paragraph. We used the word frequency counter from https://www.mtholyoke.edu/courses/quenell/s2003/ma139/js/count.html to get this done.

- Once that is done you get the letters: A L I B Y
 -Rearraging these letters we get LIBYA. From this we deduced that the challange was looking for Ghaddafi which happened to be the flag. 

##Programming 3
**Q: Still Hungry and unsutisfied, you are looking for more. Some more, unique un heard dishes. Then you can find one to make it your self. Its his Dish. He has his own website which is he describes as " a social home for each of our passions". The link to his website is on his google+ page. whats the name of his site. By the way he loves and hogs on "Onion Kheer". Have you heard of "Onion Kheer"?**

- The solution was simple. Searching for Onion kheer on google plus provides you with multiple results on Chef BB. The flag was affimity.com which was found on one of the top three resuts.

##Programming 4
**Q: One of the _"NullCon"_ vidoes talked about a marvalous Russian Gift. The Vidoe was uploaded on [_"May of 2015"_] What is the ID of that _"Youtube video"_.**

- This was a very simple "recon" question. If you look at the "quoted" words in the question, you go to Youtube and search for "Nullcon" and you will see its channel, under the channel's videos category, you just look for the video that was uploaded back in May of 2015. There are few videos uploaded in May of 2015, but you have unlimited submission chance, so try it until you find the correct one. 

- The _"ID"_ can be found in the URL. The correct video had the following URL: "https://www.youtube.com/watch?v=a4_PvN_A1ts". After the "watch?v=", "a4_PvN_A1ts" is the video's ID.

- Therefore the answer was: **"a4_PvN_A1ts"**

##Programming 5
**Q: Dont blink your Eyes, you might miss it. But the fatigue and exhaustion rules out any logic, any will to stay awake. What you need now is a slumber. Cat nap will not do. 1 is LIFE and 0 is DEAD. in this GAME OF LIFE sleep is as important food. So... catch some sleep. But Remember...In the world of 10x10 matirx, the Life exists. If you SLOTH, sleep for 7 Ticks, or 7 Generation, In the game of Life can you tell what will be the state of the world? 

The world- 10x10

0000000000,0000000000,0001111100,0000000100,0000001000,0000010000,0000100000,0001000000,0000000000,000000000**

- The challenge referres to Conways Game of life. We first started off by looking for a 10x10 version of the game online and found one at he following link: http://www.edshare.soton.ac.uk/948/5/gol.html. We then filled in the blocks using the binary numbers given using 1 as LIFE and 0 as DEAD. The game was runfor 7 generations and the resulting row binaries gave the flag.