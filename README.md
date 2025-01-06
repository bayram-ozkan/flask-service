
# Bir Linux sistemis üzerinde bir hizmeti dağıtma ve yönetme

# Adımlar: 
    1. Basit bir uygulama oluşturun (örneğin, bir Python veya Node.js HTTP sunucusu).
    2. Uygulamayı bir hizmet olarak yönetmek için bir systemd birim dosyası yazın.
    3. Hizmetin önyükleme sırasında otomatik olarak başladığından ve çıktıları bir dosyaya kaydettiğinden emin olun.


```
sudo systemctl link /root/task1/systemd/server.service


sudo cp /root/task1/systemd/http_server.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable http_server.service
sudo systemctl start http_server.service


sudo journalctl -u server.service -f

tail -f /root/task1/log/http_server.log

```
