
# Bir Linux sistemi  üzerinde bir servis  oluşturma ve yönetme

# Adımlar: 
    1. Basit bir uygulama oluşturun (örneğin, bir Python veya Node.js HTTP sunucusu).
    2. Uygulamayı bir hizmet olarak yönetmek için bir systemd birim dosyası yazın.
    3. Hizmetin önyükleme sırasında otomatik olarak başladığından ve çıktıları bir dosyaya kaydettiğinden emin olun.

# Path lere ve  oluşturacağınız servis adlarına dikkat edin.

## Servis için link oluşturabilir 
```
sudo systemctl link /root/task1/systemd/server.service
```

## ya da service dosyasını sistemde bulunan path e kopyalayabilirsiniz .
```
sudo cp /root/task1/systemd/http_server.service /etc/systemd/system/ 
```

## Systemd  tarafından kullanılan sistem servislerini ve yapılandırma dosyalarını yeniden yükler.
```
sudo systemctl daemon-reload
```

## Servisimizi başlangıçta otomatik olarak başlatılmasını sağlar.
```
sudo systemctl enable server.service
```

## Servisimizi aktif hale getirir.
```
sudo systemctl start server.service
```

## Servisimizi durumunu gösterir..
```
sudo systemctl status server.service
```

## Servisimizin log larını ve hatalarını gerçek zamanlı izlememizi sağlar.
```
sudo journalctl -u server.service -f
```



