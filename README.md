# PSD-helper

# ALL Hail Vinayak Bhaiya 

Since all of us are dependent on the google sheets to view stuff so that it gets updated and all periodically (Its the main source)
But sometimes it might get updated a bit late and u might wanna plan with the updated stations

So yeah
With some digging and stalking
mostly digging yeah
I came across a script written by Vinayak bhaiya (2021 grad)

Thora sa revamp kiya usko so that it can be used and u can create excel sheets for urself

These are the 3 files that u need

Scraper.py

https://p.ip.fi/ctKv

skill.py

https://p.ip.fi/JZNn

format.py

https://p.ip.fi/a1-O

Run scraper.py for pb.json (partial data)
and then
skill.py for full data (with projects list)
U can then convert json to exccel using this website https://conversiontools.io/convert/json-to-excel

Thoda sa unformatted hai but in the nick of time it will make do

and then format.py for csv

![image](https://user-images.githubusercontent.com/59202075/169376043-41591bcc-49e6-49ee-84ca-0dc2d3f79c78.png)

this is how u should add a config.json to the same path as these files:-
{
		"creds": {
			"email": "f20170008@goa.bits-pilani.ac.in",
			"password": "USE_YOUR_CREDS"
		}
}

![image](https://user-images.githubusercontent.com/59202075/169376089-23f61705-2f3b-40dd-aee4-e6c689435541.png)


This is how ur directory would look after running all the scripts

So get a dev or a friend who knows dev to just run these simple scripts

and if u don't have a dev friend
Then I feel really sad for u

![image](https://user-images.githubusercontent.com/59202075/169527740-ecd533b0-8011-4842-b84e-2639f73cb00a.png)

for those asking ki
ab change kya hua kaise pata lagaye Fafa
its quite simple
partialpsd.csv download karo idhar se every 1 hour

And use this to compare the newly downloaded file with the previously downloaded file
https://www.textcompare.org/csv/compare/

green means something new is added

yellow means something is updated


*Hosted and cronned by Sudhanshu bhaiya*

https://smk.minetest.in/mypaste/?psd

It shows the time of updation as well. Keep downloading the files and keep comparing using the above mentioned csv comparer.
![image](https://user-images.githubusercontent.com/59202075/170722520-15e2ca33-b0cd-4fea-899e-9f0365b7f6a1.png)


