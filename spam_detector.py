import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import os


def obtener_ruta_datos():
  """Obtiene la ruta al archivo de datos"""
  script_dir = os.path.dirname(__file__)  # src/
  project_dir = os.path.dirname(script_dir)  # spam_detector/
  return os.path.join(project_dir, 'data', 'spam.csv')


def entrenar_modelo():
  # Entrena el modelo de detección de spam
  # 1. Cargar datos
  data_path = obtener_ruta_datos()
  data = pd.read_csv(data_path, encoding='latin-1')
  data = data[['v1', 'v2']]
  data.columns = ['label', 'text']
  
  # 2. Dividir datos
  X_train, X_test, y_train, y_test = train_test_split(
    data['text'], data['label'], test_size=0.2, random_state=42
  )
  
  # 3. Vectorizar
  vectorizer = CountVectorizer()
  X_train_vec = vectorizer.fit_transform(X_train)
  
  # 4. Entrenar modelo
  model = MultinomialNB()
  model.fit(X_train_vec, y_train)
  
  print("Modelo entrenado exitosamente")
  return model, vectorizer


def predecir_spam(texto, modelo, vectorizer):
  ## Predice si un texto es spam o no
  vec = vectorizer.transform([texto])
  pred = modelo.predict(vec)[0]
  
  if pred == "spam":
    return "SPAM"
  else:
    return "NO SPAM"


def evaluar_modelo(modelo, vectorizer):
  ## Evalúa la precisión del modelo
  data_path = obtener_ruta_datos()
  data = pd.read_csv(data_path, encoding='latin-1')
  data = data[['v1', 'v2']]
  data.columns = ['label', 'text']
  
  X_train, X_test, y_train, y_test = train_test_split(
    data['text'], data['label'], test_size=0.2, random_state=42
  )
  
  X_test_vec = vectorizer.transform(X_test)
  predictions = modelo.predict(X_test_vec)
  accuracy = accuracy_score(y_test, predictions)
  
  return accuracy