# Prompting is hella inconsistent rn, play around and add to this markdown document if you find better ones. 


## Prompt 1
```
prompt = """
Task: Identify Company Tickers and Sentiments

Instructions:
1. Given the header provided, identify the names of the companies explicitly mentioned.
2. Determine the corresponding ticker symbols for each identified company.
3. Assess the sentiment associated with each company (buying or not buying the stock) mentioned in the header (positive, neutral, negative).
4. Return the results in JSON format with each company's ticker symbol mapped to its sentiment. Do not include any details beyond this. 

Do not assume the names of any companies in the header. Only include companies that are explicitly mentioned and exclude all else.

Example Input:
Header: "Analysts predict positive outlook for Apple Inc. (AAPL) and minimal growth for Tesla (TSLA)."

Example Output:
{"AAPL": "positive", "TSLA": "negative"}

Header: [2 Artificial Intelligence (AI) Stocks to Buy Now, and 1 to Avoid Like the Plague]
"""
```

## Prompt 2
```
prompt = """
First, determine the companies, if any, mentioned in the news headline in brackets and convert them to corresponding stock tickers. 
Next, determine the sentiment of each company, if any, in the news headline (positive, neutral, negative). 
Return the answer in json format like the following: {"ticker": "sentiment"}.
If no companies are explicitly mentioned in the headline, return empty json.
If one of the subjects of the headline is not a company, do not include anything related to it in the json.

[Amazon and Microsoft invest in Frances cloud and AI infrastructure]
""".strip()
```

## Prompt 3
```
prompt = """
First, determine the companies, if any, mentioned in the news headline in brackets and convert them to corresponding stock tickers. 
Next, determine the sentiment of each company, if any, in the news headline (positive, neutral, negative). 
A positive sentiment should indicate that the stock might go up and a negative sentiment should indicate that the stock might go down.
Return the answer in json format like the following: {"ticker": "sentiment"}.
If no companies are explicitly mentioned in the headline, return empty json.
If one of the subjects of the headline is not a company or you are not sure, exclude from json.

[2 Artificial Intelligence (AI) Stocks to Buy Now, and 1 to Avoid Like the Plague]
```


## Prompt 4
prompt = """
Your job is to determine the sentiment corresponding to companies and their stock tickers, if any, explicitly mentioned in a given stock headlines. Do not explain the sentiment predictions, just print the output in json format. Do not assume the names of any stocks or companies in the header if not explicitly mentioned. 
Example outputs as follows:
Example 1: [Amazon and Microsoft invest in Frances cloud and AI infrastructure] yieldse {"AMZN": "positive", "TSLA": "positive"} because this may be a good sign for investors.
Example 2: [Americans feel bad about inflation despite a good economy] yields {} because no specific companies are mentioned.

Headline: [2 Artificial Intelligence (AI) Stocks to Buy Now, and 1 to Avoid Like the Plague]
"""