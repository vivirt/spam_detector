import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import os


def main():
  # 1. Cargar los datos
  data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'spam.csv')
  data = pd.read_csv(data_path, encoding='latin-1')
  data = data[['v1', 'v2']]
  data.columns = ['label', 'text']


  # 2. Preprocesar y dividir datos
  X_train, X_test, y_train, y_test = train_test_split(
    data['text'], data['label'], test_size=0.2, random_state=42
  )


  # 3. Vectorizar
  vectorizer = CountVectorizer()
  X_train_vec = vectorizer.fit_transform(X_train)
  X_test_vec = vectorizer.transform(X_test)


  # 4. Entrenar modelo
  model = MultinomialNB()
  model.fit(X_train_vec, y_train)


  # 5. Evaluación
  predictions = model.predict(X_test_vec)
  print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")


  # 6. Prueba rápida
  #"Hi Mark, are we still on for the meeting tomorrow?" (NO SPAM)
  email_prueba = "WINNER!! As a valued network customer you have been selected to receivea 1000 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only."

  vec = vectorizer.transform([email_prueba])
  pred = model.predict(vec)[0]
  
  if pred == "spam":
    print(f"Resultado: SPAM")
  else:
    print(f"Resultado: NO SPAM")


if __name__ == "__main__":
  main()