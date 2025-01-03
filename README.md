# ArticleGPT
The following repository contains ArticleGPT - GPT for creation of news snippets or sub articles. In this project, GPT 2 is trained using a csv file with news articles. For each prompt, output of length and style like that of a news article will be generated. Using libraries like text blob and sentence transformer, all of the generated articles are also evaluated in tabular form on metrics like relevance, answerability (in this case, it measures a combination of length and context appropriateness) and style of writing. If the user is not satisfied with the metrics for the articles, they can go back and try again with different prompts. The training of the model and plotting of results during training was done with transformers library, flask API was used for deployment, html,css and javascript was used for front end. Here are some of the screenshots-


![image](https://github.com/user-attachments/assets/14d0f9d0-8156-4802-bee0-209686841054)


![image](https://github.com/user-attachments/assets/eb4c44c7-72fe-45f8-a6c6-07106b9ad22c)


![image](https://github.com/user-attachments/assets/302c38ea-f0a0-4a87-a873-fe93a1163b9f)


![image](https://github.com/user-attachments/assets/53ef4b17-2f63-4275-9228-e5b7dd201ca6)
