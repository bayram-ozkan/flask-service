# Talos Odaklı Yapılandırma 

# Adımlar: 
1. Talos tabanlı bir kümeyi nasıl yöneteceğinizi ve sorunlarını nasıl gidereceğinizi açıklayın. 
2. Mümkünse, örnek bir iş yükünü dağıtmak için bir yapılandırma örneği sağlayın


## Talos kurulumu

```
brew install siderolabs/tap/talosctl
```


## talos  3 workes 1 master cluster kurulumu
```
talosctl cluster create --workers 3
```


## talos dasboard
```
talosctl dashboard --nodes 10.5.0.2
```

 ## cluster a bağlanmak için config dosyasını tanımlıyoruz.
 ```
talosctl kubeconfig    /home/user/.kube/talos-default -n 10.5.0.2 
```

## default olarak talos config dosyasını export ediyorum
```
export KUBECONFIG=~/.kube/talos-default
```


## Uygulamamızın bulunduğu dizine geçiş yapalım 

```
cd kubernetes-talos/
```

## Talos cluster için hazırladığımz dizindeki yml dosyasını çalıştıralım. 
```
kubectl apply -f flask-deployment.yml
```

## Uygulamaya erişebilmek için port-forward yapalım. Tarayıcıdan 'http://localhost:8080' portundan erişebiliriz.
```
kubectl port-forward service/flask-service 8080:80

```

## talos cluster silme
```
talosctl cluster destroy
```
