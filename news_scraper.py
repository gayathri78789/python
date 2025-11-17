import requests
from bs4 import BeautifulSoup

url = "https://www.thehindu.com/"

response = requests.get(url)

if response.status_code!=200:
    print("failed to retrieve the webpage")
    exit()
    
    
html_context = response.text

soup = BeautifulSoup(html_context, 'html.parser')

headlines =[]

for h2 in soup.find_all("h2"):
    headline_text = h2.get_text().strip()
    if headline_text:
        headlines.append(headline_text)
        
        
        
output_file = "headlines.txt"       
with open(output_file, 'w', encoding='utf-8') as f:
    for i, h1 in enumerate (headlines,start =1):
        f.write(f"{i}. {h1}\n")
        
        
print(f"scraping completed! {len(headlines)} headlines saved to {output_file}.")