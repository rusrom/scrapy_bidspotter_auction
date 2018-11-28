# Scrapy spider with custom filenames of images<br/>Download images on AWS S3

Spider has 1 input argumet: **auction URL**

![argument](https://i.imgur.com/RZn6l1V.jpg)

All lots are scraping with ONLY 1 REQUEST with usings some headers and cookies trick.

![pages](https://i.imgur.com/oG3xtK1.png)

**_Scrape such fields:_**
1. Lot number
2. Lot title
3. Lot description
4. All lot images.

![bidspotter](https://i.imgur.com/iAMLYmH.png)

**_Rule for images names:_**
* 1st digit - lot number
* 2nd digit - image index
* All images need download on Amazon S3

Filenames for 5 images of lot number 1:  
1_1.jpg, 1_2.jpg, 1_3.jpg, 1_4.jpg, 1_5.jpg

![lot_photos](https://i.imgur.com/tYQZfbv.jpg)
