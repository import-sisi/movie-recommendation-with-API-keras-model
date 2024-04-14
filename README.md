# movie-recommendation-with-API-keras-model" 

This notebook presents an advanced approach to building a movie recommendation system, integrating both traditional machine learning and deep learning techniques to enhance recommendation accuracy and relevance. The system starts with a traditional method using TF-IDF for feature extraction from movie descriptions and genres, combined with user ratings data to compute similarity scores between movies.
![alt text](https://github.com/import-sisi/movie-recommendation-with-API-keras-model/blob/main/photo/Screenshot%202024-04-10%20150946.png)
![alt text](https://github.com/import-sisi/movie-recommendation-with-API-keras-model/blob/main/photo/Screenshot%202024-04-10%20151142.png)


Key Enhancements and Features:
![LINK]([https://github.com/import-sisi/movie-recommendation-with-API-keras-model/blob/main/photo/Screenshot%202024-04-10%20151142.png](https://ilikemovie.streamlit.app/))

Feature Engineering: Utilizes TF-IDF vectorization combined with MinMax scaled numerical features like popularity and vote averages. Deep Learning Integration: Incorporates an autoencoder model built using TensorFlow's Keras API to generate dense embeddings from the high-dimensional feature set. This model learns to compress and reconstruct the movie features, capturing complex patterns that are not immediately apparent. Recommendation Mechanism: Uses cosine similarity computed from embeddings to provide movie recommendations, moving beyond traditional similarity measures. Practical Use Cases: Demonstrates how to prepare the dataset, train the model, and make recommendations using the learned embeddings. This approach leverages the power of neural networks to understand and process complex patterns in the data, leading to more personalized and accurate recommendations. Whether you are a movie enthusiast looking for your next favorite film or a data scientist seeking to explore advanced recommendation systems, this notebook provides valuable insights and tools.
