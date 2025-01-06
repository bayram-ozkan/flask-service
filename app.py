import os
import logging
from flask import Flask

app = Flask(__name__)

# Log dosyasının bulunduğu dizini kontrol et, yoksa oluştur
log_directory = '/tmp/flask/logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Log dosyasının yolu
log_file = os.path.join(log_directory, 'app.log')

# Logging yapılandırması
logging.basicConfig(filename=log_file, level=logging.INFO)

# Log formatı ve seviyesini belirle
log_format = '%(asctime)s  ->  %(name)s - %(levelname)s - %(message)s - %(funcName)s - %(lineno)d'

# Logging yapılandırması
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,  # Daha ayrıntılı loglama için DEBUG seviyesi
    format=log_format
)



@app.route('/')
def home():
    app.logger.info('Ana sayfaya giriş yapıldı')  # Log yazma
    return "Merhaba, Flask Uygulaması Çalışıyor!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
