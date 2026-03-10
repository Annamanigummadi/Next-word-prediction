# Next Word Prediction using Bigram Model in NLP

## Project Description
This project focuses on building a **Next Word Prediction system** using a **Bigram Language Model**, one of the fundamental techniques in **Natural Language Processing (NLP)**.  

The system predicts the most probable next word for a given input sentence by learning patterns from a text corpus. Unlike basic implementations that return only one prediction, our system provides **Top-3 predictions**, enhancing usability similar to modern mobile keyboards and search engines.  

The project is implemented using **Python** and **Flask**, where Flask provides a lightweight web interface to interact with the NLP backend.

## Theory
- Language models estimate the probability of word sequences in a sentence.  
- **N-gram models** predict a word using the previous N–1 words as context.  
- In this project, a **Bigram model (N = 2)** is used, meaning the prediction depends only on the immediately preceding word.  
- Bigrams are consecutive word pairs. The system calculates **unigram and bigram frequencies** and computes **conditional probabilities** to predict the next word.

## Formulas

**Bigram Probability Formula:**  

\[
P(w_n | w_{n-1}) = \frac{Count(w_{n-1}, w_n)}{Count(w_{n-1})}
\]

Where:  
- `Count(wₙ₋₁, wₙ)` → Bigram frequency  
- `Count(wₙ₋₁)` → Unigram frequency  

**Sentence Prediction:**  
- Select the word with **highest probability**  
- In our system, **Top-3 predictions** are returned.


## Example Calculation

**Given Corpus:**  
I am a student
I am learning natural language processing
I am learning machine learning


**Step 1: Sentence Tokenization**  
- I / am / a / student  
- I / am / learning / natural / language / processing  
- I / am / learning / machine / learning  

**Step 2: Bigram Formation**  
- (I, am), (am, a), (a, student), (I, am), (am, learning), (learning, natural), (natural, language), (language, processing), (I, am), (am, learning), (learning, machine), (machine, learning)  

**Step 3: Frequency Count**  
- **Unigrams:** Count(I)=3, Count(am)=3, Count(learning)=3  
- **Bigrams:** Count(I, am)=3, Count(am, a)=1, Count(am, learning)=2, Count(learning, natural)=1, Count(learning, machine)=1  

**Step 4: Probability Calculation**  
For input word `am`:  
- P(a | am) = 1/3 = 0.33  
- P(learning | am) = 2/3 = 0.67  

**Step 5: Top-3 Predictions**  
| Next Word | Probability |
|-----------|------------|
| learning  | 0.67       |
| a         | 0.33       |
| (none)    | -          |

**Step 6: Final Prediction**  
- Input: `I am`  
- Last word = `am`  
- **Top predictions:** `learning`, `a`, (No more words available)  
- **Final output:** `learning`


## Technologies Used
- **Python 3.x**  
- **Flask Framework**  
- **Pandas**, **NumPy** (for data processing)  
- **HTML/CSS** (for frontend interface)  

## Installation
1. Clone the repository:  
   ```bash
   git clone <repository-link>

## Navigate to project folder:

cd next-word-prediction

## Install dependencies:

pip install -r requirements.txt
Usage

## Run the Flask application:

python app.py

Open the web interface at http://127.0.0.1:5000

Enter a sentence in the input box

The system returns Top-3 predicted next words.

## Conclusion

This project demonstrates:

Statistical language modeling concepts (bigrams, probability calculation)

Real-time NLP predictions using a web interface

Integration of Python NLP backend with Flask frontend

Low computational complexity and fast predictions


G. Annamani
Roll Number: 23A81A0584
CSE-B, Computer Science and Engineering