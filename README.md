# Wikipedia Text Extractor for Game Titles
This project is a slightly modified version of [*AnKushRR/Wikipedia-Text-Extractor*](https://github.com/AnkushRR/Wikipedia-Text-Extractor).
It extracts plan text from Wikipedia about 110 game titles given in the [*pageTitleList.txt*](https://github.com/anyaosborne/Wikipedia-Text-Extractor-Games/blob/main/pageTitleList.txt) file. The [*output*](https://github.com/anyaosborne/Wikipedia-Text-Extractor-Games/tree/main/output) contains extracted page content for each game title. The [*AllGameDescriptions.txt*](https://github.com/anyaosborne/Wikipedia-Text-Extractor-Games/blob/main/AllGameDescriptions.txt) includes extracted content all in one document, which is good for using it for machine learning training.

## Requirements
* Python3+
* You will need to download [*Wikipedia pip3 library*](https://pypi.org/project/wikipedia/)

## How to Execute The Code
* Download the repository
* You may edit the [*pageTitleList.txt*](https://github.com/anyaosborne/Wikipedia-Text-Extractor-Games/blob/main/pageTitleList.txt) with your custom Wikepedia page titles. Make sure that the page title is the as in the respective Wikipedia URL link.
* Run [*getWikiPages.py*](https://github.com/anyaosborne/Wikipedia-Text-Extractor-Games/blob/main/getWikiPages.py)

## Output
* A new file will be created in the main directory called *AllGameDescriptions*
* A new directory will be created named *Output*
