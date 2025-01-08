
# Uygulama dockerize ve deploy

# Adımlar: 
1. Docker kullanarak flask uygulamayı konteynerleştirin. 
2. Uygulamayı yönetmek için bir docker-compose.yml dosyası ve yük dengeleme için bir ters proxy (örn. NGINX veya Traefik) oluşturun. 
3. En az 2 replika yapılandırarak yüksek kullanılabilirlik sağlayın.




## Docker ve docker-compose kurulumu

```
 curl -s https://raw.githubusercontent.com/bayram-ozkan/d0cker/refs/heads/main/_docker-install.sh | sudo bash
```

```
sudo apt install docker-compose -y
```

## Flask uygulamasını docker-compose ile  local de ayağa kaldırma 
```
docker-compose up --build -d
```

> [!NOTE]
> docker-compose ile ayağa kaldırırken  path lere dikkat edin
