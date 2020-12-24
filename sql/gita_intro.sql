-- The Gita SQL is being offered in Open Source
-- MIT License
-- www.krizn.com / www.krishna.net
-- Author: Dev Bhattacharyya
-- 
-- Database: gita.db
-- 

PRAGMA encoding="UTF-8";

-- --------------------------------------------------------

--
-- Table structure for table gitaintro
--

DROP TABLE IF EXISTS gitaintro;
CREATE TABLE IF NOT EXISTS gitaintro (
  id INTEGER PRIMARY KEY,
  gitaid INTEGER default NULL,
  description text,
  user varchar(6) NOT NULL default '',
  sanskrit_text text,
  boldtext1 varchar(127) default NULL,
  boldtext2 varchar(127) default NULL,
  boldtext3 varchar(127) default NULL,
  paragraph1 text ,
  paragraph2 text ,
  paragraph3 text
);

--
-- Insert data into table gitaintro
--

INSERT INTO gitaintro VALUES(1, 1, '', '', '', 'Written scriptures of  Mahabharata (Sanskrit: महाभारत ) first appeared in Sanskrit between 540 and 300 BCE narrating an epic', 'that must have occurred a 1000 years or more before. Mahabharata has manifold tales, the central theme is about the legends', 'of the Bharatas (a Vedic Aryan group). Bhagavad-Gita (Sanskrit: भगवद्गीता) is part of “Bhisma Parva” chapter of the epic.', 'Bhagavad-Gita is a rich, philosophical treatise. It is composed of 700 verses which are strictly a dialog between Krishna and Arjuna at a battlefield. Many of the English and other language translations tend towards author-bias. Whether the reader is inclined to think this is all but an allegory or something that really happened a few thousands of years before is left entirely to the reader’s discretion.', 'What happened and what was practiced in the vedic-aryan era is beyond all religions as they exist today. Some of that may even defy our imaginations. The best way to approach such a document is to disambiguate this scripture from any religion. In my opinion the Kuru-kshetra war was a holocaust – of millions of deaths; followed by a long period of economic depression. After nearly a thousand years, as the void became refilled with newer and more modern civilizations, that we begin to see re-emergence of faith and religious beliefs. ', 'This site captures specifics of the narrative through a PHP-MySQL application. The MySQL 5.0 database is available to everybody on request. The translations have been kept strictly within the confines of what makes most logical sense.');
INSERT INTO gitaintro VALUES(2, 1, NULL, 'admin', NULL, 'This site is dedicated to the loving memory of Kay who left us on January 8, 2010 to be re-united with the Lord.', 'Kay was closely associated with Goddess Shasti (a goddess of childbirth and a Protectress of Children).', 'She loved children, she loved us and she loved life.', 'Goddess Durga rides the big cat to battle. Goddess Shashti depended on the smaller cats. Kay was small but very brave. She was almost human;  she did not speak the human languages; however,    she always expressed more than a human. It is unfortunate that Kay, a member of these wonderful feline species suffered from Cancer for nearly two years and eventually lost her battle to it.', 'We tried our best to help her lead a quality life in spite of her agony – the carcinogens however proved stronger than our efforts to combat them. She was monitored regularly and homeopathy and natural medicines helped her till the fateful day of January 8, 2010. She and I had a deep understanding of one another and a beautiful bond that can only exist between humans or celestials. I pray everyday that she be born a human so I could look directly into her eyes; not as a contender but as a friend. ', 'Kay was a friend and an inspiration. She will live in my heart for as long as I live. Like the Gita, she remains a gospel, a truth that was very personal – very much ''ours''. ');
