# Talos Odaklı Yapılandırma 

#Adımlar: 
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
 
 ```
talosctl kubeconfig    /home/yeager/.kube/talos-default -n 10.5.0.2 
```

```
export KUBECONFIG=~/.kube/talos-default
```

## talos cluster silme
```
talosctl cluster destroy
```