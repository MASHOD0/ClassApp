# ClassApp

this is the main repository for DSCE Class App .

## What is this ?

This is a web application which stores the links to all the online classes held for first year students at DSCE. Teachers will be able to login to this app and share links to classes which will be organised and presented on the homepage.

## Why was this made ?

This was made to simplify the class joining process , the links sent through whatsApp were not organised properly which was creating a lot of confusion among students many students join late to class because of this.

## How to run this ?
 
1. install python 
follow this link (https://realpython.com/installing-python/)

2. install postgresql 
 follow this link (https://www.postgresql.org/docs/9.3/tutorial-install.html)

3. Create a virtual environment
run this command 
```
python -m venv venv
```
4. install requirements
run this command 
```
pip3 install -r requirements.txt
```
5. Configure the database

create a database by the name ``` Classes ```

6. run this postgresql script
```
CREATE TABLE "Classes" (
  "id" SERIAL PRIMARY KEY,
  "Section" char,
  "subject" varchar,
  "teacher" varchar,
  "link" varchar,
  "class_time" time,
  "time" timestamp
);
```
7. Run the script
```
python main.py
```

## Contributors 
[]Mashhood Alam
[]Advaik Sunil
