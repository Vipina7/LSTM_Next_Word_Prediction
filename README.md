## Text Prediction Model with LSTM
This project is focused on building an LSTM-based text prediction model. The model takes an input text and predicts the next word based on patterns learned from a dataset of text. The primary goal is to generate accurate word predictions based on past sequences.

## Project Description
The model was developed using an LSTM (Long Short-Term Memory) Recurrent Neural Network to predict the next word in a given sequence of text. The dataset used contains a collection of text sequences which are tokenized and fed into the LSTM model for training. The model learns to understand the relationships between words and can predict the next word based on the input sequence.

## Steps Taken:
* Data Preparation:

The text data is tokenized using a tokenizer from Keras. The tokenizer converts the words into integer sequences.
Padding is applied to ensure that all input sequences are of the same length. Padding ensures that shorter sequences are padded with zeros to match the maximum sequence length.

* Model Architecture:

The model consists of the following layers:
Embedding Layer: Converts input sequences into dense vectors of fixed size.
LSTM Layers: Two LSTM layers are used to capture the temporal dependencies in the data.
Dense Layer: A fully connected layer with softmax activation to predict the probability distribution of the next word.
The model uses categorical_crossentropy loss and adam optimizer.

* Model Training:

The model is trained with the tokenized sequences, and it learns to predict the next word in the sequence.
The training process includes setting the max_sequence_len and splitting the data into training and validation sets.
Prediction Function:

The next_word function takes an input text, tokenizes it, and feeds it into the trained model to predict the next word in the sequence. The prediction is based on the word index learned during training.