import tensorflow as tf
import tensorflow_hub as hub

# Load the Universal Sentence Encoder model
use_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Function to create sentence embeddings using Universal Sentence Encoder
def create_embedding(sentence):
    # Convert sentence to a tensor
    sentence_tensor = tf.convert_to_tensor([sentence])

    # Generate embedding for the sentence
    embedding = use_model(sentence_tensor)

    return embedding.numpy()[0]  # Return the numpy array repre
	
	