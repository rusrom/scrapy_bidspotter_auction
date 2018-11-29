# Scrapy spider with custom filenames for images<br/>Download images on AWS S3

Spider has 1 input argumet: **auction URL**

![argument](https://i.imgur.com/RZn6l1V.jpg)

**_All lots are scraping with ONLY 1 REQUEST_** with usings some headers and cookies trick.

![pages](https://i.imgur.com/oG3xtK1.png)

### Scrape such fields
1. Lot number
2. Lot title
3. Lot description
4. All lot images.

![bidspotter](https://i.imgur.com/iAMLYmH.png)

### Path for saving images
Each auction URL has **catalogue-id**  
![argument](https://i.imgur.com/RZn6l1V.jpg)

For each auction on AWS S3 folder will be created with corresponding name

![aws](https://i.imgur.com/gHsGHVz.jpg)

### Rule for images names
* 1st digit - lot number
* 2nd digit - image index
* All images need download on Amazon S3

Filenames for 5 images of lot number 1:  
1_1.jpg, 1_2.jpg, 1_3.jpg, 1_4.jpg, 1_5.jpg

![lot_photos](https://i.imgur.com/pp6DLUb.jpg)

### Result on scrapinghub

![scrapinghub](https://i.imgur.com/nKa9ggT.png)
