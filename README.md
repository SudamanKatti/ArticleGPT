# ArticleGPT
the following repository demonstrates code to train GPT2 using a csv file with news articles to create article GPT (GPT for creation of news snippets or sub articles). For each prompt, output of length and style like that of a news article will be generated. Using libraries like textblob and sentence transformer, all of the generated articles are also evaluated in tabular form on metrics like relevance, answerability (in this case, it measures a combination of length and context appropriateness) and style of writing. If the user is not satisfied with the articles, they can go back and try again with different prompts. The training of the model and plotting of results during training was done with transformers library, flask API was used for deployment. Here are some of the screenshots-


![image](https://github.com/user-attachments/assets/14d0f9d0-8156-4802-bee0-209686841054)


![image](https://github.com/user-attachments/assets/6736f9b3-ddc2-436a-9ba0-90a54bd0d851)


![image](https://github.com/user-attachments/assets/302c38ea-f0a0-4a87-a873-fe93a1163b9f)


![image](https://github.com/user-attachments/assets/53ef4b17-2f63-4275-9228-e5b7dd201ca6)
